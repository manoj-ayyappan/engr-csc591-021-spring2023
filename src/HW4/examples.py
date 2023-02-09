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
    return strings.oo(d.the)

def eg_function_1():
    t1={"a":1,"b":{"c":2,"d":[3]}}
    t2=lists.copy(t1)
    t2["b"]["d"][0]=10000
    print("b4",strings.o(t1),"\nafter",strings.o(t2))

def eg_function_2():
    sym = Sym.Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == numerics.rnd(sym.div())

def eg_function_3():
    num = Num.Num()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == numerics.rnd(num.div()) 

def eg_function_4():
  t = misc.repCols( misc.dofile(d.the.get("file")).get("cols") )
  lists.map(t.cols.all,strings.oo)
  lists.map(t.rows,strings.oo)


def eg_function_5():
  cols = misc.dofile(d.the.get("file")).get("cols")
  x = misc.repCols(cols)
  misc.show(misc.repCols(cols).cluster(), 3)


def eg_function_6():
  t = misc.dofile(d.the.get("file"))
  rows = misc.repRows(t, misc.transpose(t.get("cols")))
  lists.map(rows.cols.all, strings.oo)
  lists.map(rows.rows, strings.oo)


def eg_function_7():
  t= misc.dofile(d.the.get("file"))
  rows = misc.repRows(t, misc.transpose(t.get("cols")))
  misc.show(rows.cluster(), 3)


def eg_function_8():
  t=misc.dofile(d.the.get("file"))
  rows = misc.repRows(t, misc.transpose(t.get("cols")))
  rows.cluster()
  misc.repPlace(rows)

def eg_function_9():
  misc.repgrid(d.the.get("file")) 



def add_all_examples():
        add_example("the", "show settings", eg_function_0)
        add_example("copy", "check copy", eg_function_1)
        add_example("sym", "check syms", eg_function_2)
        add_example("num",  "check nums", eg_function_3)
        add_example("repcols", "checking repcols", eg_function_4)
        add_example("synonyms", "checking repcols cluster", eg_function_5)
        add_example("reprows", "checking reprows", eg_function_6)
        add_example("prototypes", "checking reprows cluster", eg_function_7)
        add_example("position", "where's wally", eg_function_8)
        add_example("every", "the whole enchilada", eg_function_9)