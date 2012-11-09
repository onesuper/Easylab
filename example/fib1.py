#!/usr/bin/python
# O(N) fibonacci


import sys
sys.path.append(".")
sys.path.append("..")
import easylab


# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

e = easylab.Easylab("fib1")
e.start()

# go
a, b = 0, 1
for i in range(N):
    a,b = b, a+b

e.end()

# log it
e.log(N=N, time=e.getElapsedTime())

print e.timeStr()
print a

