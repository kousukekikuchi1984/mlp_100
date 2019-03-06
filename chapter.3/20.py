import json

with open("jawiki-country.json") as f:
    for l in f:
        jdict = json.loads(l)
        if jdict["title"] == "イギリス":
            print(jdict["text"])
            break
