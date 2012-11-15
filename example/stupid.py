#!/usr/bin/python
# a stupid test


import sys
import easylab.easylab as e


#read the arguments
if len(sys.argv ) < 4:
    print "wrong arguments"
    sys.exit(1)

var1 = int(sys.argv[1])
var2 = int(sys.argv[2])
var3 = int(sys.argv[3])

# get a easylab and start timer
easylab = e.Easylab("stupid")
easylab.start()


#really stupid main body
a = []
for i in range(var1):
    a.append('a')

for i in range(var2): 
    a.append('b')

for i in range(var3):
    a.append('c')


# end timer and show time
easylab.end()
print easylab.timeStr()

# log data
logstr = "var1=%d, var2=%d, var3=%d, time=%f" % (var1, var2, var3,
                                                 easylab.getElapsedTime())
easylab.log(logstr)

