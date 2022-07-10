import asyncio
import time
import webbrowser
import pyttsx3

import tkinter as tk
from tabnanny import check
from tkinter import *
import pafy
import vlc
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from youtubesearchpython import *
#import the tiktokGUI file
from tiktokGUI import *
import tiktokGUI

usersTxt = open("users.txt")
gifts = (open("gifts.txt"))
users = []
timer = 0
loop = asyncio.get_event_loop()
uniqueId = "renjestoo" #your unique id

songlist = open("songlist.txt")
last_song = ""
last_play_command = ""
engine = pyttsx3.init()

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@"+uniqueId, **(
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

"""


@client.on("join")
async def on_join(event: JoinEvent):
    print(f"    ")
    print(f"{event.user.uniqueId} has joined the livestream!\n")
    # webbrowser.open("like.mp3")
    print(f"    ")
"""

#calculate the time in seconds and minutes for the countdown() function
async def calculate_time(length):
    seconds = length % 60
    minutes = length // 60
    print(f"Wait {minutes} minutes and {seconds} seconds for the next request\n")
    await get_room_id()
    await client.send_message(f"Wait {minutes} minutes and {seconds} seconds for the next request", session_id)

async def countdown():
    global timer
    while timer > 0:
        timer -= 1
        await asyncio.sleep(1)
        if timer == 0:
            print("\n The nexts song request can be done :) \n")
            await client.send_message("The next song request can be done", session_id)
            print("Type /play artist and title to request a song")
            await client.send_message("Type /play artist and title to request a song", session_id)

async def songrequesttimer():
    requesttimer = 300
    while requesttimer > 0:
        requesttimer -= 1
        await asyncio.sleep(1)
        if requesttimer == 0:
            print(f"\n Hey {event.user.username}, you can request a song again! :) \n")
            print("Type /play artist and title to request a song")

@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount >= 100:
        webbrowser.open("like.mp3")
        print(f"    ")
        print(f"{event.user.uniqueId} sent likes!")
        print(f"Thanks {event.user.uniqueId}!")
        #add previous 3 prints to the textbox
        text.insert(END, f"{event.user.uniqueId} sent likes!")
        text.insert(END, f"Thanks {event.user.uniqueId}!")
        text.insert(END, f"\n")
        root.update()
        print(f"    ")


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"    ")
    print(f"{event.user.uniqueId} shared the livestream!")
    print(f"Thanks {event.user.uniqueId}!!!")
    engine.say(f"{event.user.uniqueId} shared the lifestream!")
    engine.runAndWait()
    engine.say(f"Thanks {event.user.uniqueId}!!!")
    engine.runAndWait()
    webbrowser.open("share.mp3")
    # print("(Shuuuiiii sound)")
    print(f"    ")
    print(f"    ")
    # time.sleep(1)


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
        if event.gift.repeat_end == 1:
            print("    ")
            print(
                f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Panda":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Panda":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Vingerhart":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Vingerhart":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Headphones":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count}\"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Headphones":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" gestuurd!")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "TikTok" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Choc Chip Cookie":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "TikTok" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Choc Chip Cookie":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Gift Box":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Gift Box":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Coffee":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Coffee":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            print("    ")
            print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
            engine.runAndWait()
            webbrowser.open("like.mp3")
            print(f"Thanks {event.user.uniqueId}!")
            print("    ")

    else:
        # If it's type 1 and the streak is over
        if event.gift.gift_type == 1:
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                print(f"    ")
                print(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
                engine.say(f"{event.user.uniqueId} has sent {event.gift.repeat_count} \"{event.gift.extended_gift.name}\" !")
                engine.runAndWait()
                webbrowser.open("like.mp3")
                print(f"Thanks {event.user.uniqueId}!")
                print(f"    ")

            elif event.gift.gift_type > 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                print(f"    ")
                print(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
                engine.say(f"{event.user.uniqueId} has sent a \"{event.gift.extended_gift.name}\" !")
                engine.runAndWait()
                webbrowser.open("like.mp3")
                print(f"Thanks {event.user.uniqueId}!")
                # print("(Emotional Damage sound)")
                print(f"    ")


@client.on("follow")
async def on_like(event: FollowEvent):
    if {event.user.uniqueId} in users:
        print(f"    ")
        print(f"Hey {event.user.uniqueId}, you already followed " + uniqueId + " ;)")
        print(f"    ")

    else:
        # user = (f"{event.user.uniqueId})
        with open("users.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(f"{event.user.uniqueId}")
        users.append({event.user.uniqueId})
        webbrowser.open("follow.mp3")
        print(f"    ")
        print(f"{event.user.uniqueId} followed " + uniqueId + " !")
        print(f"Thanks voor de follow {event.user.uniqueId}, you are amazing!")
        #print("(Thank you for following sound)")
        print(f"    ")
        # time.sleep(6)
        time.sleep(3)

@client.on("comment")
async def on_connect(event: CommentEvent):
    evaluate = (f"{event.comment}")
    global timer
    global last_song
    global last_play_command
    if (f"{event.comment}") == "/ping":
        print(f"    ")
        print(f"{event.user.uniqueId}" + " says ping")
        await client.send_message(f"{event.user.uniqueId}" + " says ping", session_id)
        print("I say: pong!")
        await client.send_message("I say: pong!", session_id)
        print(f"    ")
    elif "/play" in (f"{event.comment}"):
        tempSearch = (f"{event.comment}")
        videosSearch = VideosSearch(tempSearch[6:150], limit=1)
        if (f"{event.comment}" == "/play" or {event.comment} == "/Play"):
            print("There has to be a Artist and and a title to request a song.")
            await client.send_message("There has to be a Artist and and a title to request a song.", session_id)
        if "sus" in (f"{event.comment}") or "killer kamal" in (f"{event.comment}") or "troll" in (
                f"{event.comment}") or "rick roll" in (f"{event.comment}") or "never gonna give you up" in (
                f"{event.comment}") or "6IX9INE" in (f"{event.comment}") or "astley" in (f"{event.comment}"):
            print(f"{event.user.uniqueId} wants to request a song")
            print("Sorry, we won't listen to this ;)")
            print("")
        for i in range(1):
            link = (videosSearch.result()['result'][i]['link'])
            video = pafy.new(link)
            best = video.getbestaudio()
            length = video.length
            title = video.title
            likes = video.likes
            media = vlc.MediaPlayer(best.url)
            last_play_command = f"{event.user.uniqueId} + {tempSearch[6:50]}"
            if likes < 1000:
                print("Unpopular songs can't be requested.\n")
                await client.send_message("Unpopular songs can't be requested.", session_id)
            if title == last_song:
                print(f"Hey {event.user.uniqueId}, this song was already requested before, please try again later.")
                await client.send_message(f"Hey {event.user.uniqueId}, this song was already requested before, please try again later.", session_id)
            if timer == 0 and likes > 1000:
                timer = length
                if length > 400:
                    print("Please don't requests songs that are too long.")
                    await client.send_message("Please don't requests songs that are too long.", session_id)
                    print("Other people also want a chance to request ;)")
                    await client.send_message("Other people also want a chance to request ;)", session_id)
                    timer = 0
                else:
                    media.play()
                    media.audio_set_volume(75)

                    print(f"{event.user.uniqueId} has requested {title}")
                    await client.send_message(f"{event.user.uniqueId} has requested {title}", session_id)

                    print(f"\n Now playing: {title}")
                    await client.send_message("Now playing: {title}", session_id)

                    await calculate_time(timer)
                    last_song = title
                    await countdown()
            else:
                print(f"At the moment {last_song} is already playing.")
                await calculate_time(timer)

    elif (f"{event.comment}") == "/script":
        print("\nThe script is free on GitHub: http://github.com/renatokuipers.\n")
        await client.send_script("The script is free on GitHub: http://github.com/renatokuipers", session_id)
    elif (f"{event.comment}") == "/help":
        print("\nThe available commands are:\n- /script\n- /ping\n- /play artist and title of song\n- /calc(3*3) or /calc(2+4) or other sums\n- /viewers\n")
        await client.send_message("The available commands are:",session_id)
        await client.send_message("- /script",session_id)
        await client.send_message("- /ping",session_id)
        await client.send_message("- /play artist and title of song",session_id)
        await client.send_message("- /calc(3*3) or /calc(2+4) or other sums",session_id)
        await client.send_message("- /viewers",session_id)
    elif "/calc" in (f"{event.comment}"):
        if "exec" in (f"{event.comment}") or "exit" in (f"{event.comment}") or "quit" in (
                f"{event.comment}") or "import" in (f"{event.comment}") or "compile" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)\n")
        else:
            try:
                evaluate = (evaluate[5:250])
                print(f"    ")
                print(f"{event.user.uniqueId} asks \"{event.comment}\:")
                print(eval(evaluate))
                await client.send_message(eval(evaluate),session_id)
                print(f"    ")
            except:
                webbrowser.open("nope.mp3")
                print(f"{event.user.uniqueId}" + "-> that command doesn't exist :)\n")
                await client.send_message(f"{event.user.uniqueId}" + "-> that command doesn't exist :)",session_id)
                print("Type /help to see the available commands.")
                await client.send_message("Type /help to see the available commands.",session_id)
                # print("nope sound")
                pass
    elif "/viewers" in (f"{event.comment}"):
        viewers = str(client.viewer_count)
        if viewers != None:
            print(f"    ")
            print(f"{event.user.uniqueId} asks the amount of viewers in this livestream")
            await client.send_message(f"{event.user.uniqueId} asks the amount of viewers in this livestream",session_id)
            if viewers == 0:
                print("There are currently no viewers in this live.\n")
                await client.send_message("There are currently no viewers in this live.",session_id)
            elif viewers == 1:
                print(f"There is currently " + viewers + " viewer in this live.\n")
                await client.send_message(f"There is currently " + viewers + " viewer in this live.",session_id)
            else:
                print(f"There are currently " + viewers + " viewers in this live.\n")
                await client.send_message(f"There are currently " + viewers + " viewers in this live.",session_id)
    else:
        print(f"    ")
        print(f"{event.user.uniqueId}: \n{event.comment}\n")

@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")

if __name__ == '__main__':
    print("The script is on github.com/renatokuipers\nThis is a project I make purely for hobby.\nChats will appear in the screen.\nFollow, Share or Gift for soundeffects.\nType /help for commands\n")
    try:
        client.run()
    except:
        None, None
