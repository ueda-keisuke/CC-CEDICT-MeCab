import re

pattern = re.compile(r"^(.*?) (.*?) \[(.*?)\] /(.*?)$")

# surface -> csv (surface, left id, right id, cost, pinyin, traditional, simplified, definition)
dict = {}

with open("cedict_ts.u8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue

        match = pattern.match(line)
        if match:
            traditional = match.group(1)
            simplified = match.group(2)
            pinyin = match.group(3)
            definition = match.group(4)

            cost = int(max(-36000, -400 * (len(traditional) ** 1.5)))
            dict[traditional] = f"{traditional},0,0,{cost},*,*,*,*,{pinyin},{traditional},{simplified},{definition}"
            dict[simplified] = f"{simplified},0,0,{cost},*,*,*,*,{pinyin},{traditional},{simplified},{definition}"

with open("cedict.csv", mode='w') as f:
    for value in dict.values():
        f.write(value + "\n")

