'''
Purpose: When given a version number, obtain the appropriate minecraft server.jar download link
Note: This script is designed to take inputs from a Dockerfile
'''

import sys
import requests
import subprocess


# Dockerfile ENV variables go here
userInputVersion = str(sys.argv[1])
userInputRam = str(sys.argv[2])

# This Minecraft URL gives data for each version of Minecraft
r = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")

output = r.json()

url = False
for version in output["versions"]:
    
    print(f"{version["id"]} = {userInputVersion}: {version['id'] == userInputVersion}")
    
    if userInputVersion == version["id"]:

        raise Exception(f"{version['id']} - {userInputVersion}")
        
        # This url tells us where we can download both the client and server jarfiles
        url = version["url"]
        r = requests.get(version["url"])
        output = r.json()

        # This url is the actual server.jar download link
        url = output["downloads"]["server"]["url"]


subprocess.run(f"wget {url} -O /server.jar", check=True)
subprocess.run(f"java -Xms{userInputRam}G -Xmx{userInputRam}G -jar server.jar nogui", check=True)
