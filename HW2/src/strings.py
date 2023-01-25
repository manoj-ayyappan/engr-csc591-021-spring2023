import re
import lists

def fmt(sControl,...): 
    # emulate printf
    return sControl.format(...)

def oo(t): # print `t` then return it
    print(o(t))
    return t 

def o(t, isKeys): 
  # convert `t` to a string. sort named keys. 
    if type(t) != "table" :
        return str(t)
    fun = lambda (k,v): fmt(":\s \s",o(k),o(v)) if not re.search("^_", str(k))
    return "{" + " ".join(lists.map(t,o) if (len(t) > 0 and not isKeys) else lists.sort(lists.kap(t,fun))) + "}"

def coerce(s):  #return int or float or bool or string from `s`
    def fun(s1):
        if s1=="true": 
            return True 
        elif s1=="false":
           return False
        return s1
    return int(s) or float(s) or fun(re.match("^\s*(.-)\s*$", s))

def csv(sFilename, fun): 
    # call `fun` on rows (after coercing cell text)

    with open(sFilename) as src:
        t = {}
        for s in src:
            t.extend([coerce(s1) for s1 in s.strip().split(",")])
            fun(t)