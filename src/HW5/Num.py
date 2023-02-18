# CLASS Num
# Summarizes a stream of numbers

import math
import numerics
import globalVars as g

class Num(object):
    # Initialization
    def __init__(self, at = 0, txt = ""):
        self.has = {}
        self.at, self.txt = at , txt 
        self.n, self.mu, self.m2 = 0, 0, 0
        self.ok = False
        self.isSym = False
        self.lo, self.hi = math.inf, -math.inf
        if self.txt.endswith("-"):
            self.w = -1 
        else: 
            self.w = 1 

    def add(self, x, n = 1):
        # Add 'n'
        # Update lo and hi
        if x != "?": 
            if n is not None:
                tn = n
            else:
                tn = 1
            self.n = self.n + tn
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)
        if self.isSym:
            self.has[x] = n + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
        else:
            self.lo, self.hi = min(x, self.lo), max(x, self.hi)
            all = len(self.has) - 1
            pos = None
            if all < g.the.get("Max") - 1:
                pos = all + 1
            else:
                if (numerics.rand() < (g.the.get("Max")-1)/self.n):
                    pos = numerics.rint(0, all)
            if pos is not None:
                self.has[pos] = x
                self.ok = False

    def mid(self):
        # Returns mean
        return self.mu 
    
    def div(self):
        # Returns standard deviation using Welford's algorithm
        return (self.m2 <0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self, x, n):
        # Return a rounded number
        return x if x=="?" else numerics.rnd(x, n)

    def norm(self, n):
        # Funtion to normalize values
        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2):
        # Returns the distance
        if n1 == "?" and n2 == "?":
            return 1
        n1, n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            n1 = 1 if n2 < 0.5 else 0
        if n2 == "?":
            n2 = 1 if n1 < 0.5 else 0
        return abs(n1 - n2)



