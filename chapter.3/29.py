# -*- coding: utf-8 -*-
import re
import json
import urllib.parse, urllib.request

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

def remove_markup(text):
    text = re.sub(r"\^{2, 10}", "", text)
    regex = r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]"
    regx = re.compile(regex, re.MULTILINE+re.VERBOSE)
    text = regx.sub(r"\1", text)
    # 
    regex = r"\[\[ファイル:(?:[^|]*)?\|(?:[^|]+)?\|(.*)\]\]"
    regx = re.compile(regex, re.MULTILINE+re.VERBOSE)
    text = regx.sub(r"\1", text)
    return text

uktext = uk_text("jawiki-country.json")
text = get_basic_information(uktext)
text = remove_markup(text)
#
reg = re.compile(r"\|(.+) = (.+)", re.MULTILINE + re.VERBOSE)
results = reg.findall(text)
jdict = {}
for r in results:
    jdict[r[0].rstrip()] = r[1]

#
national_flag = jdict["国旗画像"]
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(national_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

# MediaWikiのサービスへリクエスト送信
request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@segavvy)'})
connection = urllib.request.urlopen(request)

# jsonとして受信
data = json.loads(connection.read().decode())

# URL取り出し
url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)

