import re, Num, Sym
import lists

class Cols(object):
    def __init__(self, t):
        self.names, self.all, self.x, self.y, self.klass = t, {}, {}, {}, None
        for n,s in t.items():  
            col = Sym.Sym(n,s) if s.find('^[A-Z]+') != -1 else Num.Num(n,s)
            lists.push(self.all, col)
            if not s.find('X$'):
                if s.find('!$'):
                    self.klass = col
                    lists.push(self.y if s.find('[!+-]$') else self.x, col)

    def add(self, row):
        for t in [self.x,self.y]:
            for col in t:
                col.add(row.cells[col.at])






