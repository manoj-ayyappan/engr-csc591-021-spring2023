import math
import examples

global Seed
Seed=937162211

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi)) 

def rand(lo = 0,hi = 1):
    lo, hi = lo, hi
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647 

def rnd(n, nPlaces = 3):
    mult = 10**nPlaces
    return math.floor(n * mult + 0.5) / mult
    