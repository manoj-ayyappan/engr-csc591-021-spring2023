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