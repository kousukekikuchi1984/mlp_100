def split(ary, n):
    output = []
    times = int(len(ary) / n) + 1
    for i in range(n):
        output.append(ary[i*times:(i+1)*times])
    return output

def create_file(filepath, data):
    with open(filepath, "w") as f:
        for l in data:
            f.write(l)


ary = []
with open("hightemp.txt") as f:
    for l in f:
        ary.append(l)

outputs = split(ary, 3)
for i, o in enumerate(outputs, 1):
    create_file("hightemp_sep_%s.txt" % str(i), o)



