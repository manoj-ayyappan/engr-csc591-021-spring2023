import math
import re

class SYM:
    def __init__(self):
        i=0 #remove this
    def new(i):
        i.n   = 0
        i.has = {}
        i.most, i.mode = 0, None

    def add(i,x): 
        if x != "?":
            i.n = i.n + 1 
            i.has[x] = 1 + (i.has[x] or 0)
            if i.has[x] > i.most:
                i.most,i.mode = i.has[x], x 

    def mid(i,x):
        return i.mode 

    def div(i,x, fun,e): 
        def fun(p):
            return p*math.log(p,2)
        e=0; 
        for _,n in enumerate(i.has):
            e = e + fun(n/i.n) 
        return -e 

class NUM:
    def __init__(self):
        i=0 #remove this
    def new(i):
        i.n, i.mu, i.m2 = 0, 0, 0
        i.lo, i.hi = math.huge, -math.huge

    def add(i,n): 
        if n != "?":
            i.n  = i.n + 1
            d = n - i.mu
            i.mu = i.mu + d/i.n
            i.m2 = i.m2 + d*(n - i.mu)
            i.lo = math.min(n, i.lo)
            i.hi = math.max(n, i.hi) 

    def mid(i,x):
        return i.mu 
    def div(i,x):  
        return (i.m2 <0 or i.n < 2) and 0 or (i.m2/(i.n-1))^0.5 



Seed=937162211

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi)) 

def rand(lo,hi):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647 

def rnd(n, nPlaces): 
    mult = 10^(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult

# Lists

def map(t, fun,     u):
    u={}; 
    for k,v in enumerate(t):
        v,k=fun(v)
        u[k or (1+len(u))]=v  
    return u 
 
def kap(t, fun,     u): 
    u={}; 
    for k,v in enumerate(t):
        v,k=fun(k,v); u[k or (1+len(u))]=v; end; return u

def sort(t, fun):
    list.sort(t,fun); return t #which sort?

def keys(t): 
    return sort(kap(t, lambda k,_:  k)) 

### Strings
def fmt(sControl,*args):
    return format(sControl,*args)

def oo(t):
    print(o(t)); 
    return t

def o(t,isKeys,     fun):
    if type(t)!="table":
        return str(t)
    fun = lambda k,v: fmt(":%s %s",o(k),o(v)) if not re.search("^_" , str(k)) else False #Should this be false or 0?
    return "{"+ (len(t)>0 and not isKeys and map(t,o) or sort(kap(t,fun))," ")+"}"

def coerce(s,    fun): 
    def fun(s1):
        if s1=="true":
            return True 
        elif s1=="false":
            return False
        return s1 
    return math.tointeger(s) or math.tonumber(s) or fun(re.match("^%s*(.-)%s*$",s)) 



#-------------------------------------------------------------------------------
# Examples
examples_added = {}

# Register an example
def add_example(key, str, fun):
    global examples_added
    '''
    Adds an example that is runnable from the command line and updates the help menu
    '''
    examples_added[key] = fun
    help = help + f"  -g  {key}\t{str}\n"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)


# Add an example that shows settings
def eg_function_1():
    return oo(the)

add_example("the", "show settings", eg_function_1)


#Add an example that deals with 'random' numbers
def eg_function_2():
    global Seed
    num1,num2 = NUM(), NUM()

    Seed=the.seed
    for i in range(1, 10e3):
        num1.add( rand(0,1) )

    Seed=the.seed
    for i in range(1, 10e3):
        num2.add( rand(0,1) )

    m1,m2 = rnd(num1.mid(),10), rnd(num2.mid(),10)
    return m1==m2 and 0.5 == rnd(m1,1)

add_example("rand", "generate, reset, regenerate same", eg_function_2)


#Add an example that deals with symbols
def eg_function_3():
    sym=SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a"==sym.mid() and 1.379 == rnd(sym.div())

add_example("sym","check syms", eg_function_3)


def eg_function_4():
    num=NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div()) 
  
add_example("num", "check nums", eg_function_4 )

main(the, help, examples_added)