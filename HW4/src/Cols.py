import re, Num, Sym
import lists

class Cols(object):
    def __init__(self, t):
        self.names, self.all, self.x, self.y = t, {}, {}, {}
        for n,s in t.items(): 
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
        for t in (self.x, self.y):
            for k,v in t.items():
                v.add(row.cells[v.at])






