# Lists

import numerics
import copy as c

def push(t, x):
    # Push `x` to end of list; return `x` 
    t[len(t)] = x
    return x 

def map(t, fun): 
    # map a function `fun`(v) over list (skip nil results) 
    u = {}
    if(type(t) == dict):
        for k,v in t.items():
            v = fun(v)
            if k is None:
                k = 1+len(u)
            u[k] = v 
        return u
    else:
        for k,v in enumerate(t):
            v = fun(v)
            if k is None:
                k = 1+len(u)
            u[k] = v 
        return u

def kap(t, fun): 
    # map function `fun`(k,v) over list (skip nil results) 
    u={}
    for k,v in t.items():
        # print("------>" + str(v.txt))
        v, k = fun(k, v)
        if k is None:
            k = len(u) + 1
        u[k] = v
    return u

def sort(t, fun): 
    # Return `t`,  sorted by `fun` (default= `<`)
    sort(t, key = fun)
    return t

def keys(t): 
    # Return list of table keys, sorted
    return sort(kap(t, lambda k,_: k ))


def lt(x):
    # Return a function that sorts ascending on `x`
    def fun(a, b):
        return a[x] < b[x]
    return fun

def any(t):
    # Returns one items at random
    y = numerics.rint(len(t) - 1,0)
    return t[y]

def many(t, n):
    # Returns some items from `t`
    u = []
    for i in range(n):
        u.append(any(t))
    return u

def last(t):
    if(type(t) == dict):
        return list(t.values())[-1]
    else:
        return t[-1]

# def copy(t, u=None):
#     if type(t) != "dict":
#         return t
#     u = {k: copy(v) for k, v in t.items()}
#     return u

def copy(t):
    if type(t) != dict:
        return t
    u = c.deepcopy(t)
    return u
