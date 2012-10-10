presses = {'a':1, 'b':2, 'c':3, 'd':1, 'e':2, 'f':3, 'g':1, 'h':2, 'i':3, 'j':1, \
           'k':2, 'l':3, 'm':1, 'n':2, 'o':3, 'p':1, 'q':2, 'r':3, 's':4, 't':1, \
           'u':2, 'v':3, 'w':1, 'x':2, 'y':3, 'z':4, ' ':1}
keys = {'a':'2', 'b':'2', 'c':'2', 'd':'3', 'e':'3', 'f':'3', 'g':'4', 'h':'4', 'i':'4', 'j':'5', \
        'k':'5', 'l':'5', 'm':'6', 'n':'6', 'o':'6', 'p':'7', 'q':'7', 'r':'7', 's':'7', 't':'8', \
        'u':'8', 'v':'8', 'w':'9', 'x':'9', 'y':'9', 'z':'9', ' ':'0'}
        
def translate(phrase):
    chars = phrase[:]
    output = ""
    lastKey = -1
    
    for c in chars:
        key = keys[c]
        if key == lastKey:
            output += ' '
        
        lastKey = key
        output += key * presses[c]
        
    return output
    
if __name__ == "__main__":
    filename = "C-large-practice.in"
    outputs = []
    
    with open(filename) as f:
        lines = [l.replace("\n", "") for l in f]
        outputs = [translate(l) for l in lines[1:]]
    
    with open(filename.replace(".in", ".out"), "w") as f:
        for i in range(1, len(outputs)+1):
            f.write("Case #%d: %s\n" % (i, outputs[i-1]))