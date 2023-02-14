import math
import numerics

class Num(object):
    def __init__(self, at = 0, txt = ""):
        self.at, self.txt = at , txt 
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = math.inf, -math.inf

        if self.txt.endswith("-"):
            self.w = -1 
        else: 
            self.w = 1 

    def add(self, n):
        if n != "?": 
            self.n += 1 
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        return self.mu 
    
    def div(self):
        return (self.m2 <0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self, x, n):
        return x if x=="?" else numerics.rnd(x, n)

    def norm(self, n):
        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1, n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            n1 = 1 if n2 < 0.5 else 0
        if n2 == "?":
            n2 = 1 if n1 < 0.5 else 0
        return abs(n1 - n2)



