import time
import webbrowser

import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from TikTokLive.types.events import GiftEvent, FollowEvent

# import test.py
users = []

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
            "polling_interval_ms": 500,

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
            "lang": "nl-NL"

        }
    )
)

"""
@client.on("join")
async def on_join(event: JoinEvent):
    print(f"{event.user.uniqueId} is in de stream erbij gekomen!")
    webbrowser.open("like.mp3")
    print("(Plop sound)")
    print(f"    ")
"""

@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount == 1:
        webbrowser.open("like.mp3")
        # exec(open("test2.py").read())
        print(f"    ")
        print(f"{event.user.uniqueId} heeft Likes gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        print("(Plop sound)")
        print(f"    ")
        time.sleep(2)


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"    ")
    webbrowser.open("share.mp3")
    # exec(open("test4.py").read())
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print("(Shuuuiiii sound)")
    print(f"    ")
    print(f"    ")
    time.sleep(1)


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.extended_gift.name == "rose" or event.gift.extended_gift.name == "roos":
        if event.gift.repeat_end == 1:
            webbrowser.open("Rose.mp3")
            print(f"    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("(Are you sure about that sound)")
            print(f"    ")
            time.sleep(3)

        elif event.gift.gift_type != 1 and event.gift.extended_gift.name == "rose" or event.gift.extended_gift.name == "roos":
            webbrowser.open("Rose.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("(Are you sure about that sound)")
            print(f"    ")
            time.sleep(3)
    else:
        # If it's type 1 and the streak is over
        if event.gift.gift_type == 1:
            if event.gift.repeat_end == 1:
                webbrowser.open("EmotionalDamage.mp3")
                print(f"    ")
                print(
                    f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
                print(f"Dankjewel {event.user.uniqueId}!")
                print("(Emotional Damage sound)")
                print(f"    ")
                time.sleep(5)

            elif event.gift.gift_type != 1:
                webbrowser.open("EmotionalDamage.mp3")
                print(f"    ")
                print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                print(f"Dankjewel {event.user.uniqueId}!")
                print("(Emotional Damage sound)")
                print(f"    ")
                time.sleep(5)


@client.on("follow")
async def on_like(event: FollowEvent):
    if f"{event.user.uniqueId}" in users:
        print(f"    ")
        print(f"{event.user.uniqueId}, je hebt Renjestoo al gevolgd ;)")
        print(f"    ")
        print(f"    ")
        print(f"    ")
    else:
        users.append(f"{event.user.uniqueId}")
        # file_object = open('users.txt', 'a')
        # file_object.write("\n")
        # file_object.write(f"{event.user.uniqueId}")
        # file_object.close()
        webbrowser.open("follow.mp3")
        # exec(open("test3.py").read())
        print(f"    ")
        print(f"    ")
        print(f"    ")
        print(f"{event.user.uniqueId} heeft Renjestoo gevolgd!")
        print(f"Thanks voor de follow {event.user.uniqueId}, je bent een topper!")
        print("(Thank you for following sound)")
        print(f"    ")
        print(f"    ")
        print(f"    ")
        # time.sleep(6)
        time.sleep(3)


@client.on("comment")
async def on_connect(event: CommentEvent):
    evaluate = (f"{event.comment}")

    if (f"{event.comment}") == "/ping":
        print(f"{event.comment}")
        print("pong!")
    elif (f"{event.comment}") == "/help":
        print(f"    ")
        print("De beschikbare commando's zijn:")
        print("/help")
        print("/ping")
        print("/eval(en dan een som)")
        print(f"    ")
    elif "/eval" in (f"{event.comment}"):
        if "exec" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif (f"{event.comment}") == "/eval(exit())":
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif "system" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif "os" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif "()" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif "compile" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif "import" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        elif (f"{event.comment}") == "/eval(quit())":
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + ": Nope :)")
            print(f"    ")
        else:
            try:

                evaluate = (evaluate[5:250])
                print(f"    ")
                if print(len(eval(evaluate))) > 25:
                    print("Uitkomst is te lang!")
                else:
                    print(eval(evaluate))
            except:
                webbrowser.open("nope.mp3")
                (f"{event.user.uniqueId}" + "-> Dat commando bestaat niet :)")
                print("nope sound")
                pass
    else:
        print(f"    ")
        print(f"{event.user.uniqueId}: ")
        print(f"{event.comment}")
        print(f"    ")
        print(f"    ")


@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")


if __name__ == '__main__':
    print("Dit is een project die ik maak puur uit hobby.")
    print("Chats komen in het scherm te staan.")
    print("Follow, Share of Gift voor soundeffects.")
    client.run()
