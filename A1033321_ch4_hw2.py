#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
count = 1
min = 0
max = 100
x = random.randint(1,99)
print u'終極密碼Start!!!'
print u'請輸入你猜的數字>>'
n = input()
while n!=x:
  if n>max:
    print u'你輸入的數字超過最大值，現在範圍是%d~%d' %(min,max)
    print u'請輸入你猜的數字>>'
    n = input()
  elif n<min:
    print u'你輸入的數字小於最小值，現在範圍是%d~%d' %(min,max)
    print u'請輸入你猜的數字>>'
    n = input()
  elif n>x:
    max=n
    print u'現在範圍是%d~%d' %(min,max)
    print u'請輸入你猜的數字>>'
    n = input()
  elif n<x:
    min=n
    print u'現在範圍是%d~%d' %(min,max)
    print u'請輸入你猜的數字>>'
    n = input()
  count+=1
print u'恭喜你猜中!終極密碼是%d,你花了%d次猜中。' %(x,count)