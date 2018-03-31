#my first attempt screwed up so now I will start this over
with open('url.dat', 'r') as inString:
	with open('feed.dat', 'w') as outString:
		for line in inString:
			line = line.rstrip('\n') + 'feeds/posts/default' #adding feeds/posts/default at the end of these blogs
			print(line, file=outString)