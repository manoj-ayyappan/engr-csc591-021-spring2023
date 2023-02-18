# CLASS Data
# Store many rows, summarized into columns

import strings
import lists
import numerics
import Row
import Cols
import globalVars as g
import math


class Data(object):
    # Initialization
    # A container of `i.rows`, to be summarized in `i.cols`
    def __init__(self, src={}):
        self.rows, self.cols = {}, None
        if str(type(src)) == "<class 'str'>":
            # load from a csv file on disk
            strings.csv(src,self.add)
        else:
           # load from a list
           lists.map(src, self.add)
    
    def add(self, t):
        # Add a new row, update column headers
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

    def clone(self, init = {}): 
        # return a DATA with same structure as `ii. 
        data = Data({0:self.cols.names})
        if(type(init) == dict):
            for it, x in init.items():
                data.add(x.cells)
            return data
        else:
            for it, x in enumerate(init):
                data.add(x.cells)
            return data

    # def stats(self, what=None, cols=None, nPlaces=None):
    #     # Reports mid or div of cols (defaults to i.cols.y)
    #     if what == None:
    #         what = "mid"
    #     if cols == None:
    #         cols = self.cols.y
    #     if nPlaces == None:
    #         nPlaces = 2

    #     def fun(k, col):
    #         if isinstance(what, str):
    #             return round(getattr(col, what)(), nPlaces), col.txt
    #         else:
    #             return round(what(col), nPlaces), col.txt
    #     return lists.kap(cols, fun)
    
    def furthest(self, row1, rows):
        # Sort other `rows` by distance to `row`
        t = self.around(row1, rows, None)
        return t[len(t) - 1]
    
    
    def better(self, row1, row2, s1=0, s2=0, ys=None, x=None, y=None):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        for n,col in ys.items():
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)
        
    def around(self, row1, rows=None, cols=None):
        # sort other `rows` by distance to `row`
        if rows is None:
            rows = self.rows
        else:
            if(type(rows) == dict):
                rows = {k:v for k,v in rows.items()}
            else:
                rows = {k:v for k,v in enumerate(rows)}
        sorted_stuff = sorted([{"row": row2, "dist": self.dist(row1, row2, cols)} for k, row2 in rows.items()], key=lambda x: x["dist"])
        return {k:v for k,v in enumerate(sorted_stuff)}

    
    def dist(self, row1, row2, cols=None, n=None, d=None):
        # Returns 0..1 distance `row1` to `row2`
        n, d = 0, 0
        cols = cols if cols else self.cols.x
        for k, col in cols.items():
            n = n + 1
            d = d + (col.dist(row1.cells[col.at], row2.cells[col.at])**g.the.get("p"))
        return (d/n)**(1/g.the.get("p"))

    def half(self, rows=None, cols=None, above=None):
        # Divides data using 2 far points
        # def project(row):
        #     return {"row": row, "dist": numerics.cosine(self.dist(row, A, cols), self.dist(row, B, cols), c)}
        
        def project(row):
            x, y = numerics.cosine(dist(row, A), dist(row, B), c)
            if not hasattr(row,"x"):
                row.x = x 
            if not hasattr(row,"y"):
                row.y = y
            return {"row": row, "x": x, "y": y}

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        if rows is None:
            rows = self.rows

       
        if above is None:
            A = lists.any(rows)
        else:
            A = above
        B = self.furthest(A,rows).get("row")
        c = dist(A, B)
        left, right = [], []
        mid = None
        
        mapped_rows = lists.map(rows, project)
        only_mapped_rows = list(mapped_rows.values())
        sorted_mapped_rows = sorted(only_mapped_rows, key=lambda item: item["x"])

        for n, tmp in enumerate(sorted_mapped_rows):
            if n < len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    
    # def cluster(self, rows=None, mini=None, cols=None, above=None):
    #     # returns `rows`, recursively halved
    #     node = {}
    #     rows = {k:v for k,v in enumerate(rows)} if rows else self.rows
    #     cols = cols if cols else self.cols.x
    #     node["data"] = self.clone(rows)
    #     node["left"] = {}
    #     node["right"] = {}
    #     if len(rows) >= 2:
    #         left, right, node["A"], node["B"], node["mid"], c = self.half(rows, cols, above)
    #         node["left"] = self.cluster(left, mini, cols, node["A"])
    #         node["right"] = self.cluster(right, mini, cols, node["B"])
    #     return node
    
    def cluster(i, rows=None, cols=None, above=None):
        if rows is None:
            rows = i.rows
        if cols is None:
            cols = i.cols.x
        node = {'data': i.clone(rows)}
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = i.half(rows, cols, above)
            node['left'] = i.cluster(left, cols, node['A'])
            node['right'] = i.cluster(right, cols, node['B'])
        return node


    # def sway(self, rows=None, min=None, cols=None, above=None):
    #     node, left, right, A, B, mid = None, None, None, None, None, None
    #     rows = {k:v for k,v in enumerate(rows)} if rows else self.rows
    #     if min is None:
    #         min = (len(rows))**g.the.get("min")
    #     if cols is None:
    #         cols = self.cols.x
    #     temp = {}
    #     node = {"data": self.clone(rows)}
    #     if len(rows) > 2 * min:
    #         left, right, node["A"], node["B"], node["mid"], c= self.half(rows, cols, above)
    #         if self.better(node["B"], node["A"]):
    #             left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
    #         node["left"] = self.sway(left, min, cols, node["A"])
    #     return node
    
    def sway(self, cols=None, worker=None, best=None, rest=None):
        def workerF(rows, worse, above = None):
            if len(rows) <= (len(self.rows)**g.the["min"]):
                return rows, lists.many(worse, g.the["rest"] * len(rows))
            else:
                l, r, A, B, mid, c = self.half( rows, cols, above)
                if self.better(B, A):
                    l, r, A, B = r, l, B, A
                lists.map(r, lambda row: lists.push(worse, row))
                return workerF(l, worse, A)
        if worker is None:
            best, rest = workerF(self.rows, [])
            return self.clone(best), self.clone(rest)
        else:
            best, rest = worker
            return self.clone(best), self.clone(rest)



    def tree(self, rows = None, cols = None, above=None, here=None):
        if rows is None:
            rows = self.rows
        if here is None:
            here = {'data': self.clone(rows)}
        if len(rows) >= 2*(len(self.rows)**g.the["min"]):
            left, right, A, B, mid, c = self.half(rows, cols, above)
            here['left'] = self.tree( left, cols, A)
            here['right'] = self.tree(right, cols, B)
        return here
    





