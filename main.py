from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, LikeEvent, FollowEvent, ShareEvent
from playsound import playsound
import os, subprocess
#import test.py
file = "EmotionalDamage.mp3"


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
            "timeout_ms": 1000,

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
@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            exec(open("test.py").read())
            print(f"    ")
            print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        exec(open("test.py").read())
        print(f"    ")
        print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        print(f"    ")

@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount == 1:
        #exec(open("test2.py").read())
        print(f"    ")
        print(f"{event.user.uniqueId} heeft Likes gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        print(f"    ")

@client.on("follow")
async def on_like(event: FollowEvent):
    exec(open("test3.py").read())
    print(f"    ")
    print(f"    ")
    print(f"    ")
    print(f"{event.user.uniqueId} heeft Renjestoo gevolgd!")
    print(f"Thanks voor de follow {event.user.uniqueId}, je bent een topper!")
    print(f"    ")
    print(f"    ")
    print(f"    ")

@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"    ")
    print(f"{event.user.nickname}: ")
    print(f"{event.comment}")
    print(f"    ")
    print(f"    ")
    print(f"    ")

@client.on("share")
async def on_share(event: ShareEvent):
    exec(open("test4.py").read())
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print(f"    ")
    print(f"    ")

if __name__ == '__main__':
    client.run()