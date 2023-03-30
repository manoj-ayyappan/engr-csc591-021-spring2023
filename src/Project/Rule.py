import lists
import copy

class RULE():
    t = {}
    def __init__(self, ranges, maxSize):
        self.t = {}
        for range in ranges:
            if range.txt not in self.t:
                self.t[range.txt] = []
            self.t[range.txt].append({'lo': range.lo, 'hi': range.hi, 'at': range.at})
        self.t = self.prune(maxSize)
    
    def prune(self, maxSize, n=0):
        tmp = copy.deepcopy(self.t)
        for txt, ranges in tmp.items():
            n += 1
            if len(ranges) == maxSize[txt]:
                n += 1
                self.t.pop(txt)
        if n > 0:
            return self.t


    def showRule(self):
        
        def merges(attr, ranges):
            sorted_ranges = sorted(ranges, key=lambda x: x['lo'])
            merged_ranges = merge(sorted_ranges)
            pretty_merged_ranges = []
            for i in range(len(merged_ranges)):
                pretty_merged_ranges.append(merged_ranges[i]['lo'] if merged_ranges[i]['lo'] == merged_ranges[i]['hi'] else [merged_ranges[i]['lo'], merged_ranges[i]['hi']])
            # pretty_merged_ranges = map(pretty, merged_ranges)
            # pretty_merged_ranges = merged_ranges
            return pretty_merged_ranges, attr
        
        def merge(t0):
            t, j = [], 0
            while j < len(t0):
                left, right = t0[j], t0[j+1] if j+1 < len(t0) else None
                if right and left['hi'] == right['lo']:
                    left['hi'] = right['hi']
                    j += 1
                t.append({'lo': left["lo"], 'hi': left["hi"]})
                j += 1
            return t if len(t0) == len(t) else merge(t)
        
        y = self.t
        return lists.kap(self.t, merges)

    def selects(self, rows):
        def disjunction(ranges, row):
            for range in ranges:
                lo, hi, at = range["lo"], range["hi"], range["at"]
                x = row.cells[at]
                if x == "?":
                    return True
                if lo == hi and lo == x:
                    return True
                if lo <= x and x < hi:
                    return True
            return False
        
        def conjunction(row):
            for _,ranges in self.t.items():
                if not disjunction(ranges, row): 
                    return False
            return True
        
        def filteringFunction(pair):
            key, value = pair
            return conjunction(value)
        
        return list(filter(filteringFunction, rows.items()))

