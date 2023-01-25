def push(t, x):
  t.append(x) 
  return x 

def kap(t, fun) # map function `fun`(k,v) over list (skip nil results) 
    u = {}
    for k,v in t.items():
        v, k = fun(k, v)
        if k is None:
            k = len(u) + 1
        u[k] = v
        return u