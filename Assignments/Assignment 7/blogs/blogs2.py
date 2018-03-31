#my first attempt screwed up so now I will start this over
inFile = open("url.txt")
outFile = open("url.dat", "w+") # for convenience, same file name, but different file extension
listDel = ['?expref=next-blog'] # we are gonna get rid of this line from the first url.txt file
for line in inFile:
	for word in listDel:
		line = line.replace(word, "")
	outFile.write(line)
inFile.close()
outFile.close()

