import strings
import json
import Data
import lists
import query

def transpose(t):
  u = []
  for i in range(len(t[0])):
    u.append([t[j][i] for j in range(len(t))])
  return u

def repCols(cols):
  cols = cols.copy()
  for i, col in enumerate(cols):
    col[-1] = str(col[0]) + ":" + str(col[-1])
    for j in range(1, len(col)):
      col[j-1] = col[j]
    col.pop()
  cols.insert(0, [f"Num{j}" for j in range(1, len(cols[0])+1)])
  cols[0][-1] = "thingX"
  cols = {k:{j:l for j,l in enumerate(v)} for k,v in enumerate(cols)}
  return Data.Data(cols)

def repRows(t, rows):
  rows = rows.copy()
  for j, s in enumerate(rows[-1]):
    rows[0][j] = str(rows[0][j]) + ":" + str(s)
  rows.pop()
  for n, row in enumerate(rows):
    if n == 0:
      row.append("thingX")
    else:
      u = t.get("rows")[len(t.get("rows")) - n]
      row.append(u[-1])
  return Data.Data(rows)

def repPlace(data):
  n = 20
  g = [[' ' for j in range(n+1)] for i in range(n+1)]
  maxy = 0
  print("")
  f = data.rows
  for r, row in data.rows.items():
    c = chr(64 + r + 1)
    print(c, row.cells[-1])
    x, y = int(row.x * n), int(row.y * n)
    maxy = max(maxy, y+1)
    g[y][x] = c
  print("")
  for y in range(0, maxy):
    print(" ".join(g[y]))
  print("")

def repgrid(sFile):
  t = dofile(sFile)
  rows = repRows(t, transpose(t.get("cols")))
  cols = repCols(t.get("cols"))
  show(rows.cluster(), 3)
  show(cols.cluster(), 3)
  repPlace(rows)

def show(node, nPlaces, lvl=0):
    if node:
        print("|.. " * lvl, end="")
        if not node.get("left"):
            print(lists.last(lists.last(node["data"].rows).cells))
        else:
            print("%.f" % round(100 * node["c"], nPlaces))
        show(node.get("left"), nPlaces, lvl + 1)
        show(node.get("right"), nPlaces, lvl + 1)


def dofile(fileName):
    with open(fileName) as f:
        s = f.read()
    return json.loads(s)

def showTree(tree, lvl=0, post=""):
  if tree:
    lvl = lvl or 0
    print("{}[{}] ".format(("|.. ") * lvl, len(tree['data'].rows)), end="")
    print((lvl == 0 or not tree.get('left')) and strings.o(query.stats(tree['data'])) + (strings.ooo(lists.any(tree['data'].rows)))or "")
    showTree(tree.get('left'), lvl+1)
    showTree(tree.get('right'), lvl+1)


def selects(rule,rows,    disjunction,conjunction):
  def disjunction(ranges,row,    x):
    for _,range in ranges.items():
      lo, hi, at = range.lo, range.hi, range.at
      x = row[at]
      if x == "?":
         return True
      if lo==hi and lo==x:
         return True
      if lo<=x  and x< hi:
          return True 
    return False 
  def conjunction(row):
    for _,ranges in rule.items(): 
      if not disjunction(ranges,row):
         return False
    return True 
  def fun(r):
      if conjunction(r):
         return r
  return lists.map(rows, fun)