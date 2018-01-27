#A2.py
#Program for python
#Uses BeautifulSoup and requests
#Usage: python A2.py <name of URI>
#NOTE: must be a URI

from bs4 import BeautifulSoup
import sys
import urllib.request
import requests
if (len(sys.argv) == 1):
    #1. takes as a command line argument a web page
    print('invalid parameter')
html_page = urllib.request.urlopen(sys.argv[1])
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a'):
    #2. extracts all links the from the page
    #print(link.get('href')) <- this was a testing line earlier
    try:
        r = requests.head(link.get('href'), allow_redirects=True)
        # follow all redirects until 200
        if "application/pdf" in r.headers["content-type"]: 
            print(link.get('href'))
            #3. list all links that result in PDF files
            print(r.headers.get('content-length'))
            #print out bytes for each link
    except:
        #if something wrong happens
        print('An error occurred with getting the links!. Try another URI')
# 4. will test on three URIs
# http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html
# http://www.cs.odu.edu/~anwala
# http://www.desconversa.com.br/
