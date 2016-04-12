#!/usr/bin/env python
# -*- coding: utf-8 -*-

class professor:
  words = u"我一點都不會介意"
  def specialty(self):
    print u"教授的專長是C語言和電腦網路"
    	
class student(professor):
  def specialty(self):
    print u"學生的專長是C語言和電腦網路"
  def hobby(self):
    print u"學生的興趣是python"

pro = professor()
stu = student()

pro.specialty()
stu.specialty()
stu.hobby()
print u"%s" %pro.words
print u"%s" %stu.words