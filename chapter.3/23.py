import re
import json

def uk_text(path):
    with open("jawiki-country.json") as f:
        for l in f:
            jdict = json.loads(l)
            if jdict["title"] == "イギリス":
                return jdict["text"]


uktext = uk_text("jawiki-country.json")
reg = re.compile(r"^={2,}(.+?)(={2,})$", re.MULTILINE + re.VERBOSE)
results = reg.findall(uktext)
sections = [ [t[0], len(t[1])-1] for t in results]
print(sections)
