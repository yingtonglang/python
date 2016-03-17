#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPrime(N):
  prime=1
  for i in range(2,N):
    if N%i==0:
	  prime =0
	  break
  return prime

sum = 0
for x in range(2,1001):
  if isPrime(x)==1:
    sum+=x
print sum