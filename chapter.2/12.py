col1 = []
col2 = []

with open("hightemp.txt", "r") as f:
    for l in f:
        ary = l.split("\t")
        col1.append(ary[0])
        col2.append(ary[1])

print("\n".join(col1))
print("\n".join(col2))

