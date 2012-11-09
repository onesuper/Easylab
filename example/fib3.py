#!/usr/bin/python
# O(1) fibonacci


import sys
sys.path.append(".")
sys.path.append("..")
import easylab
from math import sqrt

# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

e = easylab.Easylab("fib3")
e.start()

# go

r = int(((1+sqrt(5))/2)**N/sqrt(5))

e.end()

# log it
e.log(N=N, time=e.getElapsedTime())

print e.timeStr()
print r

