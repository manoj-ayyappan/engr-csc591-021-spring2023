import math

Seed=937162211
def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi)) # n ; a integer lo..hi-1

def rand(lo = 0,hi = 1):
    # n; a float "x" lo<=x < x
    global Seed
    lo, hi = lo, hi
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces = 3):
    mult = 10**nPlaces
    return math.floor(n * mult + 0.5) / mult