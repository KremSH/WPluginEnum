import requests
import sys
import subprocess
plugins = []
if len(sys.argv) < 3:
    print("usage: python3 pluginEnum.py [URL] [wordlist]")
    sys.exit(2)
url = sys.argv[1]
wordlist = sys.argv[2]
with open (wordlist) as Wlist:
    for word in Wlist:
        fullURL = "http://" + url + "/wp-content/plugins/" + word.strip() + "/"
        response = requests.get(fullURL)
        if response.status_code != 404:
            plugins.append(word.strip())

print("Found plugins and versions:\n --------------------")

for plugin in plugins:
    pluginRead = "http://" + url + "/wp-content/plugins/" + plugin + "/readme.txt"
    response = requests.get(pluginRead) 
    version = response.text.find("Stable tag:")
    index = int(version) + len("Stable tag: ")
    print(plugin + ": " + response.text[index:index+5])
