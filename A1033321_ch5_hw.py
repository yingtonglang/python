#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
print u'請輸入您的會員卡號:',
cardid = raw_input()

while re.findall(r"[A-Z]-{1}\d{6}",cardid)==[]:
  print u'您輸入的卡號有誤，請重新輸入:'
  cardid = raw_input()
  
if re.findall(r"E-056790",cardid)!=[]:
  print u'恭喜您中了10萬元!!!'

elif re.findall(r"E-\d56790",cardid)!=[]:
  print u'恭喜您中了2萬元!!'
	
elif re.findall(r"[A-Z]-\d{3}790",cardid)!=[]:
  print u'恭喜您中了100元購物禮券!'
  
else:
  print u'銘謝惠顧'