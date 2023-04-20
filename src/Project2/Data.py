# CLASS Data
# Store many rows, summarized into columns

from audioop import reverse
import strings
import lists
import numerics
import Row
import Cols
import globalVars as g
import math
import query
import Rule
import discretization
import functools



class Data(object):
    # Initialization
    # A container of `i.rows`, to be summarized in `i.cols`
    def __init__(self, src={}, datai=None, data2=None, col_names=None):
        self.rows, self.cols = {}, None
        if str(type(src)) == "<class 'str'>":
            # load from a csv file on disk
            strings.csv(src,self.add)
        else:
            tmp = []
            if(datai):
                for i in range(len(src)):
                    tmp.append(src[i][1])
                self.cols=Cols.Cols(datai.cols.names)
            if(data2):
                for i in range(len(src)):
                    tmp.append(src[i])
                self.cols=Cols.Cols(data2.cols.names)
            if(col_names):
                for i in range(len(src)):
                    tmp.append(src[i])
                self.cols=Cols.Cols(col_names)
            if len(tmp) > 0:
                lists.map(tmp, self.add)
            else:
                lists.map(src, self.add)
    
    def add(self, t):
        # Add a new row, update column headers
        if self.cols != None:
            # true if we have already seen the column names
            if hasattr(t, "cells"):
                t = t  
                lists.push(self.rows, t)
                self.cols.add(t)
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
    
    def furthest(self, row1, rows):
        # Sort other `rows` by distance to `row`
        t = self.around(row1, rows, None)
        return t[len(t) - 1]
    
    def better(self, row1, row2, s1=0, s2=0, ys=None, x=None, y=None):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        if g.the["better"] == 'zitler':
            return self.better_original(row1, row2, s1, s2, ys, x, y)
        if g.the["better"] == 'hv':
            return self.better_hv(row1, row2, ys=ys)
        if g.the["better"] == 'bdom':
            return self.better_bdom( row1, row2, ys=ys)
        return None

    ###########
    # ORIGINAL
    ###########
    def better_original(self, row1, row2, s1=0, s2=0, ys=None, x=None, y=None):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        for n,col in ys.items():
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)

    ###########
    # Substituting zitler's predicate with boolean domination
    ###########
    def is_dominant_bdom(self, row1, row2, ys=None):
        ys = self.cols.y if ys is None else ys
        
        dominates = False
        for n, col in ys.items():
            x = col.norm(row1.cells[col.at]) * col.w * -1
            y = col.norm(row2.cells[col.at]) * col.w * -1
            if x > y:
                return False
            elif x < y:
                dominates = True
        return dominates

    def better_bdom(self, row1, row2, ys=None):
        is_row1_dominant = self.is_dominant_bdom(row1, row2, ys=ys)
        is_row2_dominant = self.is_dominant_bdom(row2, row1, ys=ys)
        if is_row1_dominant and not is_row2_dominant:
            return True
        else:
            return False


    ###########
    # Substituting zitler's predicate with hyper volume
    ###########
    

    def hypervolume(self, row, ys=None):
        ys = self.cols.y if ys is None else ys
        
        hv = 1
        for n, col in ys.items():
            x = col.norm(row.cells[col.at]) * col.w 
            hv *= x
        
        return hv

    def better_hv(self, row1, row2, ys=None):
        ys = self.cols.y if ys is None else ys
        hv1 = 1
        hv2 = 1
        for n, col in ys.items():
            x1 = col.norm(row1.cells[col.at]) * col.w 
            x2 = col.norm(row2.cells[col.at]) * col.w 
            hv1 *= x1
            hv2 *= x2
        
        if hv1 > hv2:
            return False
        else:
            return True



    def betters(self,  n):
        def fun(r1, r2):
            return -1 if self.better(r1, r2) else 1

        rowItems = list(self.rows.values())
        tmp=sorted(rowItems, key = functools.cmp_to_key(fun))
        return (lists.slice(tmp,0,n), lists.slice(tmp,n)) if not n is None else (tmp, None)
        
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
        # print((d/n)**(1/g.the.get("p")))
        return (d/n)**(1/g.the.get("p"))
    
    

    # def half_2(self, rows=None, cols=None, above=None):
    #     # Divides data using 3 far points
    #     def project(row):
    #         x, y = numerics.cosine(dist(row, A), dist(row, B), c)
    #         if not hasattr(row,"x"):
    #             row.x = x 
    #         if not hasattr(row,"y"):
    #             row.y = y
    #         return {"row": row, "x": x, "y": y}

    #     def dist(row1, row2):
    #         return self.dist(row1, row2, cols)

    #     if rows is None:
    #         rows = self.rows

       

    #     if above is None:
    #         A = lists.any(rows)
    #     else:
    #         A = above
    #     B = self.furthest(A,rows).get("row")
    #     for i in range(100):
    #         C = self.furthest(B,rows).get("row")
    #         if self.dist(B, C) > self.dist(A, B):
    #             A = B
    #             B = C
    #     c = dist(A, B)
    #     left, right = [], []
    #     mid = None
        
    #     mapped_rows = lists.map(rows, project)
    #     only_mapped_rows = list(mapped_rows.values())
    #     sorted_mapped_rows = sorted(only_mapped_rows, key=lambda item: item["x"])

    #     for n, tmp in enumerate(sorted_mapped_rows):
    #         if n < len(rows) // 2:
    #             left.append(tmp["row"])
    #             mid = tmp["row"]
    #         else:
    #             right.append(tmp["row"])
    #     evals = 1 if g.the.get("Reuse") and above else 2
    #     return left, right, A, B, mid, c, evals

   
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
        
        # fastmap2, fastmap3
        # resuse = true/false
        # for all datasets
        
        # if above is None:
        #     A = lists.any(rows)
        # else:
        #     A = above if g.the["Reuse"] else lists.any(rows)
        # B = self.furthest(A,rows).get("row")

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
        evals = 1 if g.the.get("Reuse") and above else 2
        return left, right, A, B, mid, c, evals

    ###########
    # ORIGINAL - Hierarchical agglomerative clustering algorithm
    ###########
    def hierarchial_cluster(i, rows=None, cols=None, above=None):
        if rows is None:
            rows = i.rows
        if cols is None:
            cols = i.cols.x
        node = {'data': i.clone(rows)}
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'], node['evals'] = i.half(rows, cols, above)
            node['left'] = i.cluster(left, cols, node['A'])
            node['right'] = i.cluster(right, cols, node['B'])
        return node

    def cluster(i, rows=None, cols=None, above=None):
        if g.the.get('clustering_alg') == "DBSCAN":
            print()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\nDBSCANNNNNNNNNNNNN")
            print()
            return i.dbscan_cluster(rows=None, cols=None)
        else:
            print()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\nHHHHHHHHHH")
            print()
            return i.hierarchial_cluster(rows=None, cols=None, above=None)
    

    def sway(self):
        if g.the["sway"] == 'original':
            return self.sway_original()
        else:
            return self.sway_dbscan()

    ###########
    # ORIGINAL - Sway using Hierarchical clustering 
    ###########    
    def sway_original(self, cols=None, worker=None, best=None, rest=None, evals=0):
        def workerF(rows, worse, evals0,  above = None):
            if len(rows) <= (len(self.rows)**g.the["min"]):
                return rows, lists.many(worse, g.the["rest"] * len(rows)), evals0
            else:
                if type(rows) is list:
                    rows = {i: rows[i] for i in range(len(rows))}
                else:
                    rows = rows

                l, r, A, B, mid, c, evals = self.half( rows, cols, above)
                if self.better(B, A):
                    l, r, A, B = r, l, B, A
                lists.map(r, lambda row: lists.push(worse, row))
                return workerF(l, worse,evals+evals0, A)
        if worker is None:
            best, rest, evals = workerF(self.rows, [], 0)
            return self.clone(best), self.clone(rest), evals
        else:
            best, rest = worker
            return self.clone(best), self.clone(rest), evals

    ###########
    # Sway Using DBSCAN
    ###########      

    def dbscan(self, rows, eps, min_pts):
        clusters = []
        visited = set()
        noise = set()
        for i, row in rows.items():
            if i in visited:
                continue
            visited.add(i)
            neighbors = []
            for j, other_row in rows.items():
                if j != i and self.dist(row, other_row) <= eps:
                    neighbors.append(j)
            if len(neighbors) < min_pts:
                noise.add(rows[i])
            else:
                cluster = set()
                self.expand_cluster(rows, i, neighbors, cluster, visited, eps, min_pts)
                clusters.append(list(cluster))
        return clusters, list(noise)


    def expand_cluster(self, rows, i, neighbors, cluster, visited, eps, min_pts):
        cluster.add(rows[i])
        for j in neighbors:
            if j not in visited:
                visited.add(j)
                other_neighbors = []
                for k, other_row in rows.items():
                    if k != j and self.dist(other_row, rows[j]) <= eps:
                        other_neighbors.append(k)
                if len(other_neighbors) >= min_pts:
                    neighbors.extend(other_neighbors)
            if j not in cluster:
                cluster.add(rows[j])

    # Use eps 0.05 for auto93
    # Use eps 0.25 for coc1000
    # Use eps 0.07 for china
    def sway_dbscan(self, eps= 0.05, min_pts=5):
        eps = g.the["eps"]
        min_pts = g.the["minpts"]
        clusters, noise = self.dbscan(self.rows, eps, min_pts)
        best, rest, evals = self.find_best_cluster(clusters)
        rest = lists.many(rest, g.the["rest"] * len(best))
        return self.clone(best), self.clone(rest) , evals
    
    
    
    def find_best_cluster(self, clusters):
        best_cluster = None
        bestIndex = -1
        best_score = float('-inf')
        evals = 0
        for n, cluster in enumerate(clusters):
            score, evals1 = self.compute_cluster_score(cluster)
            evals += 1
            if score > best_score:
                best_cluster = cluster
                best_score = score
                best_index = n
        rest = []
        for n, cluster in enumerate(clusters):
            if(n != best_index):
                rest.extend(cluster)
        return best_cluster, rest, evals

    def compute_cluster_score(self, cluster):
        score = 0
        count = 0
        for i, row1 in enumerate(cluster):
            for j, row2 in enumerate(cluster):
                if i < j:
                    count += 1
                    if self.better(row1, row2):
                        score += 1
                    else:
                        score -= 1
        return score, count





    



    




    def tree(self, rows = None, cols = None, above=None, here=None):
        if rows is None:
            rows = self.rows
        if here is None:
            here = {'data': self.clone(rows)}
        if len(rows) >= 2*(len(self.rows)**g.the["min"]):
            left, right, A, B, mid, c, evals = self.half(rows, cols, above)
            here['left'] = self.tree( left, cols, A)
            here['right'] = self.tree(right, cols, B)
        return here
    
    def xpln(self, best, rest):
        def v(has):
            return query.value(has, len(best.rows), len(rest.rows), "best")
        
        def score(ranges):
            rule = Rule.RULE(ranges, maxSizes)
            if rule:
                ltr = rule.showRule()
                strings.oo(ltr)
                bestr = rule.selects(best.rows)
                restr = rule.selects(rest.rows)
                if len(bestr) + len(restr) > 0:
                    return v({"best": len(bestr), "rest": len(restr)}), rule
                else:
                    return 0, rule
        
        tmp = []
        maxSizes = {}
        for _, ranges in discretization.bins(self.cols.x, {"best": best.rows, "rest": rest.rows}).items():
            maxSizes[ranges[0].txt] = len(ranges)
            print("")
            for _, range in ranges.items():
                print(range.txt, range.lo, range.hi)
                lists.push(tmp, {"range": range, "max": len(ranges), "val": v(range.y.has)})
        
        rule, most = self.firstN(sorted(tmp, key=lambda d: -d['val']) , score)
        return rule, most
    
    def firstN(self, sortedRanges, scoreFun, useful=None, most=None, out=None):
        # print("")
        # for r in sortedRanges:
            # print(r['range'].txt, r['range'].lo, r['range'].hi, numerics.rnd(r['val'], 2), strings.o(r['range'].y.has))
        
        global first
        first = sortedRanges[0]['val']
        
        def useful(range):
            global first
            if range['val'] > 0.05 and range['val'] > first / 10:
                return range
        
        sortedRanges = list(filter(None, map(useful, sortedRanges))) # reject useless ranges
        
        most, out = -1, None
        
        for n in range(1, len(sortedRanges)+1):
            tmp, rule = scoreFun(list(map(lambda x: x['range'], sortedRanges[:n])))
            if tmp and tmp > most:
                out, most = rule, tmp
        return out, most
    
    def xpln_noprint(self, best, rest):
        def v(has):
            return query.value(has, len(best.rows), len(rest.rows), "best")
        
        def score(ranges):
            rule = Rule.RULE(ranges, maxSizes)
            if rule:
                # ltr = rule.showRule()
                # strings.oo(ltr)
                bestr = rule.selects(best.rows)
                restr = rule.selects(rest.rows)
                if len(bestr) + len(restr) > 0:
                    return v({"best": len(bestr), "rest": len(restr)}), rule
                else:
                    return 0, rule
        
        tmp = []
        maxSizes = {}
        for _, ranges in discretization.bins(self.cols.x, {"best": best.rows, "rest": rest.rows}).items():
            maxSizes[ranges[0].txt] = len(ranges)
            # print("")
            for _, range in ranges.items():
                # print(range.txt, range.lo, range.hi)
                lists.push(tmp, {"range": range, "max": len(ranges), "val": v(range.y.has)})
        
        rule, most = self.firstN(sorted(tmp, key=lambda d: -d['val']) , score)
        return rule, most



    





