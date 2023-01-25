import re
import strings
import sys

global the
global help

the,help = {},""" 
data.lua : an example csv reader script
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   data.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ../etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
"""
b4={}
for k,v in globals().items():
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
        if x=="-" + (k.sub(1,1)) or x=="--" + k:
            v = v=="false" and "true" or v=="true" and "false" or sys.argv[n+1]
    options[k] = strings.coerce(v) 
    return options 


# `main` fills in the settings, updates them from the command line, runs
# the start up actions (and before each run, it resets the random number seed and settings);
# and, finally, returns the number of test crashed to the operating system.
def main(options,help,funs):  # nil; main program
    saved,fails={},0
    passed = 0
    failed = 0
    for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k]=v
    if options.help:
        print(help) 
    else:
        for what in funs.keys():
            if options.go=="all" or what==options.go:
                for k,v in saved.items:
                    options[k]=v
                Seed = options.seed
                if funs[what]()==false:
                    fails=fails+1
                    print("❌ fail:",what) 
                    failed += 1
                else:
                    print("✅ pass:",what) 
                    passed += 1
        for k,v in globals().items():
            if k not in b4:
                print(f"#W ?{k} {type(v)}")
        return passed,failed