import app
import tkinter as tk
from tkinter import *

#create a window with the title "TikTok Puller app"
root = tk.Tk()
root.title("TikTok Puller app")
root.geometry("500x500")
root.configure(background='#000000')


#add a readonly textbox the size of the window
text = tk.Text(root, height=400, width=450)
text.grid(row=0, column=0)
text.configure(wrap='word')


#add a close button to the window
button = tk.Button(root, text="Close", command=root.destroy)
button.grid(row=1, column=0)


#get comment from main and show it in the textbox
def show_output():
    text.delete('1.0', END)
    text.insert(END, app())
    root.update()
    root.after(1000, show_output)

#show the window
root.mainloop()
show_output()
print(app())
