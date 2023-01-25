import re, Num, Sym
from .. import lists

class Cols(object):
    def __init__(self, t):
        self.names, self.all, self.x, self.y, self.klass = t, {}, {}, {}
        for n,s in t.items():
            col = Num.Num(n,s) if re.search("^[A-Z]+",s) else Sym.Sym(n,s)
            lists.push(self.all, col)
            if not re.search("X$",s):
                if re.search("!$",s):
                    self.klass = col
                lists.push(re.search("[!+-]$",s) and self.y or self.x, col)

    def add(self, row):
        for _,t in {self.x,self.y}.items():
            for _,col in t.items():
                col.add(row.cells[col.at])





