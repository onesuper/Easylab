#!/usr/bin/python
# O(N) fibonacci


import sys
import easylab.easylab as e


# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

easylab = e.Easylab("fib1")
easylab.start()

# go
a, b = 0, 1
for i in range(N):
    a,b = b, a+b

easylab.end()

# log it
logstr = "N=%d, time=%f" % (N, easylab.getElapsedTime())
easylab.log(logstr)

print e.timeStr()
print a

