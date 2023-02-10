import SYM
import NUM
import helpers
import strings
import lists
import globalVars
import os


# Examples Added to the CLI
examples_added = {}

# Register an example
def add_example(key, str, fun):
    global examples_added
    '''
    Adds an example that is runnable from the command line and updates the help menu
    '''
    examples_added[key] = fun
    globalVars.help +=  f"  -g  {key}\t{str}\n"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)

# Add an example that shows settings
def eg_function_1():
    return strings.oo(globalVars.the)

#Add an example that deals with 'random' numbers
def eg_function_2():
    
    num1 = NUM.NUM()
    num2 = NUM.NUM()

    helpers.Seed=globalVars.the.get("seed")
    for i in range(1, int(10e3)):
        num1.add( helpers.rand(0,1) )

    helpers.Seed=globalVars.the.get("seed")
    for i in range(1, int(10e3)):
        num2.add( helpers.rand(0,1) )

    m1,m2 = helpers.rnd(num1.mid(),10), helpers.rnd(num2.mid(),10)
    return m1==m2 and 0.5 == helpers.rnd(m1,1)

#Add an example that deals with symbols
def eg_function_3():
    sym=SYM.SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a"==sym.mid() and 1.379 == helpers.rnd(sym.div())

def eg_function_4():
    num=NUM.NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == helpers.rnd(num.div()) 
  

def add_all_examples():
    add_example("the", "show settings", eg_function_1)
    add_example("rand", "generate, reset, regenerate same", eg_function_2)
    add_example("sym","check syms", eg_function_3)
    add_example("num", "check nums", eg_function_4 )
