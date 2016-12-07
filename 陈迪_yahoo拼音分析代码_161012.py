from pandas import Series,DataFrame
import  pandas as pd
import  re
from math import log


##Input original file
##
df01=pd.read_csv('yahoo.txt',sep='@.*?:',engine='python',names=['username','password'])
dfpassword01=df01['password']
dfpassword01.to_csv('yahoopassword.txt',index=False,header=False)

##All to string
##
dfpassword11=pd.read_csv('yahoopassword.txt',engine='python',names=['password'])
#print dfpassword
dfpassword12=dfpassword11.password
#print  dfpassword2
dfpassword13=dfpassword12.str.extract('.*?([a-zA-Z]{2,}).*?')
#print  dfpassword3
dfpassword14=dfpassword13.dropna(axis=0)
dfpassword14.to_csv('yahoopassword_string.txt',index=False,)#header=False)


##String to pinyin
##
words = open("pinyin.txt").read().split()
#print words
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))




##
##s = 'thumbgreenappleactiveassignmentweeklymetaphor'
##s1='youareasillybitch'
##s2='wango'
##s3=infer_spaces(s2).split()
##print  s3
##print(infer_spaces(s2))


dfpassword=pd.read_csv('yahoopassword_string.txt',engine='python',names=['password'],)#nrows=1000)
sepassword=dfpassword.password
#print  sepassword
inpassword=sepassword.to_dict()
#print inpassword
exresult=[]
for i,j in inpassword.items():
    if type(j)!=str:
        j=str(j)
    exresult.append(infer_spaces(j))
#print  exresult



def string_cost(liststring):
    pinyin=[]
    for index,string1 in enumerate(exresult):
        temp1=string1.split()
        sum1=0
        maxinedx=1
        for index2,string2 in enumerate(temp1):
            cost2pinyin=wordcost.get(string2,999)
            sum1+=cost2pinyin
            #print cost2pinyin
        if sum1>100:
            temp1=None
        pinyin.append(temp1)
        #print 'temp1:'
        #print  temp1
        #print  ' '
    #print pinyin
    return pinyin
pinyin=string_cost(exresult)
dfpinyin=DataFrame(pinyin)
#print dfpinyin
dfpassword4=dfpinyin.dropna(axis=0)
dfpassword4.to_csv('yahoopassword_pinyin.txt',index=False,)#header=False)

#Find And Count
#open pinyin wordlist
#words = open("pinyin.txt").read().split()
#total number of pinyin
cnlen=len(words)
countPY=[]
countPY2=[]
for i,j in enumerate(words):
    countPY.append(j)
countPY2=[0 for i in range(411)]
#print countPY
#print 'countPY2'
#print countPY2
#print cnlen  #411
dfpinyin=pd.read_csv('yahoopassword_pinyin.txt',engine='python',names=['password'])#nrows=1000)
dictpy=dfpinyin.password.to_dict()

def countfind(stringn):
    index=countPY.index(stringn)
    #print 'index'
    #print index

    countPY2[index]=countPY2[index]+1
   #print countPY2[index]


#print 'dictpy'
#print dictpy
listpy=dictpy.values()
#print  listpy
for i,j in enumerate(listpy):
    #print j
    res=re.findall(r".([a-zA-Z]+).",j)
    #print res
    #print type(res)
    #print type(j)
    for m,n in enumerate(res):
        countfind(n)
        #print m,n,' '

print 'countPY2'
print  countPY2

file = open('yahoonoutput.txt','w')
for i in range(len(countPY)):
    file.write('%s %s\n\n'%(countPY[i],countPY2[i]))