'''
Purpose: When given a version number, obtain the appropriate minecraft server.jar download link
Note: This script is designed to take inputs from a Dockerfile
'''

import sys
import requests
import subprocess


# Dockerfile ENV variables go here
# Example RUN command: RUN python3 minecraft_version_link_finder.py = 1.17 = 2:
#Note the = at indexes 1 and 3, that's why sys.argv is for indexes 2 and 4
userInputVersion = str(sys.argv[1])
userInputRam = str(sys.argv[2])

# This Minecraft URL gives data for each version of Minecraft
r = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")

output = r.json()

url = False
for version in output["versions"]:
    
    if userInputVersion == version["id"]:
        
        # This url tells us where we can download both the client and server jarfiles
        url = version["url"]
        r = requests.get(version["url"])
        output = r.json()

        # This url is the actual server.jar download link
        url = output["downloads"]["server"]["url"]

subprocess.run(["wget", url, "-O", "/server.jar"], check=True)
#subprocess.run(["java", f"-Xms{userInputRam}G", f"-Xmx{userInputRam}G", "-jar", "server.jar", "nogui"], check=True)
