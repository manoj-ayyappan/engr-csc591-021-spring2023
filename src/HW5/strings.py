import re
import lists
import Num
import Sym
import numerics
import globalVars as g
import Row

def fmt(sControl, *args): 
    # emulate printf
    return sControl.format(...)

def oo(t): # print `t` then return it
    print(o(t))
    return t 

def o(t, isKeys = False): 
  # convert `t` to a string. sort named keys. 
    if type(t) == Num.Num:
        s = ""
        s+= "{:a Num "
        s+= ":at " + str(t.at + 1)
        s+= " :hi " + str(t.hi)
        # s+= ":id " + str(t.id)
        s+= " :lo " + str(t.lo)
        s+= " :m2 " + str(numerics.rnd(t.m2, 3))
        s+= " :mu " + str(numerics.rnd(t.mu, 3))
        s+= " :n " + str(t.n)
        s+= " :txt " + str(t.txt)
        s+= " :w " + str(t.w)
        s += " }"
        return s
    if type(t) == Sym.Sym:
        s = ""
        s+= "{:a Sym "
        s+= ":at " + str(t.at + 1)
        # s+= ":id " + str(t.id)
        s+= " :has " + str(t.has)
        s+= " :most " + str(t.most)
        s+= " :n " + str(t.n)
        s+= " :txt " + str(t.txt)
        s += " }"
        return s
    if type(t) == Row.Row:
        s = ""
        s+= "{:a Row "
        if(type(t.cells) == dict):
            f = list(t.cells.values())
        else:
            f = t.cells
        s+= ":cells " + str(f)
        s += " }"
        return s
    if type(t) != dict:
        return str(t)
    return str(t)

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
    return fun(s.strip())


    return int(s) or float(s) or fun(re.match("^\s*(.-)\s*$", s))

# def csv(sFilename, fun): 
#     # call `fun` on rows (after coercing cell text)
#     with open(sFilename) as src:
#         t = {}
#         i = 0
#         fileInput = src.read()
#         for s in re.split(",|\n", fileInput):
#             if(s != ""):
#                 t[i] = coerce(s)
#                 i += 1
#                 fun(t)

def csv(sFilename, fun): 
    with open(sFilename) as src:
        while True:
            t = {}
            i = 0
            fileInput = src.readline()
            if(fileInput):
                for s in re.split(",", fileInput):
                    if(s != ""):
                        t[i] = coerce(s)
                        i += 1   
                fun(t)
            else:
                break 

# function csv(sFilename,fun,    src,s,t) --> nil; call `fun` on rows (after coercing cell text)
#   src,s,t  = io.input(sFilename)
#   while true do
#     s = io.read()
#     if   s
#     then t={}; for s1 in s:gmatch("([^,]+)") do t[1+#t]=coerce(s1) end; fun(t)
#     else return io.close(src) end end end
