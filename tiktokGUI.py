#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated  by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jul 10, 2022 11:36:25 AM CEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tiktokGUI_support
import app
from app import *
import threading

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x750+430+196")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("TikTok Interactive Chat App")
        top.configure(background="#71a5d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.timer_bar = tk.IntVar()

        self.Chatbox_Label = tk.Label(self.top)
        self.Chatbox_Label.place(relx=0.35, rely=0.013, height=22, width=154)
        self.Chatbox_Label.configure(activebackground="#f9f9f9")
        self.Chatbox_Label.configure(background="#ffffff")
        self.Chatbox_Label.configure(compound='center')
        self.Chatbox_Label.configure(disabledforeground="#a3a3a3")
        self.Chatbox_Label.configure(foreground="#000000")
        self.Chatbox_Label.configure(highlightbackground="#d9d9d9")
        self.Chatbox_Label.configure(highlightcolor="black")
        self.Chatbox_Label.configure(relief="raised")
        self.Chatbox_Label.configure(text='''ChatBox''')

        self.Chatbox = tk.Text(self.top)
        self.Chatbox.place(relx=0.017, rely=0.053, relheight=0.632, relwidth=0.957)
        self.Chatbox.configure(background="#c0c0c0")
        self.Chatbox.configure(blockcursor="1")
        self.Chatbox.configure(cursor="")
        self.Chatbox.configure(font="TkTextFont")
        self.Chatbox.configure(foreground="black")
        self.Chatbox.configure(highlightbackground="#d9d9d9")
        self.Chatbox.configure(highlightcolor="black")
        self.Chatbox.configure(insertbackground="black")
        self.Chatbox.configure(selectbackground="#c4c4c4")
        self.Chatbox.configure(selectforeground="black")
        self.Chatbox.configure(wrap="word")

        self.Current_Song_Label = tk.Label(self.top)
        self.Current_Song_Label.place(relx=0.017, rely=0.693, height=21, width=124)
        self.Current_Song_Label.configure(activebackground="#f9f9f9")
        self.Current_Song_Label.configure(background="#ffffff")
        self.Current_Song_Label.configure(compound='left')
        self.Current_Song_Label.configure(disabledforeground="#a3a3a3")
        self.Current_Song_Label.configure(foreground="#000000")
        self.Current_Song_Label.configure(highlightbackground="#d9d9d9")
        self.Current_Song_Label.configure(highlightcolor="black")
        self.Current_Song_Label.configure(relief="raised")
        self.Current_Song_Label.configure(text='''Current Song''')

        self.CurrentSong = tk.Text(self.top)
        self.CurrentSong.place(relx=0.017, rely=0.733, relheight=0.085, relwidth=0.473)
        self.CurrentSong.configure(background="#c0c0c0")
        self.CurrentSong.configure(cursor="")
        self.CurrentSong.configure(font="TkTextFont")
        self.CurrentSong.configure(foreground="black")
        self.CurrentSong.configure(highlightbackground="#d9d9d9")
        self.CurrentSong.configure(highlightcolor="black")
        self.CurrentSong.configure(insertbackground="black")
        self.CurrentSong.configure(selectbackground="#c4c4c4")
        self.CurrentSong.configure(selectforeground="black")
        self.CurrentSong.configure(wrap="word")

        self.Time_Label = tk.Label(self.top)
        self.Time_Label.place(relx=0.017, rely=0.827, height=21, width=114)
        self.Time_Label.configure(activebackground="#f9f9f9")
        self.Time_Label.configure(background="#ffffff")
        self.Time_Label.configure(compound='left')
        self.Time_Label.configure(disabledforeground="#a3a3a3")
        self.Time_Label.configure(foreground="#000000")
        self.Time_Label.configure(highlightbackground="#d9d9d9")
        self.Time_Label.configure(highlightcolor="black")
        self.Time_Label.configure(relief="raised")
        self.Time_Label.configure(text='''Time till next song''')

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.017, rely=0.867, relheight=0.032, relwidth=0.473)

        self.Text1.configure(background="#c0c0c0")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Progress_Next_Song = ttk.Progressbar(self.top)
        self.Progress_Next_Song.place(relx=0.017, rely=0.907, relwidth=0.467, relheight=0.0, height=22)
        self.Progress_Next_Song.configure(length="280")
        self.Progress_Next_Song.configure(variable=self.timer_bar)


def start_up():
    tiktokGUI_support.main()

if __name__ == '__main__':
    threading.Thread(tiktokGUI_support.main())
    app.client.run()
