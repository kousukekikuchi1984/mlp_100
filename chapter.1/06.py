s1 = "paraparaparadise"
s2 = "paragraph"
X = set()
Y = set()

def ngram(words, n):
    output = []
    for i in range(len(words) - (n - 1)):
        output.append([words[i], words[i+1]])
    return output

sl1 = ngram(s1, 2)
for ch in sl1:
    X.add("".join(ch))

sl2 = ngram(s2, 2)
for ch in sl2:
    Y.add("".join(ch))

print(X | Y)
print(X & Y)
print(X - Y)

print("se" in X)
print("se" in Y)
