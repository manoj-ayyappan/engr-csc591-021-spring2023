import examples
import re
import strings
import sys
import os
import globalVariables

b4={} 
for k, v in list(globals().items()):
    b4[k]=v 

def settings(s, t=None):
    if t is None:
        t = {} 
    matches = re.finditer(r'\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', s)
    for m in matches:
        k = m.group(1)
        v = m.group(2)
        t[k] = strings.coerce(v, None)
    return t

def cli(options):
    for k,v in options.items():
        v = str(v)
        for n in range(len(sys.argv)):
            if sys.argv[n]=="-" + (k[:1]) or sys.argv[n]=="--"+ k:
                v = v=="false" and "true" or v=="true" and "false" or sys.argv[n+1]
    options[k] = strings.coerce(v)
    return options

def main(options, help, funs=None, k=None, saved={}, fails=0):
    global Seed
    t = {}
    for k,v in cli(settings(globalVariables.help)).items():
        options[k] = v
        saved[k] = v
  
    if options.get("help"):
        print(help) 
    else: 
        for what, fun in funs.items():
            if options.get("go") == "all" or what == options.get("go"):
                for k, v in saved.items():
                    options[k] = v
                Seed = options.get("seed")
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:",what) 
                else: 
                    print("✅ pass:",what)
        for k,v in globals().items():
            if k not in b4:
               print(f"#W ?{k} {type(v)}")
        # os._exit(fails) 

os.system('python3 ./examples.py')
main(globalVariables.the, globalVariables.help, examples.examples_added)
# print("------> 1 "+ str(examples.eg_function_1()))
# print("------> 2 "+ str(examples.eg_function_2()))
# print("------> 3 "+ str(examples.eg_function_3()))
# print("------> 4 "+ str(examples.eg_function_4()))



