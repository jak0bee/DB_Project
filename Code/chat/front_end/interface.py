import tkinter as tk
from tkinter import scrolledtext


def send_message():
    message = message_entry.get()
    if message:
        chat_text.insert(tk.END, "You:" + '\t', 'you_tag')
        chat_text.insert(tk.END, f"{message}\n", ('message_tag', 'you_tag'))
        message_entry.delete(0, tk.END)
        # Here, you also add code to send the message to the server.


app = tk.Tk()
app.title("Game Chat")

# Sidebar for conversations
sidebar = tk.Listbox(app)
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)

# Chat area
chat_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, font=("Arial", 16))
chat_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
chat_text.tag_configure('you_tag', foreground='#00FF00')
chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
chat_text.configure(spacing1=5, spacing3=5)

# Input area
message_entry = tk.Entry(app, width=50)
message_entry.pack(padx=20, pady=20, side=tk.LEFT)
send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(padx=20, side=tk.LEFT)

app.mainloop()
