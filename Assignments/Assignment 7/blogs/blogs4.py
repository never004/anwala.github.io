#!/usr/bin/python
# -*- coding: utf-8 -*-
#my first attempt screwed up so now I will start this over
import sys
import re
import requests
import feedparser
import clusters
from bs4 import BeautifulSoup
from urllib.request import urlopen

def WordCounts(url): # returns title and {} of word counts
	p = feedparser.parse(url) #parsing
	wc = {}
	for entr in p.entries:
		if 'summary' in entr:
			summary = entr.summary
		else:
			summary = entr.description
		words = getWords(entr.title + ' ' + summary) #extraction
		for word in words:
			wc.setdefault(word,0)
			wc[word] += 1

	return(p.feed.title, wc)
def getWords(html): #remove HTML tags
	text = re.compile(r'<[^>]+>').sub('', html)
	words = re.compile(r'[^A-Z^a-z]+').split(text) #split by non-alpha chars
	return [word.lower() for word in words if word != ''] #lowercase

feedcount = {}
word_count = {}
feedList = [line for line in open('feed.dat','r')]
for feedURL in feedList:
	try:
		(title, wc) = WordCounts(feedURL)
		word_count[title] = wc
		for (word, count) in wc.items():
			feedcount.setdefault(word, 0)
			if count > 1:
				feedcount[word] += 1
	except:
		print('ERROR: failed to parse feed %s' % feedURL)
wordList = []
for (w, bc) in feedcount.items():
	frac = float(bc) / len(feedList)
	if frac > 0.1 and frac < 0.5:
		wordList.append(w)
outFile = open('blogdata.txt', 'w')
outFile.write('Blog')
for word in wordList:
	outFile.write('\t%s' % word)
outFile.write('\n')
for (blog, wc) in word_count.items():
	print(blog)
	outFile.write(blog)
	for word in wordList:
		if word in wc:
			outFile.write('\t%d' % wc[word])
		else:
			outFile.write('\t0')
	outFile.write('\n')