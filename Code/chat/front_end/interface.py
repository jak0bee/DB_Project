import os
import tkinter as tk
from tkinter import font as tkFont


def send_message(event=None):
    message = message_entry.get()
    if message:
        chat_text.insert(tk.END, "You:\n", ('sender_tag', 'green_tag'))
        chat_text.insert(tk.END, f"{message}\n\n", ('message_tag', 'green_tag'))
        message_entry.delete(0, tk.END)
        # Here, you also add code to send the message to the server.


def on_mousewheel(event):
    chat_text.yview_scroll(-1 * (event.delta // 300), "units")


def prevent_highlight(event):
    return 'break'


def load_custom_font(font_path):
    # Register the custom font and return its name
    font_name = tkFont.Font(file=font_path).actual()['family']
    return font_name


app = tk.Tk()
app.title("Game Chat")
app.minsize(800, 600)

# Sidebar for conversations
sidebar = tk.Listbox(app)
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)

# Chat area
chat_frame = tk.Frame(app)
chat_frame.pack(padx=20, pady=(20, 10), fill=tk.BOTH, expand=True)

chat_text = tk.Text(chat_frame, wrap=tk.WORD, font=("Arial", 16), height=20, bg="#f5f5f5", bd=0)
chat_text.grid(row=0, column=0, sticky="nsew")
chat_text.config(takefocus=0)

custom_font_name = load_custom_font('../../../Resources/fonts/Bender-Thin.otf')

chat_text.tag_configure('sender_tag', font=(custom_font_name, 12))
chat_text.tag_configure('green_tag', foreground='#00FF00')
chat_text.tag_configure('message_tag', lmargin1=50, lmargin2=50)
chat_text.configure(spacing1=5, spacing2=2, spacing3=0)

chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)

# Bind mouse scroll event to the chat_text widget
chat_text.bind("<MouseWheel>", on_mousewheel)
chat_text.bind("<Button-1>", prevent_highlight)
chat_text.bind("<B1-Motion>", prevent_highlight)

# Input area
input_frame = tk.Frame(app)
input_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

message_entry = tk.Entry(input_frame, width=50)
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=(10, 20))

message_entry.bind('<Return>', send_message)

app.mainloop()
