import re
import json

def uk_text(path):
    with open("jawiki-country.json") as f:
        for l in f:
            jdict = json.loads(l)
            if jdict["title"] == "イギリス":
                return jdict["text"]

def get_basic_information(uktext):
    regex = (r"^{{基礎情報 国"
r"([\s\S]*)"
r"^}}")
    reg = re.compile(regex, re.MULTILINE)
    finds = reg.findall(uktext)
    return finds[0]

uktext = uk_text("jawiki-country.json")
text = get_basic_information(uktext)
reg = re.compile(r"\|(.+) = (.+)", re.MULTILINE + re.VERBOSE)
results = reg.findall(text)
jdict = {}
for r in results:
    jdict[r[0]] = re.sub(r"\^{2, 10}", "", r[1])

print(jdict)
