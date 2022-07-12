import asyncio
import time
import webbrowser
import pyttsx3

import tkinter as tk
from tabnanny import check
from tkinter import *
import pafy
import vlc
import threading
import app
from app import *
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from youtubesearchpython import *

unique_Id = "simgishbackup"

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@"+unique_Id, **(
        {
            # Whether to process initial data (cached chats, etc.)
            "process_initial_data": False,

            # Connect info (viewers, stream status, etc.)
            "fetch_room_info_on_connect": True,

            # Whether to get extended gift info (Image URLs, etc.)
            "enable_extended_gift_info": True,

            # How frequently to poll Webcast API
            "polling_interval_ms": 1000,

            # Custom Client params
            "client_params": {},

            # Custom request headers
            "headers": {},

            # Custom timeout for Webcast API requests
            "timeout_ms": 5000,

            # Custom Asyncio event loop
            "loop": None,

            # Whether to trust environment variables that provide proxies to be used in aiohttp requests
            "trust_env": False,

            # A ProxyContainer object for proxied requests
            "proxy_container": None,

            # Set the language for Webcast responses (Changes extended_gift's language)
            "lang": "en-US"

        }
    )
)


root = Tk()
root.title("TikTok Interactive App")
root.geometry("600x750")
root.config(background="#71a5d9")

chatbox = Listbox(root, height=20, width=94)
chatbox.place(x=15, y=80)

#add a listbox with the name Current Song beneath the chatbox
currentsong = Listbox(root, height=1, width=94)
currentsong.place(x=15, y=600)

#add a timer beneath the currentsong listbox
timer = Listbox(root, height=1, width=94)
timer.place(x=15, y=620)



#when client gets a comment from the server, send it to the chatbox
@client.on("comment")
async def on_connect(event: CommentEvent):
    #add the comment to the chatbox
    chatbox.insert(END, event.user.uniqueId + ":")
    chatbox.insert(END, event.comment)
    chatbox.insert(END, "")
    root.update()

root.update()
if __name__ == '__main__':
    client.run()

