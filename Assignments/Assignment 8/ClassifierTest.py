import NaiveBayesClassifier
from subprocess import check_output

#The code for this comes from test.py
#http://cs532s18.slack.com/files/U8K4TSGJ1/F9Z33U1B6/test.py

c = NaiveBayesClassifier.naivebayes(NaiveBayesClassifier.getwords)
#remove previous db file
check_output(['rm', 'neverett.db'])
c.setdb('neverett.db')
NaiveBayesClassifier.spamTrain(c)

#classify files as spam or not spam
f1 = open('Testing\\email1.txt')
e1 = f1.read()
print(c.classify(e1))
f2 = open('Testing\\email2.txt')
e2 = f2.read()
print(c.classify(e2))
f3 = open('Testing\\email3.txt')
e3 = f3.read()
print(c.classify(e3))
f4 = open('Testing\\email4.txt')
e4 = f4.read()
print(c.classify(e4))
f5 = open('Testing\\email5.txt')
e5 = f5.read()
print(c.classify(e5))
f6 = open('Testing\\email6.txt')
e6 = f6.read()
print(c.classify(e6))
f7 = open('Testing\\email7.txt')
e7 = f7.read()
print(c.classify(e7))
f8 = open('Testing\\email8.txt')
e8 = f8.read()
print(c.classify(e8))
f9 = open('Testing\\email9.txt')
e9 = f9.read()
print(c.classify(e9))
f10 = open('Testing\\email10.txt')
e10 = f10.read()
print(c.classify(e10))
f11 = open('Testing\\email11.txt')
e11 = f11.read()
print(c.classify(e11))
f12 = open('Testing\\email12.txt')
e12 = f12.read()
print(c.classify(e12))
f13 = open('Testing\\email13.txt')
e13 = f13.read()
print(c.classify(e13))
f14 = open('Testing\\email14.txt')
e14 = f14.read()
print(c.classify(e14))
f15 = open('Testing\\email15.txt')
e15 = f15.read()
print(c.classify(e15))
f16 = open('Testing\\email16.txt')
e16 = f16.read()
print(c.classify(e16))
f17 = open('Testing\\email17.txt')
e17 = f17.read()
print(c.classify(e17))
f18 = open('Testing\\email18.txt')
e18 = f18.read()
print(c.classify(e18))
f19 = open('Testing\\email19.txt')
e19 = f19.read()
print(c.classify(e19))
f20 = open('Testing\\email20.txt')
e20 = f20.read()
print(c.classify(e20))