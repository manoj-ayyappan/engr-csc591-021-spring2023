import math
import query
import lists
    
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
            e -= n/col.n * math.log(n/col.n, 2)
        return e
    else:
        # return (sorted(has(col))[int(len(has(col)) * 0.9)] - sorted(has(col))[int(len(has(col)) * 0.1)]) / 2.58
        return (lists.per(has(col), 0.9) - lists.per(has(col), 0.1)) / 2.58