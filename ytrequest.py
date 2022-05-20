import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup

music_name = ""
query_string = urllib.parse.urlencode({"search_query": music_name})
formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

inspect = BeautifulSoup(clip.content, "html.parser")
yt_title = inspect.find_all("meta", property="og:title")

for concatMusic1 in yt_title:
    pass

print(concatMusic1['content'])

subprocess.Popen(
"start /b " + "path\\to\\mpv.exe " + clip2 + " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
shell=True)