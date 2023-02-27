import lists
import globalVars as d
import query

import Sym

import math

class RANGE():
    def __init__(self,at,txt,lo=None,hi=None):
        self.at=at
        self.txt=txt
        self.lo=lo
        self.hi=hi or lo
        self.y=Sym.Sym()

def extend(range,n,s):
  range.lo = min(n, range.lo)
  range.hi = max(n, range.hi)
  range.y.add(s)

def bin(col,x):
    if x=="?" or col.isSym:
       return x
    tmp = (col.hi - col.lo)/(d.the["bins"] - 1)
    return 1 if col.hi == col.lo else math.floor(x/tmp + .5)*tmp

def itself(x):
   return x

def bins(cols,rowss):
    out = {}
    for _,col in cols.items():
        ranges = {}
        for y,rows in rowss.items():
            for _,row in rows.items():
                x = row.cells[col.at]
                if x != "?":
                    k = bin(col,x)
                    ranges[k] = ranges[k] if k in ranges else RANGE(col.at,col.txt,x)
                    extend(ranges[k], x, y)
        
        ranges = lists.sort2(lists.map(ranges, itself), lists.lt2("lo"))
        ranges = dict(zip(range(len(ranges)), ranges.values()))
        out[len(out)] = ranges if col.isSym else mergeAny(ranges)
    return out


# Given a sorted list of ranges, try fusing adjacent items
# (stopping when no more fuse-ings can be found). When done,
# make the ranges run from minus to plus infinity
# (with no gaps in between).
# Called by function `bins`.
def mergeAny(ranges0):
    def noGaps(t):
        for j in range( 1,len(t) ):
            t[j].lo = t[j-1].hi
        t[0].lo  = -math.inf
        t[len(t) - 1].hi =  math.inf
        return t 
  
    ranges1,j = {},0
    while j < len(ranges0):
        left = ranges0[j]
        if j < len(ranges0) - 1:
            right = ranges0[j+1]
            y = merge2(left.y, right.y)
            if y:
                j = j+1 # next round, skip over right.
                left.hi, left.y = right.hi, y
        lists.push(ranges1,left)
        j = j+1 

    return noGaps(ranges0) if len(ranges0)==len(ranges1) else mergeAny(ranges1)

# If the whole is as good (or simpler) than the parts,
# then return the 
# combination of 2 `col`s.
# Called by function `mergeMany`.
def merge2(col1,col2):
    new = merge(col1,col2)
    a = query.div(new)
    b = (query.div(col1)*col1.n + query.div(col2)*col2.n)/new.n
    if query.div(new) <= (query.div(col1)*col1.n + query.div(col2)*col2.n)/new.n:
        return new

# Merge two `cols`. Called by function `merge2`.
def merge(col1,col2):
    new = lists.copy(col1)
    if col1.isSym:
        for x,n in col2.has.items():
            new.add(x,n)
    else:
        for _,n in col2.has.items():
            new.add(n)
        new.lo = math.min(col1.lo, col2.lo)
        new.hi = math.max(col1.hi, col2.hi) 
    return new

def value(has,  nB=1,nR=1,sGoal=True):
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
           b = b + n 
        else:
           r = r + n
    b,r = b/(nB+1/math.inf), r/(nR+1/math.inf)
    return b**2/(b+r)
