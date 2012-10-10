from itertools import permutations
import sys

if __name__ == "__main__":
    filename = "A-small-practice.in"
    
    with open(filename) as f:
        with open(filename.replace(".in", ".out"), "w") as output:
            tests = int(f.readline().strip())
            
            for case in xrange(tests):
                min = sys.maxint
                f.readline() #skip the array length
                A = [int(i) for i in f.readline().strip().split(" ")]
                B = [int(i) for i in f.readline().strip().split(" ")]
                
                for pA in permutations(A):
                    for pB in permutations(B):
                        sum = 0
                        for i in range(len(pA)):
                            sum += pA[i] * pB[i]
                            
                        if sum < min:
                            min = sum
                
                print "Case %d: %d" % (case + 1, min)
                output.write("Case %d: %d\n" % (case + 1, min))