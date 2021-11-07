# factorial en iteratif
import sys
n = int(sys.argv[1])
r = 1

while n > 0 :
    r *= n
    n -= 1

print(r)