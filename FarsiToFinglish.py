import random as r
import json
with open("Dictionary.json", mode="r", encoding="utf-8") as target:
    data = json.load(target)
txt = "مهربان"
out = ""
for i in range(0, len(txt)):
    if txt[i] == " ":
        out += " "
    else:
        if i == len(txt)-1:
            out += data[txt[i]]["l"]
        elif i == 0:
            out += data[txt[i]]["f"][int(r.random()*3)]
        else:
            if txt[i+1] == " ":
                out += data[txt[i]]["l"]
            elif data[txt[i+1]]["tier"] > 1:
                out += data[txt[i]]["mtu"]
            elif data[txt[i]]["tier"] > 1:
                out += data[txt[i]]["mtn"]
            else:
                out += data[txt[i]]["mtn"][int(r.random()*3)]
print(out)
