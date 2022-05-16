import re
import urllib.parse
import urllib.request
import webbrowser
import time
import pywhatkit
import requests
from TikTokLive import *
from TikTokLive.types.events import *

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
@client.on("join")
async def on_join(event: JoinEvent):
    print(f"{event.user.uniqueId} is in de stream erbij gekomen!")
    webbrowser.open("like.mp3")

@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount == 1:
        webbrowser.open("like.mp3")
        # exec(open("test2.py").read())
        print(f"    ")
        print(f"{event.user.uniqueId} heeft Likes gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        print(f"    ")


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"    ")
    webbrowser.open("share.mp3")
    # exec(open("test4.py").read())
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print(f"    ")
    print(f"    ")


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            exec(open("Gift.py").read())
            time.sleep(3)
            print(f"    ")
            print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

        elif event.gift.gift_type != 1:
            exec(open("Gift.py").read())
            time.sleep(3)
            print(f"    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

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
        time.sleep(3)
        exec(open("test3.py").read())
        print(f"    ")
        print(f"    ")
        print(f"    ")
        print(f"{event.user.uniqueId} heeft Renjestoo gevolgd!")
        print(f"Thanks voor de follow {event.user.uniqueId}, je bent een topper!")
        print(f"    ")
        print(f"    ")
        print(f"    ")
        # time.sleep(6)


@client.on("comment")
async def on_connect(event: CommentEvent):
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
