#!/usr/bin/python
# Filename: easylab_autorun.py

import re

def argvTransform(argv):
    regex = ur"\d+:\d+"

    # construct the new argv
    new_argv = []
    for arg in argv:
        if re.match(regex, arg):
            new_argv.append(arg.split(":")) # "1:10" => ["1", "10"]
        else:
            new_argv.append([arg])
            
    # expand ["1", "4"] to ["1", "2", "3", "4"]
    fat_argv = []
    for arg in new_argv:
        if len(arg) > 1:
            fat_argv.append([str(i) for i in range(int(arg[0]), int(arg[1])+1)])
        else:
            fat_argv.append(arg)

    argc = len(fat_argv)
    if argc == 1:
        return listGen1(fat_argv)
    elif argc == 2:
        return listGen2(fat_argv)
    elif argc == 3:
        return listGen3(fat_argv)
    elif argc == 4:
        return listGen4(fat_argv)
    elif argc == 5:
        return listGen5(fat_argv)
    else:
        return []    #!!!!!!!!!

        
def listGen1(fat_argv):        
    return [[a] for a in fat_argv[0]]
        

def listGen2(fat_argv):        
    return [[a, b] for a in fat_argv[0] for b in fat_argv[1]]

           
def listGen3(fat_argv):        
    return [[a, b, c] for a in fat_argv[0] for b in fat_argv[1] for c in fat_argv[2]]

        
def listGen4(fat_argv):        
    return [[a, b, c, d] for a in fat_argv[0] for b in fat_argv[1]
           for c in fat_argv[2] for d in fat_argv[3]]

        
def listGen5(fat_argv):        
    return [[a, b, c, d, e] for a in fat_argv[0] for b in fat_argv[1]
           for c in fat_argv[2] for d in fat_argv[3] for e in  fat_argv[4]]

