
output = []
with open("hightemp.txt") as f:
    for l in f:
        output.append( l.replace("\t", ",") )

print("".join(output))
