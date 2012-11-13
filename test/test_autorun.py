#!/usr/bin/python
# Filename: test_autorun.py

import sys
sys.path.append("..")
sys.path.append(".")
import easylab_autorun as auto






print auto.argvTransform(["python", "123.py", "1", "2", "3"])
print auto.argvTransform(["python", "123.py", "1:2", "1:3", "3"])
print auto.argvTransform(["a.out", "1:3", "2,4,8"])
