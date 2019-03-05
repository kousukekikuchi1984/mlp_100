ary = []
with open("hightemp.txt") as f:
    for l in f:
        ary.append( float(l.split("\t")[2]) )

print(sorted(ary, reverse=True) )
