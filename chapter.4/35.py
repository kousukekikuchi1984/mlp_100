# -*- coding: utf-8 -*-

import re
import MeCab

def openfile(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents

def parse_all(contents):
    t = MeCab.Tagger("")
    return t.parse(contents)

def writefile(path, data):
    with open(path, "w") as f:
        f.write(data)


# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

def transformer(parsed):
    def run():
        lines = parsed.split("\n")
        output = []
        for line in lines:
            tagged = line.split("\t")
            word = tagged[0]
            tags = tagged[1].split(",")
            #
            jdict = {}
            jdict["surface"] = word
            jdict["base"] = tags[6]
            jdict["pos"] = tags[0]
            jdict["pos1"] = tags[1]
            output.append(jdict)
            if word == "。":
                yield output
                output = []
    outputs = []
    r = run()
    while True:
        try:
            outputs.append(next(r))
        except Exception:
            return outputs

mecabed = openfile("neko.txt.mecab")
outputs = transformer(mecabed)

results = []
curs = []
for sentence in outputs:
    for line in sentence:
        if line["pos"] == "名詞":
            curs.append(line["surface"])
        else:
            if len(curs) > 0:
                results.append( "".join(curs) )
                curs = []

print(sorted(set(results), key= lambda c: len(c))) 
