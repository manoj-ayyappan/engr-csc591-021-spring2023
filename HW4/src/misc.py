import strings
import json
import Data

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
      u = t.rows[len(t.rows) - n - 1]
      row.append(u[-1])
  return rows

def repPlace(data):
  n = 20
  g = [[' ' for j in range(n+1)] for i in range(n+1)]
  maxy = 0
  print("")
  for r, row in enumerate(data.rows):
    c = chr(64 + r)
    print(c, row.cells[-1])
    x, y = int(row.x * n), int(row.y * n)
    maxy = max(maxy, y+1)
    g[y+1][x+1] = c
  print("")
  for y in range(1, maxy):
    print("".join(g[y]))

def repgrid(sFile):
  t = __import__(sFile)
  rows = repRows(t, transpose(t.cols))
  cols = repCols(t.cols)
  show(rows.cluster())
  show(cols.cluster())
  repPlace(rows)

def show(node, what, cols, nPlaces, lvl=0): #--> nil; prints the tree generated from `DATA:tree`.
    if node:
        print("| "*lvl + str(len(node.get("data").rows)) + "  ", end = "")
        if not node.get("left") or lvl==0:
            print(strings.o(node["data"].stats("mid",node["data"].cols.y,nPlaces)))
        else:
            print("")
        show(node.get("left") , what,cols, nPlaces, lvl+1)
        show(node.get("right"), what,cols, nPlaces, lvl+1)

def dofile(fileName):
    with open(fileName) as f:
        s = f.read()
    return json.loads(s)