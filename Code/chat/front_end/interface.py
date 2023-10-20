import tkinter as tk


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


def on_mousewheel(event):
    chat_text.yview_scroll(-1 * (event.delta // 300), "units")


def prevent_highlight(event):
    return 'break'


app = tk.Tk()
app.title("Game Chat")
app.minsize(800, 600)

# Sidebar for conversations
sidebar = tk.Listbox(app, bg='#1C1C1C')
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)

# Chat area
chat_frame = tk.Frame(app)
chat_frame.pack(padx=20, pady=(20, 10), fill=tk.BOTH, expand=True)

chat_text = tk.Text(chat_frame, wrap=tk.WORD, font=("Courier", 16), height=20, bd=0, bg='#1C1C1C')
chat_text.grid(row=0, column=0, sticky="nsew")
chat_text.config(takefocus=0)

chat_text.tag_configure('sender_tag', font=("Courier", 16, 'bold'))
chat_text.tag_configure('green_tag', foreground='#07B51E')
chat_text.tag_configure('orange_tag', foreground='#FC9D03')
chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
chat_text.configure(spacing1=5, spacing2=2, spacing3=0)

chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)

# Bind mouse scroll event to the chat_text widget
chat_text.bind("<MouseWheel>", on_mousewheel)
chat_text.bind("<Button-1>", prevent_highlight)
chat_text.bind("<B1-Motion>", prevent_highlight)
chat_text.bind("<T>", received_message('Aniusia', 'Nie wiem!!!'))

# Input area
input_frame = tk.Frame(app)
input_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

message_entry = tk.Entry(input_frame, width=50, bg='#1C1C1C')
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button_image = tk.PhotoImage(file='../../../Resources/images/send_icon.png')
send_button_icon = send_button_image.subsample(int(send_button_image.width() / 25))

send_button = tk.Button(input_frame, image=send_button_icon, command=sent_message)
send_button.pack(side=tk.RIGHT, padx=(10, 0))

message_entry.bind('<Return>', sent_message)

app.mainloop()
