from .. import strings
from .. import lists
from . import Row
from . import Cols


# Store many rows, summarized into columns
class Data(object):
    def __init__(self, src={}):
        self.rows, self.cols = {}, None
        if type(src) == "string":
            # load from a csv file on disk
            strings.csv(src,self.add)
        else:
           # load from a list
           map(src, self.add)
    
    def add(self, t):
        if self.cols:
            # true if we have already seen the column names
            t = t.cells and t or Row(t) # ensure is a ROW, reusing old rows in the are passed in
            # t =ROW(t.cells and t.cells or t) # make a new ROW
            lists.push(self.rows, t) # add new data to "i.rows"
            self.cols.add(t)  # update the summary information in "ic.ols"
        else:
           self.cols=Cols.Cols(t)  #  here, we create "i.cols" from the first row

    def clone(self, init = {}): # return a DATA with same structure as `ii. 
        data = Data({self.cols.names})
        lists.map(init, lambda x: data.add(x))
        return data

    def stats(self, what, cols, nPlaces): # reports mid or div of cols (defaults to i.cols.y)
        def fun(k, col):
            return col.rnd(getattr(col)[what or "mid"](col), nPlaces), col.txt 
        return lists.kap(cols or self.cols.y, fun)


