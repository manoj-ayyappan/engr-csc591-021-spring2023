import re
import lists

def fmt(sControl, *args): 
    # emulate printf
    return sControl.format(...)

def oo(t): # print `t` then return it
    print(o(t))
    return t 

def o(t, isKeys = False): 
  # convert `t` to a string. sort named keys. 
    if type(t) != "table" :
        return str(t)
    fun = lambda k,v: fmt(":\s \s",o(k),o(v)) if not re.search("^_", str(k)) else None
    return "{" + " ".join(lists.map(t,o) if (len(t) > 0 and not isKeys) else lists.sort(lists.kap(t,fun))) + "}"

def coerce(s):  #return int or float or bool or string from `s`
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


    return int(s) or float(s) or fun(re.match("^\s*(.-)\s*$", s))

def csv(sFilename, fun): 
    # call `fun` on rows (after coercing cell text)
    with open(sFilename) as src:
        t = {}
        i = 0
        fileInput = src.read()
        for s in re.split(",|\n", fileInput):
            if(s != ""):
                t[i] = coerce(s)
                i += 1
                fun(t)

# function csv(sFilename,fun,    src,s,t) --> nil; call `fun` on rows (after coercing cell text)
#   src,s,t  = io.input(sFilename)
#   while true do
#     s = io.read()
#     if   s
#     then t={}; for s1 in s:gmatch("([^,]+)") do t[1+#t]=coerce(s1) end; fun(t)
#     else return io.close(src) end end end
