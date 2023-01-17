class NUM:
    def __init__(self):
        i=0 #remove this
    def new(i):
        i.n, i.mu, i.m2 = 0, 0, 0
        i.lo, i.hi = math.huge, -math.huge

    def add(i,n): 
        if n != "?":
            i.n  = i.n + 1
            d = n - i.mu
            i.mu = i.mu + d/i.n
            i.m2 = i.m2 + d*(n - i.mu)
            i.lo = math.min(n, i.lo)
            i.hi = math.max(n, i.hi) 

    def mid(i,x):
        return i.mu 
    def div(i,x):  
        return (i.m2 <0 or i.n < 2) and 0 or (i.m2/(i.n-1))^0.5 
