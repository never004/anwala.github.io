#read friendcount values
setwd('C:/users/nathaniel/appdata/local/programs/Assignment 4/')
fcount <- read.csv("acnwala-friendscount.csv", header=TRUE, sep=",")
attach(fcount)
sortdata <- fcount[order(FRIENDCOUNT),]
sorteddata <- c(sort(FRIENDCOUNT))
plot(sorteddata, type="l", axes=FALSE, ann=FALSE)
points(11, 98, col="blue", pch=16) #acnwala is blue
points(62, mean(FRIENDCOUNT), col="red", pch=16) #mean is red
points(63, sqrt(var(FRIENDCOUNT)), col="purple", pch=16) #stddev is purple
points(48, median(FRIENDCOUNT), col="orange", pch=16) #median is orange
axis(1, at=20*0:100)
axis(2, at=200*0:3000)
title(main="Friendship Paradox (Facebook)")
title(xlab="USER")
title(ylab="FRIENDCOUNT")
print(mean(FRIENDCOUNT))
print(sqrt(var(FRIENDCOUNT)))
print(median(FRIENDCOUNT))
detach(fcount)