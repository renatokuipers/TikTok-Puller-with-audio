import math
import time
import webbrowser
import tk
from tk import *
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
#from TikTokLive.types.events import GiftEvent, FollowEvent

# users that followed
# utf = users.txt

# users that liked
# utl = usersL.txt

users = []
lq = []
fq = []
sq = []
gq = []

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
            "lang": "en-US"

        }
    )
)

"""
@client.on("join")
async def on_join(event: JoinEvent):
    print(f"    ")
    print(f"{event.user.uniqueId} is in de stream erbij gekomen!")
    #webbrowser.open("like.mp3")
    #print("(Plop sound)")
    print(f"    ")
"""

@client.on("like")
async def on_like(event: LikeEvent):
    if event.likeCount == 1:
        webbrowser.open("like.mp3")
        print(f"    ")
        print(f"{event.user.uniqueId} heeft  Likes gestuurd!")
        print(f"Dankjewel {event.user.uniqueId}!")
        # print("(Plop sound)")
        print(f"    ")
        #time.sleep(1)


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"    ")
    webbrowser.open("share.mp3")
    print(f"{event.user.uniqueId} heeft de stream gedeeld!")
    print(f"Dankjewel {event.user.uniqueId}!!!")
    print("(Shuuuiiii sound)")
    print(f"    ")
    print(f"    ")
    time.sleep(1)


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
            print("(Are you sure about that sound)")
            print("    ")
            time.sleep(3)

        elif event.gift.gift_type > 1 and event.gift.extended_gift.name == "Rose" or event.gift.gift_type == 1 and event.gift.extended_gift.name == "Roos":
            webbrowser.open("Rose.mp3")
            print("    ")
            print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
            print(f"Dankjewel {event.user.uniqueId}!")
            print("(Are you sure about that sound)")
            print("    ")
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

            elif event.gift.gift_type > 1:
                webbrowser.open("EmotionalDamage.mp3")
                print(f"    ")
                print(f"{event.user.uniqueId} heeft \"{event.gift.extended_gift.name}\" gestuurd!")
                print(f"Dankjewel {event.user.uniqueId}!")
                print("(Emotional Damage sound)")
                print(f"    ")
                time.sleep(5)


@client.on("follow")
async def on_like(event: FollowEvent):
    usersTxt = []
    with open('users.txt') as f:
        usersTxt = f.readlines()

    if f"{event.user.uniqueId}" in users:
        print(f"    ")
        print(f"{event.user.uniqueId}, je hebt Renjestoo al eens gevolgd ;)")
        print(f"    ")
        print(f"    ")
        print(f"    ")

    else:
        # user = (f"{event.user.uniqueId})
        with open("users.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(f"{event.user.uniqueId}")
        users.append({event.user.uniqueId})
        webbrowser.open("follow.mp3")
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
        print(f"    ")
        print(f"{event.user.uniqueId}" + " zegt ping")
        print("Ik zeg: pong!")
        print(f"    ")
    elif (f"{event.comment}") == "/script":
        print("Het script is gratis op http://github.com/renatokuipers te vinden.")
    elif (f"{event.comment}") == "/help":
        print(f"    ")
        print("De beschikbare commando's zijn:")
        print("- /script")
        print("- /ping")
        print("- /calc(3*3) of /calc(2+4) of andere sommen")
        print(f"    ")
    elif "/calc" in (f"{event.comment}"):
        if "exec" in (f"{event.comment}") or "exit" in (f"{event.comment}") or "quit" in (f"{event.comment}") or "import" in (f"{event.comment}") or "compile" in (f"{event.comment}"):
            webbrowser.open("nope.mp3")
            print(f"    ")
            print(f"{event.user.uniqueId}" + "-> Nope :)")
            print("nope sound")
            print(f"    ")
        else:
            try:
                evaluate = (evaluate[5:250])
                print(f"    ")
                print(f"{event.user.uniqueId} vraagt \"{event.comment}\:")
                print(eval(evaluate))
                print(f"    ")
            except:
                webbrowser.open("nope.mp3")
                print(f"{event.user.uniqueId}" + "-> Dat commando bestaat niet :)")
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
    print("Het script staat op github.com/renatokuipers")
    print("Dit is een project die ik maak puur uit hobby.")
    print("Chats komen in het scherm te staan.")
    print("Follow, Share of Gift voor soundeffects.")
    print("Typ /help voor commando's")
    try:
        client.run()
    except:
        None, None
