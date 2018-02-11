#needs listlinks.txt, from the twt.py program
from urllib.parse import urlparse
outFile = open("timemaps.txt", "w")
with open("listlinks.txt", "r") as inFile:
    for line in inFile:
        uri = urlparse(inFile.readline())
        line = outFile.write("http://memgator.cs.odu.edu/timemap/json/" + uri.geturl())
outFile.close()
#this program creates a new txt file: timemaps.txt
#it rewrites the urls to their memgator equivalents for use with part two of the assignment
