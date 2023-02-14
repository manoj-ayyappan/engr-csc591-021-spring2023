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
def eg_function_13():
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
      lists.add(num1, numerics.rand())
  for i in range(1,10000): 
      lists.add(num2, numerics.rand()**2)
  print(1,numerics.rnd(query.mid(num1)), numerics.rnd(query.div(num1)))
  print(2,numerics.rnd(query.mid(num2)), numerics.rnd(query.div(num2)))
  return .5 == numerics.rnd(query.mid(num1)) and numerics.mid(num1) > query.mid(num2)

def eg_function_3():
  sym=lists.adds(Sym.Sym(), {"a","a","a","a","b","b","c"})
  print (query.mid(sym), numerics.rnd(query.div(sym)))
  return 1.38 == numerics.rnd(query.div(sym))

def eg_function_4():
  n=0
  def fun(t):
      n += len(t)

  strings.csv(d.the.file, fun)
  return 3192 == n

def eg_function_5():
  data=Data.Data(d.the.file)
  col=data.cols.x[1]
  print(col.lo,col.hi, query.mid(col), query.div(col))
  strings.oo(data.stats())

def eg_function_6():
  data1=Data.Data(d.the.file)
  data2=data1.clone(data1.rows)
  strings.oo(data1.stats())
  strings.oo(data2.stats())

def eg_function_7():
  assert(False == cliffsDelta( {8,7,6,2,5,8,7,3},{8,7,6,2,5,8,7,3}),"1")
  assert(True  == cliffsDelta( {8,7,6,2,5,8,7,3}, {9,9,7,8,10,9,6}),"2")
  t1,t2={},{}
  for i in range(1,1000):
    lists.push(t1,numerics.rand())
  for i in range(1,1000):
      lists.push(t2,numerics.rand()**.5)
  assert(False == cliffsDelta(t1,t1),"3")
  assert(True  == cliffsDelta(t1,t2),"4")
  diff,j = False,1.0

  def fun(x):
      return x*j

  while not diff:
    t3=lists.map(t1,fun)

def eg_function_8():
  data = Data.Data(d.the.file)
  num  = Num.Num()
  for _,row in enumerate(data.rows):
    num.add(data.dist(row, data.rows[1]))
  strings.oo({"lo":num.lo, 
              "hi":num.hi, 
              "mid":numerics.rnd(query.mid(num)), 
              "div":numerics.rnd(query.div(num))})

def eg_function_9():
  data = Data.Data(d.the.get("file"))
  left,right,A,B,c = data.half()
  print(len(left),len(right))
  l,r = data.clone(left), data.clone(right)
  print("l",strings.o(l.stats()))
  print("r",strings.o(r.stats()))

def eg_function_10():
  showTree(tree(Data.Data(d.the.file)))

def eg_function_11():
  data = Data.Data(d.the["file"])
  best,rest = data.sway()
  print("\nall ", strings.o(data.stats()))
  print("    ",   strings.o(data.stats(query.div)))
  print("\nbest", strings.o(best.stats()))
  print("    ",   strings.o(best.stats(query.div)))
  print("\nrest", strings.o(rest.stats()))
  print("    ",   strings.o(rest.stats(query.div)))
  print("\nall ~= best?", strings.o(numerics.diffs(best.cols.y, data.cols.y)))
  print("best ~= rest?", strings.o(numerics.diffs(best.cols.y, rest.cols.y)))

def eg_function_12():
  data = Data.Data(d.the["file"])
  best,rest = data.sway()
  print("all","","","", strings.o({"best":len(best.rows), "rest":len(rest.rows)}))
  for k,t in discretization.bins(data.cols.x,{"best":best.rows, "rest":rest.rows}).items():
    for _,range in enumerate(t):
      if range.txt != b4:
            print("")
      b4 = range.txt
      print(range.txt,range.lo,range.hi,
           numerics.rnd(value(range.y.has, len(best.rows),len(rest.rows),"best")),
           strings.o(range.y.has))



def add_all_examples():
        add_example("the", "show settings", eg_function_13)
        add_example("rand", "demo random number generation", eg_function_0)
        add_example("some", "demo of reservoir sampling", eg_function_1)
        # add_example("nums", "demo of NUM", eg_function_2)
        # add_example("syms", "demo SYMS", eg_function_3)
        # add_example("csv", "reading csv files", eg_function_4)
        # add_example("data",  "showing data sets", eg_function_5)
        # add_example("clone", "replicate structure of a DATA", eg_function_6)
        # add_example("cliffs", "stats tests", eg_function_7)
        # add_example("dist", "distance test", eg_function_8)
        # add_example("half", "divide data in halg", eg_function_9)
        # add_example("tree", "make snd show tree of clusters", eg_function_10)
        # add_example("sway", "optimizing", eg_function_11)
        # add_example("bins",  "find deltas between best and rest", eg_function_12)