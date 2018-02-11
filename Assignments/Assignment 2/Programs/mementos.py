import requests
import json
from urllib.parse import urlparse
outFile = open("mementos.json", "w")
with open("timemaps.txt", "r") as inFile:
    for line in inFile:
        uri = urlparse(inFile.readline())
        r = requests.get(uri.geturl())
        print(r.status_code)
        outFile.write(r.text + '\n')
outFile.close()
