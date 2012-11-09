#!/usr/bin/python
# O(2^N) fibonacci


import sys
sys.path.append(".")
sys.path.append("..")
import easylab


# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

e = easylab.Easylab("fib2")
e.start()

# go
def fibonacci(n):
    return n>=2 and fibonacci(n-2)+fibonacci(n-1) or n

r = fibonacci(N)

e.end()

# log it
e.log(N=N, time=e.getElapsedTime())

print e.timeStr()
print r

