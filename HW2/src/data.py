import strings
import lists
import Row
import Cols


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
        data = Data({self.cols.names})
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



