class Map(object):
    def __init__(self, points):
        self.points = points
        self.sinks = [[" " for col in row] for row in points]
        self.sinkChar = 'a'
        
    def findSink(self, row, col):
        if self.sinks[row][col] != " ": #short-circuit if found other route
            return self.sinks[row][col]
        else:
            toRow, toCol = self.findDest(row, col)
            if toRow == None: #found a sink
                return self.sinks[row][col]
            self.sinks[row][col] = self.findSink(toRow, toCol) #recursively follow path until sink found
            return self.sinks[row][col]
        
    def findDest(self, row, col):
        val = self.points[row][col]
        toRow = None
        toCol = None
        
        #Find which direction to move
        if row > 0: #North
            if self.points[row-1][col] < val: 
                val = self.points[row-1][col]
                toRow = row-1
                toCol = col
        
        if col > 0: #West
            if self.points[row][col-1] < val: 
                val = self.points[row][col-1]
                toRow = row
                toCol = col-1
                
        if col < len(self.points[row]) - 1: #East
            if self.points[row][col+1] < val:
                val = self.points[row][col+1]
                toRow = row
                toCol = col+1
                
        if row < len(self.points) - 1: #South
            if self.points[row+1][col] < val:
                val = self.points[row+1][col]
                toRow = row+1
                toCol = col
        
        if toRow == None:
            self.sinks[row][col] = str(self.sinkChar)
            self.sinkChar = chr(ord(self.sinkChar) + 1)

        return (toRow, toCol)

    def solve(self):
        for row in xrange(len(self.points)):
            for col in xrange(len(self.points[row])):
                self.sinks[row][col] = self.findSink(row, col)
        
        return str(self)
        
    def __str__(self):
        rows = [" ".join(row) for row in self.sinks]
        return "\n".join(rows)
            
if __name__ == "__main__":
    filename = "B-small-practice.in"
    
    with open(filename) as f:
        with open(filename.replace(".in", ".out"), "w") as output:
            tests = int(f.readline().strip())
            
            for case in xrange(tests):
                rowCount = int(f.readline().strip().split(" ")[0])
                rows = []
                for rowIdx in xrange(rowCount):
                    nums = f.readline().strip().split(" ")
                    rows.append([int(n) for n in nums])
                map = Map(rows)
                output.write("Case #%d:\n" % (case + 1))
                output.write(map.solve() + "\n")