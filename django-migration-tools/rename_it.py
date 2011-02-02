# -*- coding: utf-8 -*-

__author__ = "Matias Herranz (matiasherranz@gmail.com)"
__version__ = "0.1"


import os

file1 = open('./orig.txt', 'r')
file2 = open('./dest.txt', 'r')

lines1 = [line[:-1] for line in file1]
lines2 = [line[:-1] for line in file2]

for i in range(0, 78):
    print 'Renaming: %s -> %s' % (lines1[i], lines2[i])
    os.rename(lines1[i], lines2[i])