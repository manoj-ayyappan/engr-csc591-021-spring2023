import math
import query
import lists

def has(col):
    if not hasattr(col,"isSym") and not col.ok:
        myKeys = list(col.has.keys())
        myKeys.sort()
        sorted_dict = {i: col.has[i] for i in myKeys}
    col.ok = True 
    return col.has
    
def mid(col, mode=None, most=None):
    if col.isSym:
        return col.get("mode")
    else:
        return lists.per(query.has(col), 0.5)
    

def div(col, e=None):
    if col.get("isSym"):
        e = 0
        for _, n in col.get("has").items():
            e -= n/col.get("n") * math.log(n/col.get("n"), 2)
        return e
    else:
        return (sorted(has(col))[int(len(has(col)) * 0.9)] - sorted(has(col))[int(len(has(col)) * 0.1)]) / 2.58