Seed=937162211

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi)) 

def rand(lo,hi):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647 

def rnd(n, nPlaces): 
    mult = 10^(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult