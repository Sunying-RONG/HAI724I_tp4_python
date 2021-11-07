# factorielle en recusif 
import sys
n = int(sys.argv[1])

def factorielle(n) :
    if n == 0 :
        return 1
    return n * factorielle(n-1)

print(factorielle(n))