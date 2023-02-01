import numerics

def push(t, x):
  t[len(t)] = x
  return x 

def map(t, fun): # t; map a function `fun`(v) over list (skip nil results) 
    u = {}
    for k,v in t.items():
        v = fun(v)
        if k is None:
            k = 1+len(u)
        u[k] = v 
    return u

def kap(t, fun): # map function `fun`(k,v) over list (skip nil results) 
    u={}
    for k,v in t.items():
        # print("------>" + str(v.txt))
        v, k = fun(k, v)
        if k is None:
            k = len(u) + 1
        u[k] = v
    return u

def sort(t, fun): # t; return `t`,  sorted by `fun` (default= `<`)
    sort(t, key = fun)
    return t

def keys(t): # ss; return list of table keys, sorted
    return sort(kap(t, lambda k,_: k ))


def lt(x):
    def fun(a, b):
        return a[x] < b[x]
    return fun

def any(t):
    y = numerics.rint(len(t) - 1,0)
    return t[y]

def many(t, n):
    u = []
    for i in range(n):
        u.append(any(t))
    return u
