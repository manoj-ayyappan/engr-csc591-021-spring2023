import strings
import numerics
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
    d.help +=  f"  -g  {key}\t{str}\n"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)

# Add an example that shows settings
def eg_function_1():
    return strings.oo(d.the)

#Add an example that deals with symbols
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
    global n 
    n = 0
    def fun(t):
        global n
        n += len(t)
    strings.csv(d.the.get("file"), fun )
    return n == 8 * 399

def eg_function_5():
    data = Data.Data(d.the.get("file"))
    return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[0].at == 0 and len(data.cols.x) == 4

def eg_function_6():
    data = Data.Data(d.the.get("file"))
    for k,cols in {"y":data.cols.y, "x":data.cols.x}.items():
        print(k,"\tmid\t", strings.o(data.stats("mid",cols,2 )))
        print("", "\tdiv\t", strings.o(data.stats("div",cols,2)))

def add_all_examples():
    add_example("the", "show settings", eg_function_1)
    add_example("sym","check syms", eg_function_2)
    add_example("num", "check nums", eg_function_3 )
    add_example("csv", "read from csv", eg_function_4 )
    add_example("data","read DATA csv", eg_function_5 )
    add_example("stats","stats from DATA", eg_function_6 )