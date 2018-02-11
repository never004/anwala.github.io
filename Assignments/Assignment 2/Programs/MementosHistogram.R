x <- 0 * 1:969
mementos <- c(x,128,2,256,2,2,3,2,1,6,1,2,14,1,2,1,1,4,4,2,3,1,12,6,4,16,3,16,3,1,1,2)
max_num <- max(mementos)
hist(mementos,breaks=max_num,axes=FALSE,ann=FALSE, ylim=c(0,10))
title(main="URIs vs. Number of Mementos", font.main="4")
axis(1, at=16*0:240)
axis(2, at=0:10)
title(xlab="Number of Mementos")
title(ylab="Frequency of Occurrence")
#31 total values