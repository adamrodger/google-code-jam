from datetime import datetime, timedelta

class Journey(object):
    def __init__(self, startTime, endTime, startLoc, T):
        self.startTime = datetime.strptime(startTime, "%H:%M")
        self.endTime = datetime.strptime(endTime, "%H:%M") + timedelta(minutes = int(T))
        self.startLoc = startLoc
        self.start = True

    def __repr__(self):
        return "<%s, %s, %s, %s>" % (self.startLoc, self.startTime.strftime("%H:%M"), self.endTime.strftime("%H:%M"), self.start)

class Timetable(object):
    def __init__(self, journeys):
        self.journeys = sorted(journeys, key= lambda j: j.startTime)
        
    def findStarts(self):
        for j in self.journeys:
            n = self._findNext(j)
            if n:
                n.start = False

        tA = [j for j in self.journeys if j.startLoc == "A" and j.start]
        tB = [j for j in self.journeys if j.startLoc == "B" and j.start]
        
        return "%d %d" % (len(tA), len(tB))
    
    def _findNext(self, start):
        next = [j for j in self.journeys if j.startTime >= start.endTime and j.start and j.startLoc != start.startLoc]
        if len(next):
            return next[0]
        else:
            return None
        
if __name__ == "__main__":
    filename = "B-large-practice.in"
    
    with open(filename) as f:
        with open(filename.replace(".in", ".out"), "w") as output:
            tests = int(f.readline().strip())
            
            for case in xrange(tests):                            
                T = int(f.readline().strip())
                NA, NB = [int(s) for s in f.readline().strip().split(" ")]

                jA = []
                jB = []
                
                for i in xrange(NA):
                    l = f.readline().strip()
                    jA.append(Journey(l.split(" ")[0], l.split(" ")[1], "A", T))
                
                for i in xrange(NB):
                    l = f.readline().strip()
                    jB.append(Journey(l.split(" ")[0], l.split(" ")[1], "B", T))

                timetable = Timetable(jA + jB)
                output.write("Case #%d: %s\n" % (case + 1, timetable.findStarts()))