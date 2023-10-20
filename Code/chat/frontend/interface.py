# Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
import tkinter as tk

import socketio
from PIL import Image
from PIL import ImageTk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chat.tables.chat_tables import ChatSession, GroupChatMember, ChatMessage
from data_interaction.entities import Player
from database_actions import db, app, database_url


def chat_interface():
    sio = socketio.Client()


    @sio.on('received_message')
    def on_received_message(data):
        sender_id = data['sender_id']
        message = data['message']

        if sender_id != user_id:
            sender_name = session.query(Player.player_name).filter(sender_id == Player.id).first()
            display_message(sender_name, message, 'orange_tag')


    def sent_message(event=None):
        global current_session_id
        message = message_entry.get()

        if message:
            # commands
            if message[0] == '/':
                if message.startswith('/create_chat'):
                    session_name = message[13:]
                    if len(session_name) <= 200:
                        with app.app_context():
                            new_chat_session = ChatSession(session_name=session_name)
                            db.session.add(new_chat_session)
                            db.session.commit()
                            new_chat_session = session.query(ChatSession).filter_by(session_name=session_name).first()

                            new_group_chat_member = GroupChatMember(session_id=new_chat_session.id, player_id=user_id)
                            db.session.add(new_group_chat_member)
                            db.session.commit()

                            add_conversation(session_name, new_chat_session.id)
                            select_conversation(default_img_id=new_chat_session.id)
                            current_session_id = new_chat_session
                    else:
                        chat_text.insert(tk.END, 'Chat name too long!')

                elif message.startswith('/add_player'):
                    player_id = message[12:]
                    if player_id.isdigit():
                        player_id = int(player_id)
                        new_group_chat_member = GroupChatMember(session_id=current_session_id, player_id=player_id)
                        db.session.add(new_group_chat_member)
                        db.session.commit()
                        chat_text.insert(tk.END, f'player {player_id} added', 'message_tag')

                message_entry.delete(0, tk.END)

            # messages
            else:
                display_message('You', message, 'green_tag')
                message_entry.delete(0, tk.END)
                with app.app_context():
                    new_message = ChatMessage(session_id=current_session_id, sender_id=user_id, message_text=message)
                    db.session.add(new_message)
                    db.session.commit()

                sio.emit('send_message', {
                    'sender_id': user_id,
                    'session_id': current_session_id,
                    'message': message
                })


    def display_message(sender_name: str, message: str, color_tag=None) -> None:
        chat_text.insert(tk.END, f"{sender_name}:\n", ('sender_tag', color_tag))
        chat_text.insert(tk.END, f"{message}\n\n", ('message_tag', color_tag))


    current_y_position = 0
    image_to_text = dict()


    def add_conversation(conversation_name: str, this_conversation_id: int):
        global current_y_position

        img_id = sidebar.create_image(0, current_y_position, anchor=tk.NW, image=idle_conversation,
                                      tags="clickableImage")

        if len(conversation_name) >= 30:
            conversation_name = conversation_name[:27] + '...'
        lower_right_text_id = sidebar.create_text(190, current_y_position + 70, text=conversation_name, anchor=tk.SE,
                                                  fill="white", tags="clickableImage")

        image_to_text[img_id] = (lower_right_text_id, conversation_name, this_conversation_id)

        sidebar.tag_bind(img_id, '<Button-1>', select_conversation)
        current_y_position += idle_conversation.height() + 5
        sidebar.config(scrollregion=sidebar.bbox(tk.ALL))
        select_conversation(default_img_id=img_id)

        return img_id


    def select_conversation(event=None, default_img_id=None):
        for img_id in sidebar.find_withtag("clickableImage"):
            if sidebar.type(img_id) == "image":
                sidebar.itemconfig(img_id, image=idle_conversation)
                text_ids = image_to_text[img_id][:2]
                for text_id in text_ids:
                    sidebar.itemconfig(text_id, fill="white")

        items_with_current_tag = sidebar.find_withtag(tk.CURRENT)
        if default_img_id:
            clicked_conversation = default_img_id
        else:
            if items_with_current_tag:
                clicked_conversation = sidebar.find_withtag(tk.CURRENT)[0]
            else:
                clicked_conversation = False

        if clicked_conversation and sidebar.type(clicked_conversation) == "image":
            sidebar.itemconfig(clicked_conversation, image=selected_conversation)
            text_ids = image_to_text[clicked_conversation][:2]
            for text_id in text_ids:
                sidebar.itemconfig(text_id, fill="black")

            _, conversation_name, session_id = image_to_text[clicked_conversation]
            session_messages = (session.query(ChatMessage)
                                .filter(ChatMessage.session_id == session_id)
                                .order_by(ChatMessage.sent_at)
                                .all())

            global current_session_id
            current_session_id = session_id

            chat_text.delete(1.0, tk.END)
            for message in session_messages:
                message_text = message.message_text
                player = session.query(Player).filter_by(id=message.sender_id).first()
                tag = 'green_tag' if player.id == user_id else 'orange_tag'
                player_name = player.player_name if tag == 'orange_tag' else 'You'
                display_message(player_name, message_text, tag)

            chat_label.config(text=conversation_name)


    def on_mousewheel(event):
        chat_text.yview_scroll(-1 * (event.delta // 300), "units")


    def prevent_highlight(event):
        return 'break'


    def on_sidebar_scroll(event):
        """Handle scrolling of the canvas."""
        delta = -1 * int(event.delta)
        sidebar.yview_scroll(delta, "units")


    root = tk.Tk()
    root.title("Game Chat")
    root.configure(bg='#242424')
    root.minsize(800, 600)

    sidebar_frame = tk.Frame(root, bg='#1A1A1A')
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Create a vertical scrollbar for the canvas
    scrollbar = tk.Scrollbar(sidebar_frame, orient="vertical")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    sidebar = tk.Canvas(sidebar_frame, bg='#1A1A1A', width=200, yscrollcommand=scrollbar.set)
    sidebar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=sidebar.yview)
    scrollbar.pack_forget()
    sidebar.bind("<MouseWheel>", on_sidebar_scroll)

    pil_image = Image.open('../../../Resources/images/conversation_idle.png')
    pil_image = pil_image.resize((200, 90), Image.LANCZOS)
    idle_conversation = ImageTk.PhotoImage(pil_image)
    pil_image = Image.open('../../../Resources/images/conversation_selected.png')
    pil_image = pil_image.resize((200, 90), Image.LANCZOS)
    selected_conversation = ImageTk.PhotoImage(pil_image)

    chat_topbar = tk.Frame(root, bg='#1A1A1A', height=50)
    chat_topbar.pack(fill=tk.X, padx=5, pady=(0, 0), side=tk.TOP)
    chat_label = tk.Label(chat_topbar, text="", bg='#1A1A1A', fg='white', font=("Courier", 16), padx=10)
    chat_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Chat Area
    chat_frame = tk.Frame(root)
    chat_frame.pack(padx=5, pady=(2, 10), fill=tk.BOTH, expand=True)

    chat_text = tk.Text(chat_frame, wrap=tk.WORD, font=("Courier", 16), height=20, bd=0, bg='#1A1A1A')
    chat_text.pack(fill=tk.BOTH, expand=True)
    chat_text.tag_configure('sender_tag', font=("Courier", 16, 'bold'))
    chat_text.tag_configure('green_tag', foreground='#07B51E')
    chat_text.tag_configure('orange_tag', foreground='#FC9D03')
    chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
    chat_text.configure(spacing1=5, spacing2=2, spacing3=0)
    chat_text.bind("<MouseWheel>", on_mousewheel)
    chat_text.bind("<Button-1>", prevent_highlight)
    chat_text.bind("<B1-Motion>", prevent_highlight)

    # Input area
    input_frame = tk.Frame(root, bg='#242424')
    input_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

    message_entry = tk.Entry(input_frame, width=50, bg='#1C1C1C', foreground='#E3E3E3')
    message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    send_button_image = tk.PhotoImage(file='../../../Resources/images/send_icon.png')
    send_button_icon = send_button_image.subsample(int(send_button_image.width() / 25))
    send_button = tk.Button(input_frame, image=send_button_icon, command=sent_message)
    send_button.pack(side=tk.RIGHT, padx=(10, 0))
    message_entry.bind('<Return>', sent_message)

    if sidebar.find_withtag("clickableImage"):
        first_conversation_id = sidebar.find_withtag("clickableImage")[0]
        select_conversation(default_img_id=first_conversation_id)

    Session = sessionmaker(bind=create_engine(database_url))
    session = Session()
    global user_id
    while True:
        input_id = input('Enter your user number (id): ')
        if input_id.isdigit():
            user_id = session.get(Player, int(input_id))
            if user_id:
                user_id = user_id.id
                break

    open_conversations = [sid[0] for sid in
                          session.query(GroupChatMember.session_id).filter(GroupChatMember.player_id == user_id).all()]
    for conversation_id in reversed(open_conversations):
        chat_session = session.get(ChatSession, conversation_id)
        add_conversation(chat_session.session_name, chat_session.id)

    global current_session_id
    if open_conversations:
        select_conversation([key for key, val in image_to_text.items() if val[2] == open_conversations[-1]][0])
        current_session_id = open_conversations[-1]

    session.close()

    sio.connect('http://localhost:5000')

    root.mainloop()
