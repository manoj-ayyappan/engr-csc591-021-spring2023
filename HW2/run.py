# HW2

import examples
import re
import strings
import sys
import globalVariables

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

