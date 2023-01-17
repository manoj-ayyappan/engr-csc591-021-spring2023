import math 
class SYM:
    def __init__(self):
        i=0 #remove this
    def new(i):
        i.n   = 0
        i.has = {}
        i.most, i.mode = 0, None

    def add(i,x): 
        if x != "?":
            i.n = i.n + 1 
            i.has[x] = 1 + (i.has[x] or 0)
            if i.has[x] > i.most:
                i.most,i.mode = i.has[x], x 

    def mid(i,x):
        return i.mode 

    def div(i,x, fun,e): 
        def fun(p):
            return p*math.log(p,2)
        e=0; 
        for _,n in enumerate(i.has):
            e = e + fun(n/i.n) 
        return -e 
