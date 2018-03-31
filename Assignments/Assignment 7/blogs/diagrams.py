import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
cl = clusters.hcluster(data)
clusters.printclust(cl,labels=blognames) #ascii diagram
clusters.drawdendrogram(cl,blognames,jpeg='blogcluster.jpg') #drawing the dendrogram
