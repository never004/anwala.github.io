import numpredictA9
import math
import re

file = open('blogdata.txt')
data = []
for line in file:
	line = line.strip()
	data.append([int(x) for x in line.split('\t')])
firstVector = data[0] #http://f-measure.blogspot.com/, line 54
secondVector = data[1] #http://ws-dl.blogspot.com/, line 71
print('http://f-measure.blogspot.com/ results')
result = numpredictA9.knnestimate(data, firstVector, 1)
print('kNN estimate: k = 1: ' + str(result))
result = numpredictA9.knnestimate(data, firstVector, 2)
print('kNN estimate: k = 2: ' + str(result))
result = numpredictA9.knnestimate(data, firstVector, 5)
print('kNN estimate: k = 5: ' + str(result))
result = numpredictA9.knnestimate(data, firstVector, 10)
print('kNN estimate: k = 10: ' + str(result))
result = numpredictA9.knnestimate(data, firstVector, 20)
print('kNN estimate: k = 20: ' + str(result))
print(' ') #now for the second vector
print('http://ws-dl.blogspot.com/ results')
result = numpredictA9.knnestimate(data, secondVector, 1)
print('kNN estimate: k = 1: ' + str(result))
result = numpredictA9.knnestimate(data, secondVector, 2)
print('kNN estimate: k = 2: ' + str(result))
result = numpredictA9.knnestimate(data, secondVector, 5)
print('kNN estimate: k = 5: ' + str(result))
result = numpredictA9.knnestimate(data, secondVector, 10)
print('kNN estimate: k = 10: ' + str(result))
result = numpredictA9.knnestimate(data, secondVector, 20)
print('kNN estimate: k = 20: ' + str(result))
