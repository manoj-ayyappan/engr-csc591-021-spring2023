import math
import globalVars as g
import numerics
import query
import lists

def tiles(rxs):
    # makes on string per treatment showing rank, distribution, and values
    lo, hi = math.inf, -math.inf
    for rx in rxs:
        lo = min(lo, rx['has'][0])
        hi = max(hi, rx['has'][-1])
    
    for rx in rxs:
        t, u = rx['has'], [' ']*g.the["width"]
        
        def of(x, most):
            return max(1, min(most, x))
        
        def at(x):
            index = of(len(t)*x//1, len(t))
            return t[int(index)]
        
        def pos(x):
            return math.floor(of(g.the["width"]*(x-lo)/(hi-lo+1E-32)//1, g.the["width"]))
        
        a, b, c, d, e = at(.1), at(.3), at(.5), at(.7), at(.9) 
        A, B, C, D, E = pos(a), pos(b), pos(c), pos(d), pos(e)
        
        for i in range(A, B+1):
            u[i] = '-'
        for i in range(D, E+1):
            u[i] = '-'
        
        u[g.the["width"]//2] = '|'
        u[C] = '*'
        
        rx['show'] = ''.join(u) + ' {' + "{:>6.2f}".format(a)
        
        for x in [b, c, d, e]:
            rx['show'] += ', ' +  "{:>6.2f}".format(x)
        
        rx['show'] += '}'
    
    return rxs


def scottKnot(rxs):
    def merges(i, j):
        out = lists.RX({}, rxs[i]['name'])
        for k in range(i, j+1):
            out = merge(out, rxs[j])
        return out
    
    def same(lo, cut, hi):
        l = merges(lo, cut)
        r = merges(cut+1, hi)
        return numerics.cliffsDelta(l['has'], r['has']) and numerics.bootstrap(l['has'], r['has'])
    
    def recurse(lo, hi, rank):
        cut, best = None, 0
        b4 = merges(lo, hi)
        
        for j in range(lo, hi+1):
            if j < hi:
                l = merges(lo, j)
                r = merges(j+1, hi)
                now = (l['n']*(query.mid(l) - query.mid(b4))**2 + r['n']*(query.mid(r) - query.mid(b4))**2) / (l['n'] + r['n'])
                if now > best:
                    if abs(query.mid(l) - query.mid(r)) >= cohen:
                        cut, best = j, now
        
        if cut and not same(lo, cut, hi):
            rank = recurse(lo, cut, rank) + 1
            rank = recurse(cut+1, hi, rank)
        else:
            for i in range(lo, hi+1):
                rxs[i]['rank'] = rank
        return rank 
    
    rxs.sort(key=lambda x: query.mid(x))
    cohen = query.div(merges(1, len(rxs))) * g.the['cohen']
    recurse(0, len(rxs)-1, 1)
    return rxs

