#!/usr/bin/python
# O(2^N) fibonacci


import sys
import easylab.easylab as e


# read argumeny
if len(sys.argv ) < 2:
    print "wrong arguments"
    sys.exit(1)
N = int(sys.argv[1])

easylab = e.Easylab("fib2")
easylab.start()

# go
def fibonacci(n):
    return n>=2 and fibonacci(n-2)+fibonacci(n-1) or n

r = fibonacci(N)

easylab.end()

# log it
logstr = "N=%d, time=%f" % (N, easylab.getElapsedTime())
easylab.log(logstr)


print e.timeStr()
print r

