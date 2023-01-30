import strings
import lists
import Row
import Cols
import globalVars as g
import math
import random


# Store many rows, summarized into columns
class Data(object):
    def __init__(self, src={}):
        self.rows, self.cols = {}, None
        if str(type(src)) == "<class 'str'>":
            # load from a csv file on disk
            strings.csv(src,self.add)
        else:
           # load from a list
           lists.map(src, self.add)
    
    def add(self, t):
        if self.cols != None:
            # true if we have already seen the column names
            if hasattr(t, "cells"):
                t = t  
            else: 
                t = Row.Row(t) # ensure is a ROW, reusing old rows in the are passed in
            # t =ROW(t.cells and t.cells or t) # make a new ROW
                lists.push(self.rows, t) # add new data to "i.rows"
                self.cols.add(t)  # update the summary information in "i.cols"
        else:
           self.cols=Cols.Cols(t)  #  here, we create "i.cols" from the first row

    def clone(self, init = {}): # return a DATA with same structure as `ii. 
        data = Data(self.cols.names)
        lists.map(init, lambda x: data.add(x))
        return data

    def stats(self, what=None, cols=None, nPlaces=None):
        if what == None:
            what = "mid"
        if cols == None:
            cols = self.cols.y
        if nPlaces == None:
            nPlaces = 2

        def fun(k, col):
            return round(getattr(col, what)(), nPlaces), col.txt
        return lists.kap(cols, fun)
    
    def better(self, row1, row2, s1=0, s2=0, ys=None, x=None, y=None):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)
        
    def around(i, row1, rows=None, cols=None):
        if rows is None:
            rows = i.rows
        return sorted(
            [{"row": row2, "dist": i.dist(row1, row2, cols)} for row2 in rows],
            key=lambda x: x["dist"],
        )

    
    def dist(self, row1, row2, cols=None, n=None, d=None):
        n, d = 0, 0
        cols = cols if cols else self.cols.x
        for col in cols:
            n = n + 1
            d = d + (col.dist(row1.cells[col.at], row2.cells[col.at])**g.the.p)
        return (d/n)(1/g.the.p)

    def half(self, rows=None, cols=None, above=None):
        def project(row):
            return {"row": row, "dist": cosine(self.dist(row, A, cols), self.dist(row, B, cols), c)}

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        if rows is None:
            rows = self.rows
        some = random.sample(rows, g.the.Sample)
        A = above or some[0]
        B = self.around(A, some)[int(g.the.Far * len(rows))].row
        c = dist(A, B)
        left, right = [], []
        mid = None
        for n, tmp in enumerate(sorted(map(rows, project), key=lambda x: x["dist"])):
            if n <= len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    
    def cluster(self, rows=None, min=None, cols=None, above=None):
        node, left, right, A, B, mid = {}, None, None, None, None, None
        rows = rows if rows else self.rows
        min = min if min else (len(rows))**g.the.min
        cols = cols if cols else self.cols.x
        node["data"] = self.clone(rows)
        if len(rows) > 2*min:
            left, right, node["A"], node["B"], node["mid"] = self.half(rows, cols, above)
            node["left"] = self.cluster(self, left, min, cols, node["A"])
            node["right"] = self.cluster(self, right, min, cols, node["B"])
        return node



