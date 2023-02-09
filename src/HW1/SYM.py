import math 

class SYM:
    def __init__(self):
        self.n   = 0
        self.has = {}
        self.most, self.mode = 0, None

    def add(self, x): 
        if x != "?":
            self.n = self.n + 1 
            if x not in self.has:
                self.has[x] = 0
            self.has[x] += 1
            if self.has[x] > self.most:
                self.most,self.mode = self.has[x], x

    def mid(self):
        return self.mode 

    def fun(p):
        return p*math.log(p,2)

    def div(self, fun = fun,e = 0): 
        for _,n in self.has.items():
            e = e + fun(n/self.n) 
        return -e 
