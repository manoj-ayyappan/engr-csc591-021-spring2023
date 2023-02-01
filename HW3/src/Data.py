import strings
import lists
import numerics
import Row
import Cols
import globalVars as g
import math


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
        data = Data({0:self.cols.names})
        for it, x in init.items():
            data.add(x.cells)
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
        for n,col in ys.items():
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)
        
    def around(self, row1, rows=None, cols=None):
        if rows is None:
            rows = self.rows
        else:
            rows = {k:v for k,v in enumerate(rows)}
        sorted_stuff = sorted([{"row": row2, "dist": self.dist(row1, row2, cols)} for k, row2 in rows.items()], key=lambda x: x["dist"])
        return {k:v for k,v in enumerate(sorted_stuff)}

    
    def dist(self, row1, row2, cols=None, n=None, d=None):
        n, d = 0, 0
        cols = cols if cols else self.cols.x
        for k, col in cols.items():
            n = n + 1
            d = d + (col.dist(row1.cells[col.at], row2.cells[col.at])**g.the.get("p"))
        return (d/n)**(1/g.the.get("p"))

    def half(self, rows=None, cols=None, above=None):
        def project(row):
            return {"row": row, "dist": numerics.cosine(self.dist(row, A, cols), self.dist(row, B, cols), c)}

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        if rows is None:
            rows = self.rows

       
        some = lists.many(rows, g.the.get("Sample"))

        if above is None:
            A = lists.any(some)
        else:
            A = above
        B = self.around(A,some)[(g.the.get("Far") * len(rows))//1 - 1].get("row")
        c = dist(A, B)
        left, right = [], []
        mid = None
        
        mapped_rows = lists.map(rows, project)
        only_mapped_rows = list(mapped_rows.values())
        sorted_mapped_rows = sorted(only_mapped_rows, key=lambda x: x["dist"])

        for n, tmp in enumerate(sorted_mapped_rows):
            if n < len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    
    def cluster(self, rows=None, mini=None, cols=None, above=None):
        node = {}
        rows = {k:v for k,v in enumerate(rows)} if rows else self.rows
        mini = mini if mini else (len(rows))**g.the.get("min")
        cols = cols if cols else self.cols.x
        node["data"] = self.clone(rows)
        node["left"] = {}
        node["right"] = {}
        if len(rows) > 2*mini:
            left, right, node["A"], node["B"], node["mid"], c = self.half(rows, cols, above)
            node["left"] = self.cluster(left, mini, cols, node["A"])
            node["right"] = self.cluster(right, mini, cols, node["B"])
        return node

    def sway(self, rows=None, min=None, cols=None, above=None):
        node, left, right, A, B, mid = None, None, None, None, None, None
        rows = {k:v for k,v in enumerate(rows)} if rows else self.rows
        if min is None:
            min = (len(rows))**g.the.get("min")
        if cols is None:
            cols = self.cols.x
        temp = {}
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node["A"], node["B"], node["mid"], c= self.half(rows, cols, above)
            if self.better(node["B"], node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
            node["left"] = self.sway(left, min, cols, node["A"])
        return node



