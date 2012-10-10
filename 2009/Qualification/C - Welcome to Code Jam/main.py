def search(pi, pm):
    global count
    
    if pm >= len(MATCH):
        count += 1
        return
    
    if pi >= len(line):
        return #exhausted input
    
    for i in range(pi, len(line)):
        if line[i] == MATCH[pm]:
            #target found, try rest of string
            search(i+1, pm+1)

if __name__ == "__main__":
    MATCH = "welcome to code jam"
    filename = "C-small-practice.in"
    
    with open(filename) as f:
        with open(filename.replace(".in", ".out"), "w") as output:
            inputs = [l.strip() for l in f.readlines()][1:]
    
            for i, line in enumerate(inputs):
                count = 0
                search(0, 0)
                output.write("Case #%d: %04d\n" % (i+1, count % 10000))