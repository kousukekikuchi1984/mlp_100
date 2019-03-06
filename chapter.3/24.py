import re
import json

def uk_text(path):
    with open("jawiki-country.json") as f:
        for l in f:
            jdict = json.loads(l)
            if jdict["title"] == "イギリス":
                return jdict["text"]


uktext = uk_text("jawiki-country.json")
reg = re.compile(r"ファイル:(.+.jpg?)\|\[\[(.+?)\]\]", re.MULTILINE + re.VERBOSE)
results = reg.findall(uktext)
print(results)
