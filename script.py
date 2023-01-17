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
args["functions"] = ["new","add","mid", "div"]


def obj(className): 
    def constructor(self, arg):
        global id 
        id = id + 1
        self.iD = id
        def method1():
            print("hello")
        setattr(className, 'func', classmethod(method1))


    
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
c1.func()
    
    

