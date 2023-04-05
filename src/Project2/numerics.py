# Numerics

import math
import globalVars as g
import Num
import lists
import random
import numerics

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

def samples(t,n):
  u= list(range(n))
  for i in range(0,n):
      index = random.randint(0, n-1)
      u[i] = t[index]
  return u

def cosine(a, b, c):
    # find x,y from a line connecting `a` to `b`
    if c == 0:
        return (0, 0)
    x1 = (a**2 + c**2 - b**2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = math.sqrt(abs(a**2 - x2**2))
    return x2, y

def cliffsDelta(ns1, ns2):
    if len(ns1) > 256:
        ns1 = lists.many(ns1, 256)
    if len(ns2) > 256:
        ns2 = lists.many(ns2, 256)
    if len(ns1) > 10 * len(ns2):
        ns1 = lists.many(ns1, 10 * len(ns2))
    if len(ns2) > 10 * len(ns1):
        ns2 = lists.many(ns2, 10 * len(ns1))
    n, gt, lt = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y:
                gt += 1
            if x < y:
                lt += 1
    uyt = lt - gt
    clidhui =  g.the["cliffs"]
    ytr = abs(lt - gt) / n
    return (abs(lt - gt) / n) <= g.the["cliffs"]

def bootstrap(y0,z0):
    x, y, z, yhat, zhat = Num.Num(), Num.Num(), Num.Num(), [], []
    # x will hold all of y0,z0
    # y contains just y0
    # z contains just z0
    for y1 in y0:
        x.add(y1)
        y.add(y1)
    for z1 in z0:
        x.add(z1)
        z.add(z1)
    xmu, ymu, zmu = x.mu, y.mu, z.mu
    # yhat and zhat are y,z fiddled to have the same mean
    for y1 in y0:
        yhat.append(y1 - ymu + xmu)
    for z1 in z0:
       zhat.append(z1 - zmu + xmu)
    # tobs is some difference seen in the whole space
    tobs = delta(y,z)
    n = 0
    for _ in range(1,g.the["bootstrap"]):
    # here we look at some delta from just part of the space
    # it the part delta is bigger than the whole, then increment n
        if delta(Num.Num(t = numerics.samples(yhat, len(yhat))), Num.Num(t = numerics.samples(zhat, len(zhat)))) > tobs:
           n = n + 1 
    # if we have seen enough n, then we are the same
    # On Tuesdays and Thursdays I lie awake at night convinced this should be "<"
    # and the above "> obs" should be "abs(delta - tobs) > someCriticalValue". 
    return n / g.the["bootstrap"] >= g.the["conf"]

def gaussian(mu = 0, sd = 1):
    mu, sd = mu or 0, sd or 1
    sq, pi, log, cos = math.sqrt, math.pi, math.log, math.cos
    r = random.random
    return mu + sd * sq(-2 * log(r())) * cos(2 * pi * r())


def delta(i, other):
  e, y, z= 1E-32, i, other
  return abs(y.mu - z.mu) / ((e + y.sd**2/y.n + z.sd**2/z.n)**0.5)

# Given two tables with the same keys, report if their
# values are different.
def diffs(nums1,nums2):
    def fun(k, nums):
        return cliffsDelta(nums.has,nums2[k].has),nums.txt
    
    return lists.kap(nums1, fun)

def float_range(start, stop, step):
    i = 0
    while True:
        next_val = start + i * step
        if next_val >= stop:
            break
        yield next_val
        i += 1