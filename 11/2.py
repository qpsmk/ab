f = open("1.txt",'w')
import random
from statistics import mean
maxout = 100
minout = 0
exitt = maxout + 1

#while(not(exitt in range(minout,maxout))):
for g in range(1250000):
    a = random.randint(0,10000)
    b = list()
    c = a
    nuls = 0
    ones = 0
    i0 = 0
    i1 = 0
    while( c > 8):
        if(c % 2 == 0):
            c  = c // 2
        else:
            c  = 3 * c + 1
        while( len(b) <= c):
            b.append(0)
        b[c]  = 1
    for i in range(len(b)):
        if(b[i] == 0):
            nuls = nuls + 1
            i0 = i0 + i
        elif(b[i] == 1):
            ones = ones + 1
            i1 = i1 + i
    if(ones >= nuls):
       c = i1
    else:
      c  = i0
    
    b = list()
    while( c > 8):
        if(c % 2 == 0):
            c  = c // 2
        else:
            c  = 3 * c + 1
        b.append(c) 
    if(len(b) == 0):
        continue   
    bb = round(mean(b))
    strb = str(bb)
    i = 0
    stri = ""
    for i in range(len(strb)):
        if(strb[i] != '0'):
          stri = stri + strb[i]
    exitt = int(stri)
    #if (exitt in range(minout,maxout)):
    if(1):
        f.write(str(exitt))
        f.write('\n')
f.close()