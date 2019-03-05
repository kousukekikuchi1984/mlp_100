import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"

def parse(s):
    return s.split(" ")

def check(s):
    return len(s) > 4

def random_choice(s):
    fc = s[0]
    lc = s[-1]
    #
    picks = ""
    for _ in s[1:-1]:
        picks += random.choice(s[1:-1])
    return "%s%s%s" % (fc, picks, lc)

chars = parse(s)
output = []
for word in chars:
    if check(word):
        output.append(random_choice(word))
    else:
        output.append(word)

print(output)
