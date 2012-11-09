#!/usr/bin/python
# a stupid test


import sys
sys.path.append(".")
import easylab


#read the arguments
if len(sys.argv ) < 4:
    print "wrong arguments"
    sys.exit(1)

var1 = int(sys.argv[1])
var2 = int(sys.argv[2])
var3 = int(sys.argv[3])

# get a easylab and start timer
e = easylab.Easylab("stupid")
e.start()


#really stupid main body
a = []
for i in range(var1):
    a.append('a')

for i in range(var2): 
    a.append('b')

for i in range(var3):
    a.append('c')


# end timer and show time
e.end()
print e.timeStr()

# log data
e.log(var1=var1, var2=var2, var3=var3, time=e.getElapsedTime())
