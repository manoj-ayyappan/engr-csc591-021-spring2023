import strings
import numerics
import misc
import lists
import globalVars as d

import Num
import Sym
import Data
import lists



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

def eg_function_0():

 function(     t,u)
  Seed=1; t={}; for i=1,1000 do push(t,rint(100)) end
  Seed=1; u={}; for i=1,1000 do push(u,rint(100)) end
  for k,v in pairs(t) do assert(v==u[k]) end end)

def eg_function_1():

 function(     num1)
  the.Max = 32
  num1 = NUM()
  for i=1,10000 do add(num1,i) end
  oo(has(num1)) end)

def eg_function_2():

 function(     num1,num2)
  num1,num2 = NUM(), NUM()
  for i=1,10000 do add(num1, rand()) end
  for i=1,10000 do add(num2, rand()^2) end
  print(1,rnd(mid(num1)), rnd(div(num1)))
  print(2,rnd(mid(num2)), rnd(div(num2)))
  return .5 == rnd(mid(num1)) and mid(num1)> mid(num2) end)

def eg_function_3():

 function(    sym)
  sym=adds(SYM(), {"a","a","a","a","b","b","c"})
  print (mid(sym), rnd(div(sym)))
  return 1.38 == rnd(div(sym)) end)

def eg_function_4():

 function(     n)
  n=0; csv(the.file, function(t) n=n+#t end)
  return 3192 == n end)

def eg_function_5():

 function(    data,col)
  data=DATA.read(the.file)
  col=data.cols.x[1]
  print(col.lo,col.hi, mid(col),div(col))
  oo(stats(data)) end)

def eg_function_6():

function(    data1,data2)
  data1=DATA.read(the.file)
  data2=DATA.clone(data1,data1.rows)
  oo(stats(data1))
  oo(stats(data2)) end)

def eg_function_7():

 function(   t1,t2,t3)
  assert(false == cliffsDelta( {8,7,6,2,5,8,7,3},{8,7,6,2,5,8,7,3}),"1")
  assert(true  == cliffsDelta( {8,7,6,2,5,8,7,3}, {9,9,7,8,10,9,6}),"2")
  t1,t2={},{}
  for i=1,1000 do push(t1,rand()) end --rand()/10) end
  for i=1,1000 do push(t2,rand()^.5) end --rand()*10) end
  assert(false == cliffsDelta(t1,t1),"3")
  assert(true  == cliffsDelta(t1,t2),"4")
  local diff,j=false,1.0
  while not diff  do
    t3=map(t1,function(x) return x*j end)

def eg_function_8():

 function(    data,num)
  data = DATA.read(the.file)
  num  = NUM()
  for _,row in pairs(data.rows) do
    add(num,dist(data, row, data.rows[1])) end
  oo{lo=num.lo, hi=num.hi, mid=rnd(mid(num)), div=rnd(div(num))} end)

def eg_function_9():

 function(   data,l,r)
  data = DATA.read(the.file)
  local left,right,A,B,c = half(data)
  print(#left,#right)
  l,r = DATA.clone(data,left), DATA.clone(data,right)
  print("l",o(stats(l)))
  print("r",o(stats(r))) end)

def eg_function_10():

 function(   data,l,r)
  showTree(tree(DATA.read(the.file))) end)

def eg_function_11():

 function(    data,best,rest)
  data = DATA.read(the.file)
  best,rest = sway(data)
  print("\nall ", o(stats(data)))
  print("    ",   o(stats(data,div)))
  print("\nbest", o(stats(best)))
  print("    ",   o(stats(best,div)))
  print("\nrest", o(stats(rest)))
  print("    ",   o(stats(rest,div)))
  print("\nall ~= best?", o(diffs(best.cols.y, data.cols.y)))
  print("best ~= rest?", o(diffs(best.cols.y, rest.cols.y))) end)

def eg_function_12():

 function(    data,best,rest, b4)
  data = DATA.read(the.file)
  best,rest = sway(data)
  print("all","","","",o{best=#best.rows, rest=#rest.rows})
  for k,t in pairs(bins(data.cols.x,{best=best.rows, rest=rest.rows})) do
    for _,range in pairs(t) do
      if range.txt ~= b4 then print"" end
      b4 = range.txt
      print(range.txt,range.lo,range.hi,
           rnd(value(range.y.has, #best.rows,#rest.rows,"best")),
           o(range.y.has)) end end end)



def add_all_examples():

        add_example("rand", "demo random number generation", eg_function_0)
        add_example("some", "demo of reservoir sampling", eg_function_1)
        add_example("nums", "demo of NUM", eg_function_2)
        add_example("syms", "demo SYMS", eg_function_3)
        add_example("csv", "reading csv files", eg_function_4)
        add_example("data",  "showing data sets", eg_function_5)
        add_example("clone", "replicate structure of a DATA", eg_function_6)
        add_example("cliffs", "stats tests", eg_function_7)
        add_example("dist", "distance test", eg_function_8)
        add_example("half", "divide data in halg", eg_function_9)
        add_example("tree", "make snd show tree of clusters", eg_function_10)
        add_example("sway", "optimizing", eg_function_11)
        add_example("bins",  "find deltas between best and rest", eg_function_12)