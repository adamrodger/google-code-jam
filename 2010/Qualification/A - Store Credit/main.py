def findIndexes(credit, prices):
    for j in xrange(len(prices)):
        for k in xrange(j+1, len(prices)):
            if prices[j] + prices[k] == credit:
                return str(j+1) + " " + str(k+1)

outputs = []
filename = "A-small-practice.in"
with open(filename) as f:
    lines = [line.strip() for line in f]
    
    N = int(lines[0])
    
    
    for i in xrange(N):
        idx = (i * 3) + 1
        
        credit = int(lines[idx])
        prices = [int(p) for p in lines[idx+2].split(" ")]
        
        outputs.append("Case #%d: %s" % (i+1, findIndexes(credit, prices)))

with open(filename.replace(".in", ".out"), "w") as f:
    f.write("\n".join(outputs))