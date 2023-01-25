def push(t, x):
  t[len(t)] = x
  return x 

def map(t, fun, u={}): # t; map a function `fun`(v) over list (skip nil results) 
    for k,v in t.items():
        v,k=fun(v)
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