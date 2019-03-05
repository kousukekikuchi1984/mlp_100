rows = 0
with open("hightemp.txt") as f:
    for l in f:
        rows += 1

print(rows)
