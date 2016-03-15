#!/usr/bin/env python
# -*- coding: utf-8 -*-

print u'請輸入一個數字:'
x = input()	
prime=1
for y in range(2,x):
  if x%y==0:
	prime =0
	print u'%d不是質數' %x;
	break
if prime==1:
  print u'%d是質數' %x;