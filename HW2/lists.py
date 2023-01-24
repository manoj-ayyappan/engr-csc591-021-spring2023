def map(t, fun,     u):
    u={}; 
    for k,v in enumerate(t):
        v,k=fun(v)
        u[k or (1+len(u))]=v  
    return u 
 
def kap(t, fun,     u): 
    u={}; 
    for k,v in enumerate(t):
        v,k=fun(k,v); u[k or (1+len(u))]=v; return u

def sort(t, fun):
    list.sort(t,fun); return t #which sort?

def keys(t): 
    return sort(kap(t, lambda k,_:  k)) 