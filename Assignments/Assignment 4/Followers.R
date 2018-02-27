#read friendcount values
setwd('C:/users/nathaniel/appdata/local/programs/Assignment 4/')
fcount <- read.table("followercount.txt", header=FALSE, sep=",")
attach(fcount)
sortfollowers <- fcount[order(V2),]
sortedfollowers <- c(sort(V2))
plot(sortedfollowers, type='l', axes=FALSE, ann=FALSE)
points(82.5, 194, col="blue", pch=16) #acnwala is blue
points(176.6, mean(V2), col="red", pch=16) #mean is red
points(187.3, sqrt(var(V2)), col="purple", pch=16) #stddev is purple
points(98.5, median(V2), col="orange", pch=16) #median is orange
axis(1, at=20*0:200)
axis(2, at=10000*0:110000)
title(main="Friendship Paradox (Twitter)")
title(xlab="user #")
title(ylab="Follower count")
print(mean(V2))
print(sqrt(var(V2)))
print(median(V2))
detach(fcount)