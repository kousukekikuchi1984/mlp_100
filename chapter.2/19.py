from collections import Counter

counter = Counter()
with open("hightemp.txt") as f:
    for l in f:
        key = l.split("\t")[0]
        counter[key] += 1

print(counter)


