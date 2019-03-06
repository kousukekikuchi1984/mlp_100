import re
import json

def uk_text(path):
    with open("jawiki-country.json") as f:
        for l in f:
            jdict = json.loads(l)
            if jdict["title"] == "イギリス":
                return jdict["text"]

def get_basic_information(uktext):
    reg = re.compile(r"{{(.+)}}")
    searched = reg.search(uktext)
    return searched.group(1)

uktext = uk_text("jawiki-country.json")
text = get_basic_information(uktext)
print(text)
reg = re.compile(r"\|(.+) = (.+)", re.MULTILINE + re.VERBOSE)
results = reg.findall(text)
jdict = {}
for r in results:
    jdict[r[0]] = r[1]

print(jdict)
