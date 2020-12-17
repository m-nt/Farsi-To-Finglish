import random as r
import json
with open("dick.json", mode="r", encoding="utf-8") as target:
    maindic = json.load(target)
txt = "رحیم"
out = ""
for i in range(0, len(txt)):
    if i == len(txt)-1:
        out += maindic[txt[i]]["l"]
    elif i == 0:
        out += maindic[txt[i]]["f"][int(r.random()*3)]
    else:
        if maindic[txt[i+1]]["tier"] > 1:
            out += maindic[txt[i]]["mtu"]
        elif maindic[txt[i]]["tier"] > 1:
            out += maindic[txt[i]]["mtn"]
        else:
            out += maindic[txt[i]]["mtn"][int(r.random()*3)]
print(out)
