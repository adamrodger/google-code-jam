import re

filename = "A-large-practice.in"
outputs = []
lines = []
words = []
patterns = []

with open(filename) as f:
    lines = [l.strip() for l in f]
    
L, D, N = lines[0].split(" ")
D = int(D)

for i in xrange(1, D+1):
    words.append(lines[i])
        
patterns = [re.compile(l.replace("(", "[").replace(")", "]")) for l in lines[D+1:]]

for i, pattern in enumerate(patterns):
    count = 0
    for word in words:
        if pattern.match(word):
            count += 1
    outputs.append("Case #%d: %d" % (i+1, count))
    
with open(filename.replace(".in", ".out"), "w") as f:
    f.write("\n".join(outputs))