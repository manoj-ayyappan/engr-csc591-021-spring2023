# the,help = {},"""
# script.lua : an example script with help text and a test suite  
# (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
# USAGE:   script.lua  [OPTIONS] [-g ACTION]
# OPTIONS:
#   -d  --dump  on crash, dump stack = false
#   -g  --go    start-up action      = data
#   -h  --help  show help            = false
#   -s  --seed  random number seed   = 937162211
# ACTIONS:
# """


# Classes
# id,obj=0
# function obj(s,    t,new) --> t; create a klass and a constructor 
#   function new(_,...) id=id+1; local i=setmetatable({a=s,id=id}, t); t.new(i,...); return i end
#   t={}; t.__index = t;return setmetatable(t, {__call=new}) end

id = 0
classes={}

args = {}
args["dataMembers"] = "iD"

def new(i):
    i.n   = 0
    i.has = {}
    i.most, i.mode = 0, None

def add(i,x): 
    if x != "?":
        i.n = i.n + 1 
        i.has[x] = 1 + (i.has[x] or 0)
        if i.has[x] > i.most:
            i.most,i.mode = i.has[x], x 

def mid(i,x):
    return i.mode 

def div(i,x, fun,e): 
    def fun(p):
        return p*math.log(p,2)
    e=0; 
    for _,n in enumerate(i.has):
        e = e + fun(n/i.n) 
    return -e 


args["functions"] = {
    "new" : lambda cls, i : new(i),
    "add" : lambda cls : add,
    "mid" : lambda cls : mid,
    "div" : lambda cls : div,
    }


def obj(className): 
    def constructor(self, arg):
        global id 
        id = id + 1
        self.iD = id
        for key, value in arg['functions'].items():
            setattr(classes[0], key, value)


    
    # method
    def displayMethod(self, arg):
        print(arg)
    
    # class method
    @classmethod
    def classMethod(cls, arg):
        print(arg)
    
    # creating class dynamically
    classes[0] = type(className, (object, ), {
        # constructor
        "__init__": constructor,
        
        # data members
        # "string_attribute": None,

        
        # member functions
        "func_arg": displayMethod,
        "class_func": classMethod
    })

obj("SYM")
c1 = classes[0](args)
c1.new({})
c1.add(1,2)
c1.mid(2,3)
# c1.div()
    
    

