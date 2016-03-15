#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("input.txt","r")
space = 0
letterE = 0
total = 0

for R in f.readline():
  if not R:
    break
  space += R.count(" ")
  letterE += R.count("e")
  total += len(R)
f.close()

percentageSpace = float(space)/total
percentageE = float(letterE)/total
print u"空白有%d個，比例為%.2f" %(space,percentageSpace);
print u"e有%d個，比例為%.2f" %(letterE,percentageE);