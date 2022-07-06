import os
import time
import getopt
import sys
from recur import func
from graphics import displayHeader
from optionchecker import optionchecker


d0 = 0
c0 = 0
argumentList = sys.argv[1:]
d0, c0 = optionchecker(argumentList)


displayHeader()
path = os.getcwd()
tar = sys.argv[1]


func(path, tar, d0, c0)
print("File not found!")
