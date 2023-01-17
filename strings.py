import math, re, lists

def fmt(sControl,*args):
    return format(sControl,*args)

def oo(t):
    print(o(t, None, None)); 
    return t

def o(t,isKeys,     fun):
    if type(t)!="table":
        return str(t)
    fun = lambda k,v: fmt(":%s %s",o(k),o(v)) if not re.search("^_" , str(k)) else False #Should this be false or 0?
    return "{"+ (len(t)>0 and not isKeys and map(t,o) or lists.sort(lists.kap(t,fun))," ")+"}"

def coerce(s,    fun): 
    def fun(s1):
        if s1=="true":
            return True 
        elif s1=="false":
            return False
        return s1 
    return math.tointeger(s) or math.tonumber(s) or fun(re.match("^%s*(.-)%s*$",s)) 


