# Easylab
# onesuper
# Filename: easylab_autorun.py
# Under Mit License

import re

def argvTransform(argv):
    regex = ur"\d+:\d+"

    # construct the new argv
    new_argv = []

    for arg in argv:
# [m:n]
        if re.match(regex, arg):
            argv = arg.split(":")  # "1:10" => ["1", "10"]
            # expand ["1", "10"] to ["1", "2", ... , "10"]
            exp_argv = [str(i) for i in range(int(argv[0]),
                                              int(argv[1])+1)]
            new_argv.append(exp_argv) 
# [a,b,c]
        elif arg.find(",") > 0:
            new_argv.append(arg.split(","))
# naked string
        else:
            new_argv.append([arg]) # "1" => ["1"]
            

    #  !!! This part will be re-written by map()
    argc = len(new_argv)
    if argc == 1:
        return listGen1(new_argv)
    elif argc == 2:
        return listGen2(new_argv)
    elif argc == 3:
        return listGen3(new_argv)
    elif argc == 4:
        return listGen4(new_argv)
    elif argc == 5:
        return listGen5(new_argv)
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



def stringToDict(string):
    if string == "":
        return {}
    strlist = string.split(",")
    strlist = [s.strip() for s in strlist]
    dictstring = "{"
    for s in strlist:
        v = s.split("=")
        pair = "'" + v[0] + "'" + ":" + v[1]
        dictstring += (pair + ",")
    dictstring += "}"
    return eval(dictstring)
        
