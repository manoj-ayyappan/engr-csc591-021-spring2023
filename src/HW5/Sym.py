# CLASS - SYM
# Summarize a stream of symbols.

import math

class Sym(object):
    # initialization
    def __init__(self, at = 0, txt = ""):
        self.at, self.txt = at , txt 
        self.n   = 0
        self.has = {}
        self.most, self.mode = 0, None

    # Updates count of things seen so far
    def add(self, x):
        if x != "?": 
            self.n += 1 
            if x in self.has.keys():
                self.has[x] = 1 + self.has[x]
            else:
                self.has[x] = 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x 

    # Returns the mode
    def mid(self):
        return self.mode 
    
    # Function to calculate the entropy
    def entropy(self, p):
        return p * math.log(p,2) 

    # Returns the entropy
    def div(self):
        e=0; 
        for _,n in self.has.items():
            e = e + self.entropy(n/self.n)
        return -e

    # Returns the same number. 
    # Symbols don't get rounded
    def rnd(self,x):
        return x 
    
    # Calculates the distance between 2 symbols
    # Returns 0 or 1
    def dist(self, s1, s2):
        if s1 == "?" and s2 == "?":
            retVal = 1
        else:
            if s1 == s2:
                retVal = 0 
            else:
                retVal = 1
        return retVal



