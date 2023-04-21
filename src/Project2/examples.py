import itertools
import strings
import numerics
import misc
import lists
import query
import discretization
import globalVars as d
import Num
import Sym
import Data
import random
import stats
import math




# Examples Added to the CLI
examples_added = {}

# Register an example
def add_example(key, str, fun):
    global examples_added
    '''
    Adds an example that is runnable from the command line and updates the help menu
    '''
    examples_added[key] = fun
    d.help +=  f"  -g  {key}    {str}"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)

# def assert(x):
#   if not x:
#     raise Exception("Failed Assertion")

# The
def eg_function_the():
    return strings.oo(d.the)

# rand
def eg_function_0():
    t=[]
    u=[]

    d.Seed=1
    for i in range(1,1000):
       t.append(numerics.rint(0, 100))

    d.Seed=1
    for i in range(1,1000):
       u.append(numerics.rint(0, 100))

    for k,v in enumerate(t):
       assert(v==u[k], "test")

# some
def eg_function_1():
  d.the["Max"] = 32
  num1 = Num.Num()
  for i in range(1,10000):
    num1.add(i)

  strings.oo(query.has(num1))

def eg_function_2():
  num1,num2 = Num.Num(), Num.Num()
  for i in range(1,10000):
      num1.add(numerics.rand())
  for i in range(1,10000): 
      num2.add(numerics.rand()**2)
  print(1,numerics.rnd(query.mid(num1), 1), numerics.rnd(query.div(num1), 1))
  print(2,numerics.rnd(query.mid(num2), 1), numerics.rnd(query.div(num2), 2))
  t = numerics.rnd(query.mid(num1), 1)
  return .5 == numerics.rnd(query.mid(num1), 1) and query.mid(num1) > query.mid(num2)


def eg_function_3():
  sym=lists.adds(Sym.Sym(), ["a","a","a","a","b","b","c"])
  print (query.mid(sym), numerics.rnd(query.div(sym), 2))
  return 1.38 == numerics.rnd(query.div(sym), 2)

def eg_function_4():
  global n
  n=0
  def fun(t):
      global n
      n += len(t)

  strings.csv(d.the["file"], fun)
  return 3192 == n

def eg_function_5():
  data=Data.Data(d.the["file"])
  col=data.cols.x[0]
  print(col.lo, col.hi, query.mid(col), query.div(col))
  strings.oo(query.stats(data))

def eg_function_6():
  data1=Data.Data(d.the["file"])
  data2=data1.clone(data1.rows)
  strings.oo(query.stats(data1))
  strings.oo(query.stats(data2))

def eg_function_7():
  assert numerics.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]) == False, "1"
  assert numerics.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]) == True, "2"
  t1, t2 = [], []
  for i in range(1000):
      t1.append(numerics.rand())
      t2.append(numerics.rand() ** 0.5)

  assert(numerics.cliffsDelta(t1, t1) == False, "3")
  assert(numerics.cliffsDelta(t1, t2) == True, "4")

  diff, j = False, 1.0
  while not diff:
      t3 = lists.map(t1, lambda x: x * j)
      diff = numerics.cliffsDelta(t1, t3)
      print(">", numerics.rnd(j, 2), diff)
      j *= 1.025

  def fun(x):
      global j
      return x*j

  while not diff:
    t3=lists.map(t1,fun)

def eg_function_8(): 
  data = Data.Data(d.the["file"]) 
  num  = Num.Num() 
  for _,row in data.rows.items(): 
    num.add(data.dist(row, data.rows[0])) 
  strings.oo({"lo":num.lo, 
              "hi":num.hi, 
              "mid":numerics.rnd(query.mid(num), 2), 
              "div":numerics.rnd(query.div(num), 2)}) 

def eg_function_9():
  data = Data.Data(d.the.get("file"))
  left,right,A,B,mid,c, evals = data.half()
  print(len(left),len(right))
  l,r = data.clone(left), data.clone(right)
  print("l",strings.o(query.stats(l)))
  print("r",strings.o(query.stats(r)))

def eg_function_10():
  misc.showTree(Data.Data(d.the["file"]).tree())

def eg_function_11():
  data = Data.Data(d.the["file"])
  best,rest,evals = data.sway()
  print("\nall ", strings.o(query.stats(data)))
  print("    ",   strings.o(query.stats(data,query.div)))
  print("\nbest", strings.o(query.stats(best)))
  print("    ",   strings.o(query.stats(best,query.div)))
  print("\nrest", strings.o(query.stats(rest)))
  print("    ",   strings.o(query.stats(rest,query.div)))
  print("\nall ~= best?", strings.o(numerics.diffs(best.cols.y, data.cols.y)))
  print("best ~= rest?", strings.o(numerics.diffs(best.cols.y, rest.cols.y)))

def eg_function_12():
  print("")
  data = Data.Data(d.the["file"])
  best,rest, evals = data.sway()
  print("all","","","", strings.o({"best":len(best.rows), "rest":len(rest.rows)}))
  print("")
  for k,t in discretization.bins(data.cols.x,{"best":best.rows, "rest":rest.rows}).items():
    for _,range in t.items():
      #if range.txt != b4:
      #      print("")
      #b4 = range.txt
      print(range.txt,range.lo,range.hi,
           numerics.rnd(discretization.value(range.y.has, len(best.rows),len(rest.rows),"best")),
           strings.o(range.y.has))
    print("")

def eg_function_13():
    data=Data.Data(d.the["file"]) 
    best,rest, evals = data.sway() 
    rule,most= data.xpln(best,rest) 
    print("\n-----------\nexplain=", strings.o(rule.showRule())) 
    data1= Data.Data(rule.selects(data.rows), datai = data) 
    print("all               ", strings.o(query.stats(data)), strings.o(query.stats(data, query.div))) 
    print(f"sway1 with {evals} evals", strings.o(query.stats(best)), strings.o(query.stats(best, query.div))) 
    print(f"xpln1 on {evals} evals", strings.o(query.stats(data1)), strings.o(query.stats(data1, query.div))) 
    top,_ = data.betters(len(best.rows)) 
    top = Data.Data(top, data2 = data) 
    print(f"top with {len(data.rows)} evals",strings.o(query.stats(top)), strings.o(query.stats(top,query.div))) 


# ok
def eg_function_14(n=1):
    random.seed(n)

# sample
def eg_function_15(): 
    samples = ["a", "b", "c", "d", "e"]
    for i in range(1, 11):
        print("", ''.join(numerics.samples(samples, len(samples))))

#num
def eg_function_16():
    n=Num.Num(t=[1,2,3,4,5,6,7,8,9,10])
    print("",n.n, n.mu, n.sd)

# Guass
def eg_function_17():
    t=[]
    for i in range(0,10**4): 
        t.append(numerics.gaussian(10,2))
    n=Num.Num(t=t)
    print("",n.n,n.mu,n.sd) 

# bootmu
def eg_function_18():
    a=[]
    for i in range(1,100):
        a.append(numerics.gaussian(10,1))
    
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    for mu in numerics.float_range(10,11,.1):
        b=[]
        for i in range(1,100):
            b.append(numerics.gaussian(mu,1))
        numB = Num.Num(t=b)
        cl=numerics.cliffsDelta(a,b)
        bs=numerics.bootstrap(a,b)
        print("",mu,1,cl,bs,cl and bs)

#bootsd
def eg_function_19():
    a=[]
    for i in range(1,100):
        a.append(numerics.gaussian(10,1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    for sd in range(1,10):
        b=[]
        for i in range(1,100):
           b.append(numerics.gaussian(12,sd))
        cl=numerics.cliffsDelta(a,b)
        bs=numerics.bootstrap(a,b)
        print("",12,sd,cl, bs, cl and bs)

# basic
def eg_function_20():
    print("\t\ttrue",  numerics.bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3}, 
                                    {8, 7, 6, 2, 5, 8, 7, 3}),
                        numerics.cliffsDelta({8, 7, 6, 2, 5, 8, 7, 3}, 
                                    {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse",  numerics.bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3},  
                                    {9, 9, 7, 8, 10, 9, 6}),
                        numerics.cliffsDelta({8, 7, 6, 2, 5, 8, 7, 3},  
                                    {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse",  numerics.bootstrap(  {0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                    {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}),
                        numerics.cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                    {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}))

# pre
def eg_function_21():
    print("\neg3")
    d=1
    for i in range(1,11):
        t1,t2 = [],[]
        for j in range(1,32):
            t1.append(numerics.gaussian(10,1))
            t2.append(numerics.gaussian(d*10,1))
        print("\t",numerics.rnd(d,2), str(d < 1.1), numerics.bootstrap(t1,t2), numerics.bootstrap(t1,t1))
        d += 0.05 

def eg_function_22():
    sk = stats.scottKnot([
            lists.RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
            lists.RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),
            lists.RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),
            lists.RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),
            lists.RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])
    tiles = stats.tiles(sk)
    for rx in tiles:
        print(rx["name"],rx["rank"],rx["show"])

def eg_function_23():
    sk = stats.scottKnot([
            lists.RX([101,100,99,101,99.5,101,100,99,101,99.5],"rx1"),
            lists.RX([101,100,99,101,100,101,100,99,101,100],"rx2"),
            lists.RX([101,100,99.5,101,99,101,100,99.5,101,99],"rx3"),
            lists.RX([101,100,99,101,100,101,100,99,101,100],"rx4")])
    tiles = stats.tiles(sk)
    for rx in tiles:
        print(rx["name"],rx["rank"],rx["show"])

def eg_function_24():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,1000):
        a.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        b.append(numerics.gaussian(10.1,1))
    for i in range(1,1000):
        c.append(numerics.gaussian(20,1))
    for i in range(1,1000):
        d.append(numerics.gaussian(30,1))
    for i in range(1,1000):
        e.append(numerics.gaussian(30.1,1))
    for i in range(1,1000):
        f.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        g.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        h.append(numerics.gaussian(40,1))
    for i in range(1,1000):
        j.append(numerics.gaussian(40,3))
    for i in range(1,1000):
        k.append(numerics.gaussian(10,1))

    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(lists.RX(v,"rx"+str(k)) )

    def fun(a):
        return query.mid(a, mode="tiles")

    lists.sort2(rxs,fun)
    for rx in stats.tiles(rxs):
        print("",rx["name"],rx["show"])

def eg_function_25():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,1000):
        a.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        b.append(numerics.gaussian(10.1,1))
    for i in range(1,1000):
        c.append(numerics.gaussian(20,1))
    for i in range(1,1000):
        d.append(numerics.gaussian(30,1))
    for i in range(1,1000):
        e.append(numerics.gaussian(30.1,1))
    for i in range(1,1000):
        f.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        g.append(numerics.gaussian(10,1))
    for i in range(1,1000):
        h.append(numerics.gaussian(40,1))
    for i in range(1,1000):
        j.append(numerics.gaussian(40,3))
    for i in range(1,1000):
        k.append(numerics.gaussian(10,1))

    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(lists.RX(v,"rx"+str(k))) 
    
    for rx in stats.tiles(stats.scottKnot(rxs)):
        print("",rx["rank"], rx["name"],rx["show"])
    


def compare_dicts(dict1, dict2, data):
    s1, s2, ys, x, y = 0, 0, data.cols.y, None, None

    index = 0
    for n, col in ys.items():
        x = dict1.get(col.txt)
        y = dict2.get(col.txt)
        x = col.norm(x)
        y = col.norm(y)
        s1 = s1 - math.exp(col.w * (x - y) / len(ys))
        s2 = s2 - math.exp(col.w * (y - x) / len(ys))

    return s1 / len(ys) < s2 / len(ys)





def eg_function_26():

    list = [
        
[4, 'zitler', 0.65, 0.5, 100, 1.0, 2.0],
[4, 'zitler', 0.65, 0.5, 600, 1.5, 2.0],
[4, 'zitler', 0.69, 0.5, 600, 3.0, 2.0],
[6, 'zitler', 0.69, 0.5, 1600, 0.5, 4.0],
[8, 'zitler', 0.65, 0.5, 600, 1.0, 2.0],
[2, 'bdom', 0.81, 0.5, 100, 0.5, 6.0],
[6, 'zitler', 0.77, 0.5, 100, 1.0, 5.0],
[4, 'zitler', 0.97, 0.5, 100, 0.5, 2.0],
[6, 'zitler', 0.85, 0.5, 100, 2.5, 5.0],
[4, 'zitler', 0.73, 0.5, 2100, 3.5, 5.0],
[8, 'zitler', 0.65, 0.5, 1600, 1.5, 4.0],
[2, 'zitler', 0.89, 0.5, 600, 4.5, 4.0],
[6, 'zitler', 0.69, 0.5, 1600, 2.5, 2.0],
[2, 'zitler', 0.93, 0.5, 600, 1.5, 6.0],
[10, 'zitler', 0.73, 0.5, 1100, 2.0, 6.0],
[6, 'zitler', 0.89, 0.5, 100, 3.0, 5.0],
[2, 'zitler', 0.73, 0.5, 600, 2.5, 5.0],
[10, 'zitler', 0.97, 0.5, 1100, 1.5, 2.0],
[6, 'zitler', 0.97, 0.5, 1600, 1.5, 2.0],
[14, 'zitler', 0.77, 0.5, 2100, 1.0, 5.0],
[8, 'zitler', 0.89, 0.5, 1600, 0.5, 3.0],
[8, 'zitler', 0.93, 0.5, 100, 0.5, 4.0],
[6, 'zitler', 0.97, 0.5, 100, 2.0, 3.0],
[10, 'zitler', 0.85, 0.5, 2100, 1.0, 5.0],
[8, 'zitler', 0.89, 0.5, 1100, 1.5, 3.0],
[4, 'zitler', 0.81, 0.5, 2600, 3.5, 3.0],
[2, 'zitler', 0.97, 0.5, 2600, 3.5, 2.0],
[8, 'zitler', 0.73, 0.5, 2600, 2.5, 4.0],
[2, 'zitler', 0.77, 0.5, 2100, 0.5, 3.0],
[4, 'zitler', 0.97, 0.5, 1600, 2.5, 5.0],
[4, 'zitler', 0.85, 0.5, 1100, 2.0, 3.0],
[6, 'zitler', 0.81, 0.5, 1600, 0.5, 6.0],
[4, 'zitler', 0.93, 0.5, 2600, 1.5, 5.0],
[14, 'bdom', 0.65, 0.5, 100, 2.5, 3.0],
[10, 'bdom', 0.69, 0.5, 600, 2.0, 4.0],
[8, 'bdom', 0.89, 0.5, 100, 1.5, 2.0],
[6, 'bdom', 0.73, 0.5, 100, 3.5, 4.0],
[12, 'zitler', 0.69, 0.5, 600, 1.5, 4.0],
[14, 'zitler', 0.65, 0.5, 600, 2.0, 3.0],
[14, 'zitler', 0.77, 0.5, 1100, 1.0, 3.0],
[14, 'zitler', 0.65, 0.5, 600, 2.5, 2.0],
[2, 'bdom', 0.69, 0.5, 1100, 2.0, 5.0],
[4, 'bdom', 0.65, 0.5, 1600, 1.5, 3.0],
[2, 'bdom', 0.77, 0.5, 100, 1.0, 5.0],
[2, 'bdom', 0.65, 0.5, 1100, 2.0, 3.0],
[12, 'bdom', 0.69, 0.5, 100, 1.0, 6.0],
[8, 'bdom', 0.69, 0.5, 100, 1.0, 4.0],
[6, 'bdom', 0.93, 0.5, 100, 0.5, 4.0],
[6, 'bdom', 0.77, 0.5, 1100, 1.5, 4.0],
[6, 'zitler', 0.89, 0.5, 1100, 4.5, 3.0],
[6, 'zitler', 0.85, 0.5, 1100, 3.5, 2.0],
[6, 'zitler', 0.77, 0.5, 2600, 4.5, 2.0],
[8, 'zitler', 0.77, 0.5, 1600, 3.5, 3.0],
[12, 'zitler', 0.89, 0.5, 100, 2.0, 3.0],
[10, 'zitler', 0.93, 0.5, 100, 3.0, 4.0],
[8, 'zitler', 0.77, 0.5, 100, 3.5, 2.0],
[12, 'zitler', 0.85, 0.5, 1100, 1.5, 2.0],
[2, 'bdom', 0.77, 0.5, 1100, 2.0, 3.0],
[4, 'bdom', 0.89, 0.5, 1600, 1.0, 2.0],
[6, 'zitler', 0.65, 0.5, 2100, 3.0, 2.0],
[4, 'bdom', 0.93, 0.5, 100, 3.0, 2.0],
[14, 'zitler', 0.77, 0.5, 1100, 2.0, 4.0],
[8, 'zitler', 0.73, 0.5, 100, 3.5, 5.0],
[12, 'zitler', 0.65, 0.5, 2100, 3.5, 4.0],
[8, 'zitler', 0.69, 0.5, 1600, 3.0, 3.0],
[14, 'bdom', 0.97, 0.5, 1600, 4.5, 6.0],
[10, 'bdom', 0.93, 0.5, 2600, 3.0, 6.0],
[6, 'bdom', 0.93, 0.5, 2600, 4.5, 4.0],
[12, 'bdom', 0.89, 0.5, 1600, 4.0, 4.0],
[14, 'bdom', 0.77, 0.5, 2100, 4.5, 6.0],
[12, 'bdom', 0.69, 0.5, 2100, 1.0, 6.0],
[8, 'bdom', 0.81, 0.5, 600, 4.0, 6.0],
[12, 'bdom', 0.81, 0.5, 1600, 4.0, 4.0],
[2, 'zitler', 0.93, 0.5, 2600, 2.5, 6.0],
[8, 'zitler', 0.97, 0.5, 2600, 4.0, 3.0],
[4, 'bdom', 0.97, 0.5, 2600, 1.0, 6.0],
[6, 'zitler', 0.89, 0.5, 2100, 4.5, 6.0],
[14, 'zitler', 0.73, 0.5, 2100, 3.0, 6.0],
[10, 'zitler', 0.77, 0.5, 2100, 4.0, 6.0],
[10, 'zitler', 0.93, 0.5, 2100, 4.0, 4.0],
[12, 'zitler', 0.81, 0.5, 2100, 3.0, 5.0],
[10, 'bdom', 0.97, 0.5, 600, 4.0, 3.0],
[12, 'bdom', 0.89, 0.5, 100, 2.5, 5.0],
[8, 'bdom', 0.97, 0.5, 2100, 2.0, 4.0],
[14, 'bdom', 0.93, 0.5, 1100, 3.5, 4.0],
[14, 'bdom', 0.65, 0.5, 1600, 1.5, 6.0],
[14, 'bdom', 0.97, 0.5, 2100, 0.5, 4.0],
[12, 'bdom', 0.85, 0.5, 600, 2.5, 5.0],
[14, 'bdom', 0.77, 0.5, 100, 1.5, 6.0],
[14, 'zitler', 0.81, 0.5, 600, 4.5, 4.0],
[8, 'zitler', 0.97, 0.5, 1600, 3.0, 4.0],
[14, 'zitler', 0.93, 0.5, 2600, 1.0, 4.0],
[10, 'zitler', 0.89, 0.5, 1600, 3.0, 4.0],
[10, 'bdom', 0.85, 0.5, 100, 4.0, 6.0],
[6, 'bdom', 0.85, 0.5, 600, 4.5, 5.0],
[4, 'bdom', 0.97, 0.5, 1600, 1.5, 6.0],
[14, 'zitler', 0.81, 0.5, 2100, 1.5, 5.0],
[4, 'bdom', 0.69, 0.5, 1600, 4.5, 3.0],
[2, 'bdom', 0.85, 0.5, 1600, 3.5, 3.0],
[10, 'bdom', 0.69, 0.5, 2600, 2.0, 4.0],
[14, 'bdom', 0.73, 0.5, 2600, 3.5, 2.0],
[4, 'bdom', 0.65, 0.5, 1100, 3.5, 5.0],
[4, 'bdom', 0.77, 0.5, 1100, 4.0, 4.0],
[10, 'bdom', 0.81, 0.5, 2600, 4.0, 4.0],
[6, 'bdom', 0.69, 0.5, 2100, 2.5, 4.0],
[6, 'bdom', 0.77, 0.5, 2600, 0.5, 6.0],
[2, 'bdom', 0.93, 0.5, 2100, 3.5, 4.0],
[14, 'zitler', 0.69, 0.5, 2600, 4.0, 2.0],
[2, 'zitler', 0.93, 0.5, 2600, 4.5, 2.0],
[4, 'bdom', 0.77, 0.5, 100, 4.0, 5.0],
[4, 'bdom', 0.77, 0.5, 1600, 2.0, 6.0],
[6, 'bdom', 0.77, 0.5, 1600, 2.5, 4.0],
[2, 'bdom', 0.73, 0.5, 2600, 2.0, 5.0],
[14, 'bdom', 0.85, 0.5, 2600, 1.0, 2.0],
[12, 'bdom', 0.81, 0.5, 600, 3.5, 2.0],
[6, 'bdom', 0.93, 0.5, 2100, 1.0, 3.0],
[8, 'bdom', 0.89, 0.5, 1100, 1.5, 3.0],
[2, 'bdom', 0.97, 0.5, 100, 3.0, 4.0],
[10, 'bdom', 0.89, 0.5, 1100, 4.0, 2.0],
[2, 'bdom', 0.93, 0.5, 1600, 1.0, 5.0],
[4, 'bdom', 0.89, 0.5, 1100, 3.0, 3.0],
[14, 'bdom', 0.69, 0.5, 2600, 1.5, 3.0],
[12, 'zitler', 0.81, 0.5, 1600, 4.5, 2.0],
[14, 'bdom', 0.69, 0.5, 2100, 3.5, 4.0],
[12, 'bdom', 0.81, 0.5, 2600, 0.5, 3.0],
[2, 'bdom', 0.89, 0.5, 600, 2.5, 6.0],
[12, 'bdom', 0.65, 0.5, 1100, 3.0, 5.0],
[6, 'bdom', 0.85, 0.5, 1600, 2.5, 4.0],
[12, 'bdom', 0.77, 0.5, 1600, 3.0, 4.0],

    ]

    #baseline_params = [9, 'zitler', 0.95, 0.5, 512, 2, 4 ]
    baseline_params = [16, 'zitler', 0.95, 0.5, 512, 2, 4 ]


    parameter_names = ["bins", "better", "Far", "min", "Max", "p", "rest"]
    formatted_parameter_names = ["Bins", "better", "Far", "Min", "Max", "P", "Rest"] 

    bestStuff = {}
    swayCache = {}

    results = {
        "all": {},
        "sway1": {},
        "xpln1":{},
        "sway2": {},
        "xpln2":{},
        "top":{}
        }
    
    globals_orig = d.the.copy()

    data=Data.Data(d.the["file"]) 
    hp_data = Data.Data(list, col_names=formatted_parameter_names)


    def custom_better(row1, row2):
        best1, rest1, eval1, best2, rest2, eval2 = None, None, None, None, None, None

        cachename1 = tuple(row1.cells)
        cachename2 = tuple(row2.cells)

        if cachename1 in swayCache:
            best1,rest1, eval1 = swayCache[cachename1]
        else:
            #Modify global vars based on hyperparameters
            d.the.update(dict(zip(parameter_names, row1.cells)))
            best1,rest1, eval1 = data.sway()
            swayCache[cachename1] = (best1,rest1, eval1)
        
        if cachename2 in swayCache:
            best2,rest2, eval2 = swayCache[cachename2]
        else:
            #Modify global vars based on hyperparameters
            d.the.update(dict(zip(parameter_names, row2.cells)))
            best2, rest2, eval2 = data.sway()
            swayCache[cachename2] = (best2,rest2, eval2)

        better_hyperparams = compare_dicts(query.stats(best1), query.stats(best2), data)

        bestStuff["bestdataSway"] = best1 if better_hyperparams else best2
        bestStuff["restdataSway"] = rest1 if better_hyperparams else rest2
        bestStuff["evaldataSway"] = eval1 if better_hyperparams else eval2

        #Reset global vars based on hyperparameters
        d.the.update(globals_orig)
        return better_hyperparams

    hp_data.better = custom_better
    best_hp, rest_hp, evals_hp = hp_data.sway()

    cachename = tuple([row.cells for row in best_hp.rows.values() if tuple(row.cells) in swayCache][0])

    print("Calculate Ours")
    print("Hyperparameters: ", dict(zip(parameter_names, cachename)))
    best_ours, rest_ours, evals_ours = swayCache[cachename]
    rule_ours, most_ours = data.xpln(best_ours, rest_ours)
    data_ours = Data.Data(rule_ours.selects(data.rows), datai = data) 

    #Use baseline model config
    print("Calculate Baseline")
    print("Hyperparameters: ", dict(zip(parameter_names, baseline_params)))
    d.the.update(dict(zip(parameter_names, baseline_params)))
    best_baseline, rest_baseline, evals_baseline = data.sway()
    rule_baseline, most_baseline = data.xpln(best_baseline, rest_baseline)
    data_baseline = Data.Data(rule_baseline.selects(data.rows), datai = data) 

    top,_ = data.betters(len(best_baseline.rows)) 
    top = Data.Data(top, data2 = data) 

    results["all"]["data"] = data
    results["all"]["mid"] = query.stats(data)
    results["all"]["div"] = query.stats(data, query.div)
    results["all"]["evals"] = 0

    results["sway1"]["data"] = best_baseline
    results["sway1"]["mid"] = query.stats(best_baseline)
    results["sway1"]["div"] = query.stats(best_baseline, query.div)
    results["sway1"]["evals"] = evals_baseline

    results["xpln1"]["data"] = data_baseline
    results["xpln1"]["mid"] = query.stats(data_baseline)
    results["xpln1"]["div"] = query.stats(data_baseline, query.div)
    results["xpln1"]["evals"] = evals_baseline

    results["sway2"]["data"] = best_ours
    results["sway2"]["mid"] = query.stats(best_ours)
    results["sway2"]["div"] = query.stats(best_ours, query.div)
    results["sway2"]["evals"] = evals_hp * evals_ours

    results["xpln2"]["data"] = data_ours
    results["xpln2"]["mid"] = query.stats(data_ours)
    results["xpln2"]["div"] = query.stats(data_ours, query.div)
    results["xpln2"]["evals"] = evals_hp * evals_ours

    results["top"]["data"] = top
    results["top"]["mid"] = query.stats(top)
    results["top"]["div"] = query.stats(top, query.div)
    results["top"]["evals"] = len(data.rows)


    print("\nMid")
    print(", \t".join(["Method", *[i.txt for i in data.cols.y.values()]]))
    for name, result_group in results.items():
        vals = [str(i) for i in result_group["mid"].values()][:-1]
        print(", \t".join([name, *vals]))

    print("\nDiv")
    print(", \t".join(["Method", *[i.txt for i in data.cols.y.values()]]))
    for name, result_group in results.items():
        vals = [str(i) for i in result_group["div"].values()][:-1]
        print(", \t".join([name, *vals]))


    print("\nEvals")
    print("Method, \t Count")
    for name, result_group in results.items():
        print(", \t".join([name, str(result_group["evals"])]))


    print("------------------")
    print("Equals")
    print("------------------")

    print(", \t".join(["Method", *[i.txt for i in data.cols.y.values()]]))
    for name1, name2 in itertools.combinations(results, 2):
        ret = {}
        for n,i in data.cols.y.items():
            list1 = [r.cells[i.at] for n2,r in results[name1]["data"].rows.items()]
            list2 =  [r.cells[i.at] for n2,r in results[name2]["data"].rows.items()]
            ret[i.txt] =  " = " if numerics.cliffsDelta(list1,list2) or numerics.bootstrap(list1,list2) else " ! "
        vals = [str(i) for i in ret.values()]
        print(", \t".join([name1+" to "+name2, *vals]))
  
    


def add_all_examples():
    add_example("hpo", "Find Most accurate hyper parameter set", eg_function_26)
    # add_example("xpln", "explore explanation sets", eg_function_13)
    # add_example("xpln2", "Try to Do Better", eg_function_26)
    # add_example("the", "show settings", eg_function_the)
    # add_example("rand", "demo random number generation", eg_function_0)
    # add_example("some", "demo of reservoir sampling", eg_function_1)
    # add_example("nums", "demo of NUM", eg_function_2)
    # add_example("syms", "demo SYMS", eg_function_3)
    # add_example("csv", "reading csv files", eg_function_4)
    # add_example("data",  "showing data sets", eg_function_5)
    # add_example("clone", "replicate structure of a DATA", eg_function_6)
    ##add_example("cliffs", "stats tests", eg_function_7)
    # add_example("dist", "distance test", eg_function_8)
    # add_example("half", "divide data in half", eg_function_9)
    # add_example("tree", "make and show tree of clusters", eg_function_10)
    # add_example("sway", "optimizing", eg_function_11)
    # add_example("bins",  "find deltas between best and rest", eg_function_12)
    

    # add_example("ok", "", eg_function_14)
    # add_example("sample", "", eg_function_15)
    # add_example("num", "", eg_function_16)
    # add_example("gauss", "", eg_function_17)
    # add_example("bootmu", "", eg_function_18)
    # add_example("bootsd", "", eg_function_19)
    # add_example("basic", "", eg_function_20)
    # add_example("pre", "", eg_function_21)
    # add_example("tiles", "", eg_function_24)
    # add_example("five", "", eg_function_22)
    # add_example("six", "", eg_function_23)
    # add_example("sk", "", eg_function_25)