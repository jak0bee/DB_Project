#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
import tkinter as tk
from PIL import ImageTk
from PIL import Image


def sent_message(event=None):
    message = message_entry.get()
    if message:
        display_message('You', message, 'green_tag')
        message_entry.delete(0, tk.END)
        # Here, you also add code to send the message to the server


def received_message(sender_name: str, message: str) -> None:
    display_message(sender_name, message, 'orange_tag')


def display_message(sender_name: str, message: str, color_tag: str) -> None:
    chat_text.insert(tk.END, f"{sender_name}:\n", ('sender_tag', color_tag))
    chat_text.insert(tk.END, f"{message}\n\n", ('message_tag', color_tag))


current_y_position = 0
image_to_text = dict()


def add_conversation(conversation_type: str, conversation_name: str):
    global current_y_position

    img_id = sidebar.create_image(0, current_y_position, anchor=tk.NW, image=idle_conversation, tags="clickableImage")

    upper_left_text_id = sidebar.create_text(10, current_y_position + 5, text=conversation_type, anchor=tk.NW,
                                             fill="white", tags="clickableImage")

    if len(conversation_name) >= 30:
        conversation_name = conversation_name[:27] + '...'
    lower_right_text_id = sidebar.create_text(190, current_y_position + 70, text=conversation_name, anchor=tk.SE,
                                              fill="white", tags="clickableImage")
    image_to_text[img_id] = (upper_left_text_id, lower_right_text_id)

    sidebar.tag_bind(img_id, '<Button-1>', select_conversation)
    current_y_position += idle_conversation.height() + 5
    sidebar.config(scrollregion=sidebar.bbox(tk.ALL))


def select_conversation(event):
    for img_id in sidebar.find_withtag("clickableImage"):
        if sidebar.type(img_id) == "image":
            sidebar.itemconfig(img_id, image=idle_conversation)
            text_ids = image_to_text[img_id]
            for text_id in text_ids:
                sidebar.itemconfig(text_id, fill="white")

    clicked_conversation = sidebar.find_withtag(tk.CURRENT)
    if clicked_conversation and sidebar.type(clicked_conversation) == "image":
        sidebar.itemconfig(clicked_conversation, image=selected_conversation)
        text_ids = image_to_text[clicked_conversation[0]]
        for text_id in text_ids:
            sidebar.itemconfig(text_id, fill="black")

    chat_text.delete(1.0, tk.END)


def on_mousewheel(event):
    chat_text.yview_scroll(-1 * (event.delta // 300), "units")


def prevent_highlight(event):
    return 'break'


def on_sidebar_scroll(event):
    """Handle scrolling of the canvas."""
    delta = -1 * int(event.delta)
    sidebar.yview_scroll(delta, "units")


app = tk.Tk()
app.title("Game Chat")
app.configure(bg='#242424')
app.minsize(800, 600)

sidebar_frame = tk.Frame(app, bg='#1A1A1A')
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

# Chat area
chat_frame = tk.Frame(app)
chat_frame.pack(padx=20, pady=(20, 10), fill=tk.BOTH, expand=True)

chat_text = tk.Text(chat_frame, wrap=tk.WORD, font=("Courier", 16), height=20, bd=0, bg='#1A1A1A')
chat_text.grid(row=0, column=0, sticky="nsew")
chat_text.config(takefocus=0)

chat_text.tag_configure('sender_tag', font=("Courier", 16, 'bold'))
chat_text.tag_configure('green_tag', foreground='#07B51E')
chat_text.tag_configure('orange_tag', foreground='#FC9D03')
chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
chat_text.configure(spacing1=5, spacing2=2, spacing3=0)

chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)

chat_text.bind("<MouseWheel>", on_mousewheel)
chat_text.bind("<Button-1>", prevent_highlight)
chat_text.bind("<B1-Motion>", prevent_highlight)
chat_text.bind("<T>", received_message('Aniusia', 'Nie wiem!!!'))

# Input area
input_frame = tk.Frame(app, bg='#242424')
input_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

message_entry = tk.Entry(input_frame, width=50, bg='#1C1C1C', foreground='#E3E3E3')
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button_image = tk.PhotoImage(file='../../../Resources/images/send_icon.png')
send_button_icon = send_button_image.subsample(int(send_button_image.width() / 25))

send_button = tk.Button(input_frame, image=send_button_icon, command=sent_message)
send_button.pack(side=tk.RIGHT, padx=(10, 0))

message_entry.bind('<Return>', sent_message)

for _ in range(30):
    add_conversation('private', 'sample')

app.mainloop()
