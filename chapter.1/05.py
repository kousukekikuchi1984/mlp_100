s = "I am an NLPer"

def ngram(words, n):
    output = []
    for i in range(len(words) - (n - 1)):
        output.append([words[i], words[i+1]])
    return output

words = s.split(" ")
chars = "".join(words)
print(ngram(words, 2))
print(ngram(chars, 2))
