import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
coordinates=clusters.scaledown(data)
clusters.draw2d(coordinates,blognames,jpeg='blogs2d.jpg') # for mds
