import math
import re
'''
Original code can be found here: https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter8/numpredict.py
'''

def cosine(vector1, vector2): #numpredict.py did not come with a cosine function
	'compute the cosine similarity of vector1 to vector2: (vector1 dot vector2)/{||vector1||*||vector2||)'
	sumxx = 0 #define all of these
	sumxy = 0
	sumyy = 0 
	for i in range(0, 958):
		x = vector1[i] #x axis
		y = vector2[i] #y axis
		sumxx += x*x
		sumyy += y*y
		sumxy += x*y
	return sumxy/math.sqrt(sumxx*sumyy)
def getdistances(data,vec1): #copied and modified from numpredict.py
  distancelist=[]
  # Loop over every item in the dataset
  for i in range(len(data)):
    vec2=data[i]
    # Add the distance and the index
    distancelist.append((cosine(vec1,vec2))) #euclidean changed to cosine, no i is necessary here either
  # Sort by distance
  distancelist.sort()
  return distancelist
def knnestimate(data,vec1,k): #copied and modified from numpredict.py
  # Get sorted distances
  dlist=getdistances(data,vec1)
  avg=0.0
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i]
    avg+=dlist[i] # this line also modified
  avg=avg/k
  return avg