import math

def has(col):
    if not col.get("isSym") and not col.get("ok"):
        col["has"].sort()
        col["ok"] = True 
        return col.get("has")
    
def mid(col, mode=None, most=None):
    if col.get("isSym"):
        return col.get("mode")
    else:
        return (sum(has(col)) / len(has(col))) / 2
    

def div(col, e=None):
    if col.get("isSym"):
        e = 0
        for _, n in col.get("has").items():
            e -= n/col.get("n") * math.log(n/col.get("n"), 2)
        return e
    else:
        return (sorted(has(col))[int(len(has(col)) * 0.9)] - sorted(has(col))[int(len(has(col)) * 0.1)]) / 2.58