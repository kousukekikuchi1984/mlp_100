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

from collections import Counter

c = Counter()

for sentence in outputs:
    for line in sentence:
        c[line["base"]] += 1

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
data = c.most_common(10)

zipped = list(zip(*data))
columns = zipped[0]
values = zipped[1]
fp = FontProperties(fname='/System/Library/Assets/com_apple_MobileAsset_Font5/458cb75c37483d7bcdfd68445b7246c76ecb29a6.asset/AssetData/Osaka.ttf')
plt.bar(range(0, 10), values)
plt.xticks(range(0, 10), columns, fontproperties=fp)
plt.xlim(xmin=-1, xmax=10)
plt.title("最頻単語の出現率", fontproperties=fp)
plt.xlabel("高い単語", fontproperties=fp)
plt.ylabel("出現率", fontproperties=fp)
plt.grid(axis='y')
plt.show()

