#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import re
import math

'''
Note, this code has been modified from the code in the link
https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter6/docclass.py
'''

def getwords(doc):
  splitter=re.compile('\\W*')
  #print(doc)
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  toreturn = dict([(w,1) for w in words])
  return toreturn

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures
    
  def setdb(self,dbfile):
    self.con=sqlite.connect(dbfile)    
    self.con.execute('create table if not exists fc(feature,category,count)')
    self.con.execute('create table if not exists cc(category,count)')


  def incf(self,f,cat):
    count=self.fcount(f,cat)
    if count==0:
      self.con.execute("insert into fc values ('%s','%s',1)" 
                       % (f,cat))
    else:
      self.con.execute(
        "update fc set count=%d where feature='%s' and category='%s'" 
        % (count+1,f,cat)) 
  
  def fcount(self,f,cat):
    res=self.con.execute(
      'select count from fc where feature="%s" and category="%s"'
      %(f,cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def incc(self,cat):
    count=self.catcount(cat)
    if count==0:
      self.con.execute("insert into cc values ('%s',1)" % (cat))
    else:
      self.con.execute("update cc set count=%d where category='%s'" 
                       % (count+1,cat))    

  def catcount(self,cat):
    res=self.con.execute('select count from cc where category="%s"'
                         %(cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def categories(self):
    cur=self.con.execute('select category from cc');
    return [d[0] for d in cur]

  def totalcount(self):
    res=self.con.execute('select sum(count) from cc').fetchone();
    if res==None: return 0
    return res[0]


  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)
    self.con.commit()

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp




class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

def spamTrain(c): #training for spam and not spam
  f1 = open('Training\\notspam1.txt')
  tr1 = f1.read()
  c.train(tr1, 'Not Spam')
  f2 = open('Training\\notspam2.txt')
  tr2 = f2.read()
  c.train(tr2, 'Not Spam')
  f3 = open('Training\\notspam3.txt')
  tr3 = f3.read()
  c.train(tr3, 'Not Spam')
  f4 = open('Training\\notspam4.txt')
  tr4 = f4.read()
  c.train(tr4, 'Not Spam')
  f5 = open('Training\\notspam5.txt')
  tr5 = f5.read()
  c.train(tr5, 'Not Spam')
  f6 = open('Training\\notspam6.txt')
  tr6 = f6.read()
  c.train(tr6, 'Not Spam')
  f7 = open('Training\\notspam7.txt')
  tr7 = f7.read()
  c.train(tr7, 'Not Spam')
  f8 = open('Training\\notspam8.txt')
  tr8 = f8.read()
  c.train(tr8, 'Not Spam')
  f9 = open('Training\\notspam9.txt')
  tr9 = f9.read()
  c.train(tr9, 'Not Spam')
  f10 = open('Training\\notspam10.txt')
  tr10 = f10.read()
  c.train(tr10, 'Not Spam')
  f11 = open('Training\\spam1.txt')
  tr11 = f11.read()
  c.train(tr11, 'Spam')
  f12 = open('Training\\spam2.txt')
  tr12 = f12.read()
  c.train(tr12, 'Spam')
  f13 = open('Training\\spam3.txt')
  tr13 = f13.read()
  c.train(tr13, 'Spam')
  f14 = open('Training\\spam4.txt')
  tr14 = f14.read()
  c.train(tr14, 'Spam')
  f15 = open('Training\\spam5.txt')
  tr15 = f15.read()
  c.train(tr15, 'Spam')
  f16 = open('Training\\spam6.txt')
  tr16 = f16.read()
  c.train(tr16, 'Spam')
  f17 = open('Training\\spam7.txt')
  tr17 = f17.read()
  c.train(tr17, 'Spam')
  f18 = open('Training\\spam8.txt')
  tr18 = f18.read()
  c.train(tr18, 'Spam')
  f19 = open('Training\\spam9.txt')
  tr19 = f19.read()
  c.train(tr19, 'Spam')
  f20 = open('Training\\spam10.txt')
  tr20 = f20.read()
  c.train(tr20, 'Spam')