import re
import requests
import urllib.parse
import urllib.request
import webbrowser
import pywhatkit
from pywhatkit import *

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *

# import test.py
file = "EmotionalDamage.mp3"
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
    webbrowser.open("share.mp3")
    # exec(open("test4.py").read())
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print(f"    ")
    print(f"    ")


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    # Rose
    if event.gift.gift_type == "Rose" or "Roos" or "rose" or "roos" and 1:
        if event.gift.repeat_end == 1:
            webbrowser.open("Rose.mp3")
            # exec(open("Rose_Gift.py").read())
            # time.sleep(4)
            print(f"    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")
        # It's not type 1, which means it can't have a streak & is automatically over
        elif event.gift.gift_type != 1:
            webbrowser.open("Rose.mp3")
            # exec(open("Rose_Gift.py").read())
            # time.sleep(4)
            print(f"    ")
            print(f"{event.user.uniqueId} heeft een \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

    # Panda
    if event.gift.gift_type == "Panda" or "panda" and 1:
        if event.gift.repeat_end == 1:
            webbrowser.open("Panda.mp3")
            # exec(open("Panda_Gift.py").read())
            # time.sleep(2)
            print(f"    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")
        # It's not type 1, which means it can't have a streak & is automatically over
        elif event.gift.gift_type != 1:
            webbrowser.open("Panda.mp3")
            # exec(open("Panda_Gift.py").read())
            # time.sleep(2)
            print(f"    ")
            print(f"{event.user.uniqueId} heeft een Panda gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

    # Other gifts
    elif event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            webbrowser.open("EmotionalDamage.mp3")
            # exec(open("Gift.py").read())
            # time.sleep(3)
            print(f"    ")
            print(
                f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")

        elif event.gift.gift_type != 1:
            webbrowser.open("EmotionalDamage.mp3")
            # exec(open("Gift.py").read())
            # time.sleep(3)
            print(f"    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print(f"    ")


#    if event.gift.gift_type == 1:
#        if event.gift.repeat_end == 1:
#            exec(open("Gift.py").read())
#            # time.sleep(3)
#            print(f"    ")
#            print(f"{event.user.uniqueId} heeft {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\" gestuurd!")
#            print(f"Dankjewel {event.user.uniqueId}!")
#            print(f"    ")

#        elif event.gift.gift_type != 1:
#            exec(open("Gift.py").read())
#            # time.sleep(3)
#            print(f"    ")
#            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
#            print(f"Dankjewel {event.user.uniqueId}!")
#            print(f"    ")

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
    command = f"{event.comment}"

    if command.find("-ytplay ") != 1:
        print(f"    ")
        print(f"{event.user.uniqueId}: ")
        print(f"{event.comment}")
        print(f"    ")
        print(f"    ")
        print(f"    ")
    else:
        #music_name = f"{event.comment}"
        #query_string = urllib.parse.urlencode({"search_query": music_name})
        #formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        #search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        #clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        #webbrowser.open("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        pywhatkit.playonyt(command.replace("-ytplay ", ""))
        print("Now playing" -> (command.replace("-ytplay ", ""))

if __name__ == '__main__':
    client.run()
