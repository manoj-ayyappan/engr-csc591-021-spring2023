# CLASS Cols
# Factory for managing a set of NUMs or SYMs

import re, Num, Sym
import lists

class Cols(object):
    # Initialization
    def __init__(self, t):
        # Generate NUMs and SYMs from column names
        self.names, self.all, self.x, self.y = t, {}, {}, {}
        if(type(t) == dict):
            f = t.items()
        else:
            f = enumerate(t)
        for n,s in f: 
            match = re.match(r'^[A-Z]', s) 
            if match:
                col = Num.Num(n,s)
            else:
                col = Sym.Sym(n,s)  
            lists.push(self.all, col)
            if not s.endswith('X'):
                if s.endswith('+') or s.endswith('-'):
                    lists.push(self.y ,col)
                else:
                    lists.push(self.x ,col)

    def add(self, row):
        # Update the (not skipped) columns with details from `row`
        for t in (self.x, self.y):
            for k,v in t.items():
                v.add(row.cells[v.at])






