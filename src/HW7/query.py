import math
import query
import lists
import numerics
    
def has(col):
    if not col.isSym and not col.ok:
        # TODO Sort 
        col.has = lists.sort(col.has)
    col.ok = True  # the invariant here is that "has" is ready to be shared.
    return col.has

def mid(col, mode=None, most=None):
    if col.isSym:
        return col.mode
    else:
        return lists.per(query.has(col), 0.5)
    

def div(col, e=None):
    if col.isSym:
        e = 0
        for _, n in col.has.items():
            e = e - n / col.n * math.log(n/col.n, 2)
        return e
    else:
        # return (sorted(has(col))[int(len(has(col)) * 0.9)] - sorted(has(col))[int(len(has(col)) * 0.1)]) / 2.58
        return (lists.per(has(col), 0.9) - lists.per(has(col), 0.1)) / 2.58
    
def stats(data, fun = None, cols = None, nPlaces = 2):
    if cols == None:
        cols = data.cols.y

    if(fun == None):
        fun = mid
    tmp = lists.kap(cols, lambda k, col: (numerics.rnd(fun(col), nPlaces), col.txt))
    tmp["N"] = len(data.rows)
    return tmp

def value(has, nB=None, nR=None, sGoal=True):
    sGoal = sGoal or True
    nB = nB or 1
    nR = nR or 1
    b, r = 0, 0
    for x, n in has.items():
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b = b / (nB + 1/math.inf)
    r = r / (nR + 1/math.inf)
    return b ** 2 / (b + r)
