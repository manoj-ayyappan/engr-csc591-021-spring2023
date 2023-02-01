import strings
import numerics
import misc
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


## Not Used
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


def eg_function_7():
    data1=Data.Data(d.the.get("file"))
    data2=data1.clone(data1.rows)
    return len(data1.rows) == len(data2.rows) and \
        data1.cols.y[0].w == data2.cols.y[0].w and \
        data1.cols.x[0].at == data2.cols.x[0].at and  \
        len(data1.cols.x) == len(data2.cols.x)

def eg_function_8():
    data=Data.Data(d.the.get("file"))
    print(0,0,strings.o(data.rows[0].cells))
    for n,t in data.around(data.rows[0]).items():
        if (n+1) % 50 == 0:
           print(n+1, numerics.rnd(t.get("dist"),2) , strings.o(t.get("row").cells))

def eg_function_9():
    data=Data.Data(d.the.get("file"))
    left,right,A,B,mid,c = data.half() 
    print(len(left),len(right),len(data.rows))
    print(strings.o(A.cells),c)
    print(strings.o(mid.cells)) 
    print(strings.o(B.cells))

def eg_function_10():
    data=Data.Data(d.the.get("file"))
    misc.show(data.cluster(),"mid",data.cols.y,1)

def eg_function_11():
    data=Data.Data(d.the.get("file"))
    misc.show(data.sway(),"mid",data.cols.y,1)

def eg_function_12():
    data1=Data.Data(d.the.get("file"))
    data2 = data1.clone(data1.rows)
    # print(str(data2.rows[0].cells))

def add_all_examples():
    add_example("myOwnTest", "MyOwnTest", eg_function_12 )
    add_example("the", "show settings", eg_function_1)
    add_example("sym","check syms", eg_function_2)
    add_example("num", "check nums", eg_function_3 )
    #add_example("csv", "read from csv", eg_function_4 ) #Not Used
    add_example("data","read DATA csv", eg_function_5 )
    #add_example("stats","stats from DATA", eg_function_6 ) #Not Used
    add_example("clone", "duplicate structure", eg_function_7 )
    add_example("around", "sorting nearest neighbors", eg_function_8 )
    add_example( "half", "1-level bi-clustering", eg_function_9 )
    add_example("cluster", "N-level bi-clustering", eg_function_10 ) 
    add_example("optimize", "semi-supervised optimization", eg_function_11 )