import examples
import re
import strings
import sys
import globalVars

b4={} 
for k, v in list(globals().items()):
    b4[k]=v 

def settings(s, t=None):
    if t is None:
        t = {} 
    for option in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        # Use capture groups from the regex to get option name and default value
        k, v = option
        t[k] = strings.coerce(v)
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
    passed = 0
    failed = 0
    t = {}
    for k,v in cli(settings(help)).items():
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
                    failed += 1
                else: 
                    print("✅ pass:",what)
                    passed += 1
        for k,v in globals().items():
            if k not in b4:
               print(f"#W ?{k} {type(v)}")
        return passed,failed

examples.add_all_examples()


if __name__ == '__main__':
    main(globalVars.the, globalVars.help, examples.examples_added)


#print("------> 1 "+ str(examples.eg_function_1()))
#print("------> 2 "+ str(examples.eg_function_2()))
#print("------> 3 "+ str(examples.eg_function_3()))
#print("------> 4 "+ str(examples.eg_function_4()))
