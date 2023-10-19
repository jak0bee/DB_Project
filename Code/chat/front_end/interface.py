import tkinter as tk
from tkinter import scrolledtext


def send_message():
    message = message_entry.get()
    if message:
        chat_text.insert(tk.END, "You:\n", ('sender_tag', 'green_tag'))
        chat_text.insert(tk.END, f"{message}\n\n", ('message_tag', 'green_tag'))
        message_entry.delete(0, tk.END)
        # Here, you also add code to send the message to the server.


def receive_message():
    pass


app = tk.Tk()
app.title("Game Chat")

# Sidebar for conversations
sidebar = tk.Listbox(app)
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)

# Chat area
chat_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, font=("Arial", 16), height=20)
chat_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
chat_text.tag_configure('sender_tag', font=("Arial", 16, 'bold'))
chat_text.tag_configure('green_tag', foreground='#00FF00')
chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
chat_text.configure(spacing1=5, spacing2=2, spacing3=0)

# Input area
message_entry = tk.Entry(app, width=50)
message_entry.pack(padx=20, pady=20, side=tk.LEFT)
send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=(10, 20))

message_entry.bind('<Return>', send_message())

app.mainloop()
