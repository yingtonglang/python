#!/usr/bin/env python
# -*- coding: utf-8 -*-

deposit = 5000
print u'請輸入取款金額:'
money = input ()

f = open("ATM.txt","w")

if (deposit-money)<0 :
  print u'您的餘額不足!'
  f.write('您的餘額不足!')
elif (deposit-money)==0 :
  print u'您的存款無剩餘存款'
  f.write('您的存款無剩餘存款')
else:
  print u'您的存款還剩%d元' %(deposit-money)
  f.write('您的存款還剩%d元' %(deposit-money))
  
f.close()