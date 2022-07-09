import TikTokPuller

import tkinter as tk
from tkinter import *

#create a window with the title "TikTok Puller app"
root = tk.Tk()
root.title("TikTok Puller app")

#add a readonly chatbox to the window
chatbox = tk.Text(root, height=15, width=50, state='disabled')
chatbox.grid(row=0, column=0, columnspan=2)

#add comments from TikTokPuller.py into the chatbox
def add_comment(comment):
    chatbox.config(state='normal')
    chatbox.insert(tk.END, comment)
    chatbox.config(state='disabled')
    chatbox.see(tk.END)

#loop through the comments and add them to the chatbox
for comment in TikTokPuller.get_comments():
    add_comment(comment)

#show the window
root.mainloop()