def openfile(filename):
    ary = []
    with open(filename) as f:
        for l in f:
            ary.append( l.rstrip() )
    return ary

col1 = openfile("col1.txt")
col2 = openfile("col2.txt")
for c1, c2 in zip(col1, col2):
    print("%s\t%s" % (c1, c2))
