import strings
import numerics
import data

import parser.Num.Num as Num
import parser.Sym.Sym as Sym
import parser.Data.Data as Data



# Examples Added to the CLI
examples_added = {}

# Register an example
def add_example(key, str, fun):
    global examples_added
    '''
    Adds an example that is runnable from the command line and updates the help menu
    '''
    examples_added[key] = fun
    data.help +=  f"  -g  {key}\t{str}\n"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)

# Add an example that shows settings
def eg_function_1():
    return strings.oo(data.the)

#Add an example that deals with symbols
def eg_function_2():
    sym = Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == numerics.rnd(sym.div())

def eg_function_3():
    num = Num()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == numerics.rnd(num.div()) 

def eg_function_4():
    n=0
    csv(the.file, lambda (t): n += len(t))
    return n == 8 * 399

def eg_function_5():
    data = Data(the.file)
    return len(data.rows) == 398 and
         data.cols.y[1].w == -1 and
         data.cols.x[1].at == 1 and 
         len(data.cols.x) == 4

def eg_function_6():
    data = Data(the.file)
    for k,cols in {y=data.cols.y,x=data.cols.x}.items():
        print(k,"mid", strings.o(data.stats("mid",cols,2 )))
        print("", "div", strings.o(data.stats("div",cols,2)))

def add_all_examples():
    add_example("the", "show settings", eg_function_1)
    add_example("sym","check syms", eg_function_2)
    add_example("num", "check nums", eg_function_3 )
    add_example("csv", "read from csv", eg_function_4 )
    add_example("data","read DATA csv", eg_function_5 )
    add_example("stats","stats from DATA", eg_function_6 )