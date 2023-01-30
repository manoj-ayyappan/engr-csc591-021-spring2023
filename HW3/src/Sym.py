import math

class Sym(object):
    def __init__(self, at = 0, txt = ""):
        self.at, self.txt = at , txt 
        self.n   = 0
        self.has = {}
        self.most, self.mode = 0, None

    def add(self, x):
        if x != "?": 
            self.n += 1 
            if x in self.has.keys():
                self.has[x] = 1 + self.has[x]
            else:
                self.has[x] = 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x 

    def mid(self):
        return self.mode 
    
    def entropy(self, p):
        return p * math.log(p,2) 

    def div(self):
        e=0; 
        for _,n in self.has.items():
            e = e + self.entropy(n/self.n)
        return -e

    def rnd(self,x):
        return x 



