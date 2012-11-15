#!/usr/bin/python
# O(1) fibonacci


import sys
import easylab.easylab as e
from math import sqrt

# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

easylab = e.Easylab("fib3")
easylab.start()

# go

r = int(((1+sqrt(5))/2)**N/sqrt(5))

easylab.end()


# log it
logstr = "N=%d, time=%f" % (N ,easylab.getElapsedTime())
easylab.log(logstr)


print easylab.timeStr()
print r

