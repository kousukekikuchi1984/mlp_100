ary = []
with open("hightemp.txt") as f:
    for l in f:
        ary.append(l.split("\t")[0])

print(set(ary))
