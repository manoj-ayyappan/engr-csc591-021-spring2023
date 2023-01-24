import math, re, lists

def fmt(sControl,*args):
    return format(sControl,*args)

def oo(t):
    print(o(t)); 
    return t

def o(t):
    return str(t)
    # fun = lambda k,v: fmt(":%s %s",o(k),o(v)) if not re.search("^_" , str(k)) else False #Should this be false or 0?
    # return "{"+ (len(t)>0 and not isKeys and map(t,o) or lists.sort(lists.kap(t,fun(None,None), None))," ", None)+"}"

def coerce(s, fun= None): 
    if fun is None:
        def fun(s1):
            if s1=="true":
                return True 
            elif s1=="false":
                return False
            return s1 
    try:
        return int(s)
    except:
        pass
    try:
        return float(s)
    except:
        pass
    return fun(s.lower().strip())


    



