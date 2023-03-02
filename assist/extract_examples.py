#extracts examples from the lua file and prints out layout code 

#What it should end up as:
#def eg_function_12():
#   ...
#def add_all_examples():
#    add_example("myOwnTest", "MyOwnTest", eg_function_12 )

import os
import sys

sys.path.append(os.path.dirname(__file__))

import re
import glob


necessary_text = """
# Examples Added to the CLI
examples_added = {}

# Register an example
def add_example(key, str, fun):
    global examples_added
    '''
    Adds an example that is runnable from the command line and updates the help menu
    '''
    examples_added[key] = fun
    d.help +=  f"  -g  {key}\\t{str}\\n"

# How to use? First define a function, then add to the examples.
# def eg_function_0:
#   return the.some.missing.nested.field
# eg("crash","show crashing behavior", eg_function_1)
"""

lua_files = glob.glob('assist/*.lua')


def create_output(examples):
    i = 0
    print(necessary_text)
    for example in examples:
        name, description, code = example
        #Create a function def
        print(f"def eg_function_{i}():\n")
        print(code)
        i += 1

    print("\n\ndef add_all_examples():\n")
    i = 0
    for example in examples:
        name, description, code = example
        print(f"\tadd_example({name}, {description}, eg_function_{i})")
        i += 1

#if True:
    #filename = "C:\\Users\\rupin\\source\\repos\\engr-csc591-021-spring2023\\HW4\\src\\assist\\grid.lua"
for filename in lua_files:
    with open(filename, "r", encoding="utf8") as f:
        s = f.read()
    
    print(filename)
    examples = []
    i = 0
    for option in re.findall("go\(([^\,]+),([^\,]+),((.|\n)*?end\s*\)\n)", s):
        # Use capture groups from the regex to get option name and default value
        name, description, code, useless = option
        if i != 0:
            examples.append((name, description, code))
        i += 1
    create_output(examples)