import asyncio
import time
import webbrowser

import PySimpleGUI as sg
import pafy
import vlc
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from youtubesearchpython import *

usersTxt = open("users.txt")
gifts = (open("gifts.txt"))
users = []
timer = 0
loop = asyncio.get_event_loop()

last_song = ""
last_play_command = ""

"""
introText = "Het script staat op github.com/renatokuipers\nDit is een project die ik maak puur uit hobby.\nChats komen in het scherm te staan.\nFollow, Share of Gift voor soundeffects.\nTyp /help voor commando's"

theme_dict = {'BACKGROUND': '#2B475D',
              'TEXT': '#FFFFFF',
              'INPUT': '#F2EFE8',
              'TEXT_INPUT': '#000000',
              'SCROLL': '#F2EFE8',
              'BUTTON': ('#000000', '#C2D4D8'),
              'PROGRESS': ('#FFFFFF', '#C7D5E0'),
              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20, 20), (20, 10))
BPAD_LEFT = ((20, 10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10, 20), (10, 20))

top_banner = [[sg.Text("TikTok Livechat with Requests!", font='Any 20', background_color=DARK_HEADER_COLOR)]]

block_1 = [[sg.Text('Chat', size=(40, 1))],
           [sg.Output(size=(700, 20), font=('Any 10'), key=("-OUT-"))]]

block_2 = [[sg.Text("Music requests", size=(40, 1))],
           [sg.Output(size=(700, 20), font=("Any 10"), key=("-MUSIC-"))]]

layout = [[sg.Column(top_banner, size=(700, 60), pad=(0, 0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(block_1, size=(700, 320), pad=BPAD_LEFT, background_color=BORDER_COLOR)],
          [sg.Column(block_2, size=(700, 80), pad=BPAD_LEFT, background_color=BORDER_COLOR)],
          [sg.Button("Exit")]]

window = sg.Window("Dashboard PySimpleGUI-Style", layout, margins=(0, 0), background_color=BORDER_COLOR,
                   no_titlebar=True, grab_anywhere=True, finalize=True)

while True:  # Event Loop
    window["-OUT-"].update()
    window["-MUSIC-"].update()
    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window["-OUT-"].write(
        "Het script staat op github.com/renatokuipers\nDit is een project die ik maak puur uit hobby.\nChats komen in het scherm te staan.\nFollow, Share of Gift voor soundeffects.\nTyp /help voor commando's")
    client: TikTokLiveClient = TikTokLiveClient(
        unique_id="@renjestoo", **(
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

    @client.on("join")
    async def on_join(event: JoinEvent):
        print(f"    ")
        print(f"{event.user.uniqueId} is in de stream erbij gekomen!")
        #webbrowser.open("like.mp3")
        #print("(Plop sound)")
        print(f"    ")


    async def countdown():
        global timer
        while timer > 0:
            timer -= 1
            await asyncio.sleep(1)
            if timer == 0:
                window["-MUSIC-"].write("\n De volgende song request kan gedaan worden :) \n")
                # print("\n De volgende song request kan gedaan worden :) \n")
    
    
    @client.on("like")
    async def on_like(event: LikeEvent):
        if event.likeCount > 0:
            webbrowser.open("like.mp3")
            # print(f"    ")
            window["-OUT-"].write(f"\n{event.user.uniqueId} heeft  Likes gestuurd!")
            # print(f"{event.user.uniqueId} heeft  Likes gestuurd!")
            window["-OUT-"].write(f"Dankjewel {event.user.uniqueId}!\n")
            # print(f"Dankjewel {event.user.uniqueId}!")
            # print("(Plop sound)")
            # print(f"    ")
            # time.sleep(1)
    
    
    @client.on("share")
    async def on_share(event: ShareEvent):
        # print(f"    ")
        webbrowser.open("share.mp3")
        window["-OUT-"].update(f"\n{event.user.uniqueId} heeft de stream gedeeld!\nDankjewel {event.user.uniqueId}!!!\n\n")
        # print(f"{event.user.uniqueId} heeft de stream gedeeld!")
        # print(f"Dankjewel {event.user.uniqueId}!!!")
        # print("(Shuuuiiii sound)")
        # print(f"    ")
        # print(f"    ")
        # time.sleep(1)
    
    
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        # If it's type 1 and the streak is over
        if event.gift.gift_type == 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
            if event.gift.repeat_end == 1:
                webbrowser.open("Rose.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x {event.gift.extended_gift.name} gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Rose.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Panda":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Panda.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Panda":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Panda.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Vingerhart":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("love.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Vingerhart":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("love.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Headphones":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Beat.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Headphones":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Beat.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "TikTok" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Choc Chip Cookie":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Gentleman.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "TikTok" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Choc Chip Cookie":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Gentleman.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Gift Box":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Welcome.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # rint(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Gift Box":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Welcome.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
        elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Coffee":
            if event.gift.repeat_end == 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Laugh.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
            elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Coffee":
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("Laugh.mp3")
                window["-OUT-"].update(
                    f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                # print("    ")
                # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                # print(f"Dankjewel {event.user.uniqueId}!")
                # print("    ")
                time.sleep(3)
    
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
                    webbrowser.open("EmotionalDamage.mp3")
                    window["-OUT-"].update(
                        f"\n{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                    # print(f"    ")
                    # print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                    # print(f"Dankjewel {event.user.uniqueId}!")
                    # print("(Emotional Damage sound)")
                    # print(f"    ")
                    time.sleep(5)
    
                elif event.gift.gift_type > 1:
                    with open("gifts.txt", "a+") as file_object:
                        file_object.seek(0)
                        data = file_object.read(100)
                        if len(data) > 0:
                            file_object.write("\n")
                        file_object.write(f"{event.gift.extended_gift.name}")
                    webbrowser.open("EmotionalDamage.mp3")
                    window["-OUT-"].update(
                        f"\n{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!\nDankjewel {event.user.uniqueId}!\n")
                    # print(f"    ")
                    # print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                    # print(f"Dankjewel {event.user.uniqueId}!")
                    # print("(Emotional Damage sound)")
                    # print(f"    ")
                    time.sleep(5)
    
    
    @client.on("follow")
    async def on_like(event: FollowEvent):
        if {event.user.uniqueId} in users:
            window["-OUT-"].update(f"\n{event.user.uniqueId}, je hebt Renjestoo al eens gevolgd ;)\n")
            # print(f"    ")
            # print(f"{event.user.uniqueId}, je hebt Renjestoo al eens gevolgd ;)")
            # print(f"    ")
    
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
            window["-OUT-"].update(
                f"\n{event.user.uniqueId} heeft Renjestoo gevolgd!\nThanks voor de follow {event.user.uniqueId}, je bent een topper!\n")
            # print(f"    ")
            # rint(f"{event.user.uniqueId} heeft Renjestoo gevolgd!")
            # print(f"Thanks voor de follow {event.user.uniqueId}, je bent een topper!")
            # print("(Thank you for following sound)")
            # print(f"    ")
            # time.sleep(6)
            time.sleep(3)
    
    
    @client.on("comment")
    async def on_connect(event: CommentEvent):
        evaluate = (f"{event.comment}")
        global timer
        global last_song
        global last_play_command
        if (f"{event.comment}") == "/ping":
            window["-OUT-"].update(f"\n{event.user.uniqueId}" + " zegt ping\nIk zeg: pong!\n")
            # print(f"    ")
            # print(f"{event.user.uniqueId}" + " zegt ping")
            # print("Ik zeg: pong!")
            # print(f"    ")
        elif "/play" in (f"{event.comment}"):
            tempSearch = (f"{event.comment}")
            videosSearch = VideosSearch(tempSearch[6:150], limit=1)
            if (f"{event.comment}" == "/play" or {event.comment} == "/Play"):
                window["-OUT-"].update("Er moet een Artiest en Titel toegevoegd worden.")
                # print("Er moet een Artiest en Titel toegevoegd worden.")
            if "sus" in (f"{event.comment}") or "killer kamal" in (f"{event.comment}") or "troll" in (
            f"{event.comment}") or "rick roll" in (f"{event.comment}") or "never gonna give you up" in (f"{event.comment}"):
                window["-OUT-"].update(
                    f"{event.user.uniqueId} wil graag een nummer luisteren waar we niet naar gaan luisteren ;)")
                # print(f"{event.user.uniqueId} wil graag een nummer luisteren waar we niet naar gaan luisteren ;)")
                # print("Hier gaan we niet naar luisteren ;)")
                # print("")
            for i in range(1):
                link = (videosSearch.result()['result'][i]['link'])
                video = pafy.new(link)
                best = video.getbestaudio()
                length = video.length
                title = video.title
                media = vlc.MediaPlayer(best.url)
                last_play_command = (f"{event.user.uniqueId} + {tempSearch[6:50]}")
                if title == last_song:
                    window["-OUT-"].update(f"{event.user.uniqueId}, Geen repeat van nummers achterelkaar.")
                    # print(f"{event.user.uniqueId}, Geen repeat van nummers achterelkaar.")
                if timer == 0:
                    timer = length
                    if length > 400:
                        window["-OUT-"].update("Geen te lange nummers aub\nAndere mensen moeten ook een kans krijgen ;)")
                        # print("Geen te lange nummers aub")
                        # print("Andere mensen moeten ook een kans krijgen ;)")
                    else:
                        media.play()
                        media.audio_set_volume(50)
                        # print(f"{event.user.uniqueId} heeft {title} aangevraagd")
                        window["-OUT-"].update(f"{event.user.uniqueId} heeft {title} aangevraagd")
                        # GUI.block_2(print(title))
                        window["-MUSIC-"].update("\n Now playing: " + title)
                        window["-MUSIC-"].update(f"\n Wacht {length} sec voor de volgende request. \n")
                        # print("\n Now playing: " + title)
                        # print(f"\n Wacht {length} sec voor de volgende request. \n")
                        last_song = title
                        await countdown()
                else:
                    window["-OUT-"].update(f"\n Nog {timer} sec voor de volgende request \n")
                    # print(f"\n Nog {timer} sec voor de volgende request \n")
    
        elif (f"{event.comment}") == "/script":
            window["-OUT-"].update("\n Het script is gratis op http://github.com/renatokuipers te vinden.\n")
            # print("\n Het script is gratis op http://github.com/renatokuipers te vinden.\n")
        elif (f"{event.comment}") == "/help":
            window["-OUT-"].update(
                "\nDe beschikbare commando's zijn:\n- /script\n- /ping\n- /play artist and title of song\n- /calc(3*3) of /calc(2+4) of andere sommen\n")
            # print("\nDe beschikbare commando's zijn:\n- /script\n- /ping\n- /play artist and title of song\n- /calc(3*3) of /calc(2+4) of andere sommen\n")
        elif "/calc" in (f"{event.comment}"):
            if "exec" in (f"{event.comment}") or "exit" in (f"{event.comment}") or "quit" in (
            f"{event.comment}") or "import" in (f"{event.comment}") or "compile" in (f"{event.comment}"):
                webbrowser.open("nope.mp3")
                window["-OUT-"].update(f"{event.user.uniqueId} wilde hacken -> Gaat niet gebeuren ;)")
                # print(f"    ")
                # print(f"{event.user.uniqueId}" + "-> Nope :)\nNope sound\n")
                # print("nope sound")
                # print(f"    ")
            else:
                try:
                    evaluate = (evaluate[5:250])
                    window["-OUT-"].update(f"\n{event.user.uniqueId} vraagt \"{event.comment}\:")
                    window["-OUT-"].update(eval(evaluate))
                    window["-OUT-"].update("\n")
                    # print(f"    ")
                    # print(f"{event.user.uniqueId} vraagt \"{event.comment}\:")
                    # print(eval(evaluate))
                    # print(f"    ")
                except:
                    webbrowser.open("nope.mp3")
                    window["-OUT-"].update(f"{event.user.uniqueId}" + "-> Dat commando bestaat niet :)")
                    # print(f"{event.user.uniqueId}" + "-> Dat commando bestaat niet :)\nNope sound")
                    # print("nope sound")
                    pass
        else:
            window["-OUT-"].update(f"\n{event.user.uniqueId}: \n{event.comment}\n\n")
            # print(f"    ")
            # print(f"{event.user.uniqueId}: \n{event.comment}\n\n")
            # print(f"{event.comment}")
            # print(f"    ")
            # print(f"    ")
    
    
    @client.on("live_end")
    async def on_connect(event: LiveEndEvent):
        # print(f"Livestream ended :(")
        window["-OUT-"].update("Livestream ended :(")
    
    
    if __name__ == '__main__':
        try:
            client.run()
        except:
            None, None
    window.close()
    """

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@renjestoo", **(
        {
            # Whether to process initial data (cached chats, etc.)
            "process_initial_data": True,

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
    print(f"{event.user.uniqueId} is in de stream erbij gekomen!")
    # webbrowser.open("like.mp3")
    # print("(Plop sound)")
    print(f"    ")


"""


async def countdown():
    global timer
    while timer > 0:
        timer -= 1
        await asyncio.sleep(1)
        if timer == 0:
            print("\n De volgende song request kan gedaan worden :) \n")


@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount >= 100:
        webbrowser.open("like.mp3")
        print(f"    ")
        print(f"{event.user.uniqueId} heeft  Likes gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        # print("(Plop sound)")
        print(f"    ")
        # time.sleep(1)


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"    ")
    webbrowser.open("share.mp3")
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print("(Shuuuiiii sound)")
    print(f"    ")
    print(f"    ")
    # time.sleep(1)


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
        if event.gift.repeat_end == 1:
            webbrowser.open("Rose.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Rose.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Panda":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Panda.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Panda":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Panda.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Vingerhart":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("love.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Finger Heart" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Vingerhart":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("love.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)
    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Headphones":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Beat.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Mini Speaker" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Headphones":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Beat.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
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
            webbrowser.open("Gentleman.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "TikTok" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Choc Chip Cookie":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Gentleman.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Gift Box":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Welcome.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Welcome" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Daisies" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Gift Box":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Welcome.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

    elif event.gift.gift_type == 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Coffee":
        if event.gift.repeat_end == 1:
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Laugh.mp3")
            print("    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Wishing Bottle" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "May" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Doughnut" or event.gift.gift_type > 1 and event.gift.extended_gift.name == "Coffee":
            with open("gifts.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(f"{event.gift.extended_gift.name}")
            webbrowser.open("Laugh.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("    ")
            time.sleep(3)

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
                webbrowser.open("EmotionalDamage.mp3")
                print(f"    ")
                print(
                    f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                print(f"Dankjewel {event.user.uniqueId}!")
                print("(Emotional Damage sound)")
                print(f"    ")
                time.sleep(5)

            elif event.gift.gift_type > 1:
                with open("gifts.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0:
                        file_object.write("\n")
                    file_object.write(f"{event.gift.extended_gift.name}")
                webbrowser.open("EmotionalDamage.mp3")
                print(f"    ")
                print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                print(f"Dankjewel {event.user.uniqueId}!")
                print("(Emotional Damage sound)")
                print(f"    ")
                time.sleep(5)


@client.on("follow")
async def on_like(event: FollowEvent):
    if {event.user.uniqueId} in users:
        print(f"    ")
        print(f"{event.user.uniqueId}, je hebt Renjestoo al eens gevolgd ;)")
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
        print(f"{event.user.uniqueId} heeft Renjestoo gevolgd!")
        print(f"Thanks voor de follow {event.user.uniqueId}, je bent een topper!")
        print("(Thank you for following sound)")
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
        print(f"{event.user.uniqueId}" + " zegt ping")
        print("Ik zeg: pong!")
        print(f"    ")
    elif "/play" in (f"{event.comment}"):
        tempSearch = (f"{event.comment}")
        videosSearch = VideosSearch(tempSearch[6:150], limit=1)
        if (f"{event.comment}" == "/play" or {event.comment} == "/Play"):
            print("Er moet een Artiest en Titel toegevoegd worden.")
        if "sus" in (f"{event.comment}") or "killer kamal" in (f"{event.comment}") or "troll" in (
                f"{event.comment}") or "rick roll" in (f"{event.comment}") or "never gonna give you up" in (
        f"{event.comment}"):
            print(f"{event.user.uniqueId} wil graag een nummer luisteren")
            print("Hier gaan we niet naar luisteren ;)")
            print("")
        for i in range(1):
            link = (videosSearch.result()['result'][i]['link'])
            video = pafy.new(link)
            best = video.getbestaudio()
            length = video.length
            title = video.title
            media = vlc.MediaPlayer(best.url)
            last_play_command = (f"{event.user.uniqueId} + {tempSearch[6:50]}")
            if title == last_song:
                print(f"{event.user.uniqueId}, Geen repeat van nummers achterelkaar.")
            if timer == 0:
                timer = length
                if length > 400:
                    print("Geen te lange nummers aub")
                    print("Andere mensen moeten ook een kans krijgen ;)")
                    timer = 0
                else:
                    media.play()
                    media.audio_set_volume(50)
                    print(f"{event.user.uniqueId} heeft {title} aangevraagd")
                    # GUI.block_2(print(title))
                    print("\n Now playing: " + title)
                    print(f"\n Wacht {length} sec voor de volgende request. \n")
                    last_song = title
                    await countdown()
            else:
                print(f" \n Nog {timer} sec voor de volgende request \n")

    elif (f"{event.comment}") == "/script":
        print("\n Het script is gratis op http://github.com/renatokuipers te vinden.\n")
    elif (f"{event.comment}") == "/help":
        print(
            "\nDe beschikbare commando's zijn:\n- /script\n- /ping\n- /play artist and title of song\n- /calc(3*3) of /calc(2+4) of andere sommen\n")
        # print("- /script")
        # print("- /ping")
        # print("- /play artist and title of song")
        # print("- /calc(3*3) of /calc(2+4) of andere sommen\n")
    elif "/calc" in (f"{event.comment}"):
        if "exec" in (f"{event.comment}") or "exit" in (f"{event.comment}") or "quit" in (
                f"{event.comment}") or "import" in (f"{event.comment}") or "compile" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)\nNope sound\n")
            # print("nope sound")
            # print(f"    ")
        else:
            try:
                evaluate = (evaluate[5:250])
                print(f"    ")
                print(f"{event.user.uniqueId} vraagt \"{event.comment}\:")
                print(eval(evaluate))
                print(f"    ")
            except:
                webbrowser.open("nope.mp3")
                print(f"{event.user.uniqueId}" + "-> Dat commando bestaat niet :)\nNope sound")
                # print("nope sound")
                pass
    else:
        print(f"    ")
        print(f"{event.user.uniqueId}: \n{event.comment}\n\n")
        # print(f"{event.comment}")
        # print(f"    ")
        # print(f"    ")


@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")


if __name__ == '__main__':
    print("Het script staat op github.com/renatokuipers\nDit is een project die ik maak puur uit hobby.\nChats komen in het scherm te staan.\nFollow, Share of Gift voor soundeffects.\nTyp /help voor commando's")
    # print("Dit is een project die ik maak puur uit hobby.")
    # print("Chats komen in het scherm te staan.")
    # print("Follow, Share of Gift voor soundeffects.")
    # print("Typ /help voor commando's")
    try:
        client.run()
    except:
        None, None
