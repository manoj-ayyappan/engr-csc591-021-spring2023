import re
import traceback
import strings
import sys
import examples
import globalVars

b4={} 
for k, v in list(globals().items()):
    b4[k]=v 
    # cache old names (so later, we can find rogues)

def settings(s, t={}):
    for option in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        # Use capture groups from the regex to get option name and default value
        k, v = option
        t[k] = strings.coerce(v)
    return t

def cli(options): # t; update key,vals in `t` from command-line flags
    for k,v in options.items():
        v = str(v)
        for n,x in enumerate(sys.argv):
            if x=="-" + (k[:1]) or x=="--" + k:
                v = v=="False" and "True" or v=="True" and "False" or sys.argv[n+1]
        options[k] = strings.coerce(v) 
    return options 


def make_attempt(funs, what, options):
    if options["debug"] == True:
        passed = funs[what]()
    else:
        try:
            passed = funs[what]()
        except Exception as e:
            print(f"Error in example '{what}': {e}")
            print(traceback.format_exc())
            passed = False
        
    if passed is False:
        print("❌ fail:\t",what)
    else:
        print("✅ pass:\t",what)
        passed = True
    return passed

# `main` fills in the settings, updates them from the command line, runs
# the start up actions (and before each run, it resets the random number seed and settings);
# and, finally, returns the number of test crashed to the operating system.
def main(options,help,funs):  # nil; main program
    global Seed
    saved={}
    passed = 0
    failed = 0
    for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k]=v
    if options.get("help") == "true":
        print(help) 
    else:
        for what in funs.keys(): 
            if options.get("go") == "all" or what==options.get("go"):
                for k,v in saved.items(): 
                    options[k]=v 
                Seed = options.get("seed") 

                passed_test = make_attempt(funs, what, options)
                
                if passed_test:
                    passed += 1
                else:
                    failed += 1

        for k,v in globals().items(): 
            if k not in b4:
                print(f"#W ?{k} {type(v)}")
        return passed,failed

examples.add_all_examples()


if __name__ == '__main__':
    main(globalVars.the, globalVars.help, examples.examples_added)

# print("------> 1 "+ str(examples.eg_function_1()))
# print("------> 2 "+ str(examples.eg_function_2()))
# print("------> 3 "+ str(examples.eg_function_3()))
# print("------> 4 "+ str(examples.eg_function_4()))
