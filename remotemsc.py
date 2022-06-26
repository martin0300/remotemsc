import requests
import os

print("Getting msc...")
##gets msc download link
mscurl = requests.get("https://martin0300.github.io/backend/minecraftservercreator.json").json()
##download msc
msc = requests.get(mscurl.get("downloadlink")).text

print("Saving temporary file...")
##save temporary file to load
with open("temp.py", "w") as tempfile:
    tempfile.write(msc)

print("Loading module...")
##load temporary file
import temp

print("Deleting temporary file...")
##delete temporary file
os.remove("temp.py")

print("Starting msc...")
##start msc
temp.init()