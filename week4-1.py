#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 1
i = 0
for x in range(1,56):
  if i<count:
	print x,
	i=i+1;
  elif i==count:
	print '\n'
	print x,
	count = count+1;
	i = 1;