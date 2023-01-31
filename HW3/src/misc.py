import strings

def show(node, what, cols, nPlaces, lvl=0): #--> nil; prints the tree generated from `DATA:tree`.
    if node:
        print("| "*lvl + len(node.get("data").rows) + "  ")
        if not node["left"] or lvl==0:
            print(strings.o(node["data"].stats("mid",node["data"].cols.y,nPlaces)))
        else:
            print("")
        show(node["left"] , what,cols, nPlaces, lvl+1)
        show(node["right"], what,cols, nPlaces, lvl+1)