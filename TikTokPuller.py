from youtubesearchpython import *
import tkinter as tk
from tkinter import *
from main import *

#create a new window
root = tk.Tk()
root.title("TikTok Puller")
root.geometry("500x500")
root.configure(background='#000000')

#add a readonly textbox the size of the window
text = tk.Text(root, height=400, width=450)
text.grid(row=0, column=0)
text.configure(wrap='word')


#add a close button to the window
button = tk.Button(root, text="Close", command=root.destroy)
button.grid(row=1, column=0)

#show output from main in the textbox
def show_output():
    text.delete('1.0', END)
    text.insert(END, main())
    root.update()
    root.after(1000, show_output)

#show the window
root.mainloop()