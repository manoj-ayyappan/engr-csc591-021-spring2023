# Numerics

import math

Seed=937162211
def rint(lo,hi):
    # Generate an integer lo..hi-1
    return math.floor(0.5 + rand(lo,hi)) # n ; a integer lo..hi-1

def rand(lo = 0,hi = 1):
    # Generate a float "x" lo<=x < x
    global Seed
    # print("Seed-> " + str(Seed))
    lo, hi = lo, hi
    # print("lo-> " + str(lo))
    # print("hi-> " + str(hi))
    Seed = (16807 * Seed) % 2147483647
    retVal = lo + (hi-lo) * Seed / 2147483647
    # print("retVal-> " + str(retVal))
    return retVal

def rnd(n, nPlaces = 3):
    # return `n` rounded to `nPlaces`
    mult = 10**nPlaces
    return math.floor(n * mult + 0.5) / mult

def cosine(a, b, c):
    # find x,y from a line connecting `a` to `b`
    if c == 0:
        return (0, 0)
    x1 = (a**2 + c**2 - b**2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = math.sqrt(abs(a**2 - x2**2))
    return x2, y