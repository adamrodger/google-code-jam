with open("B-small-practice.in") as f:
    with open("B-small-practice.out", "w") as output:
        lines = [line.strip() for line in f]
        outputs = []
        n = int(lines[0])

        for i in xrange(1, n+1):
            input = lines[i]
            line = "Case #%d: %s" % (i, " ".join(input.split(" ")[::-1]))
            outputs.append(line)
            
        output.write("\n".join(outputs))