import math
from .. import numerics

class Num(object):
    def __init__(self, at = 0, txt = ""):
        self.at, self.txt = at , txt 
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = math.inf, -math.inf
        self.w = -1 if self.txt.endswith("-") else 1

    def add(self, n, d):
        if n != "?": 
            self.n += 1 
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = math.min(n, self.lo)
            self.hi = math.max(n, self.hi)

    def mid(self):
        return self.mu 
    
    def div(self):
        return (self.m2 <0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self, x, n):
        return x if x=="?" else numerics.rnd(x, n)



