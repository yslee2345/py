# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:27:14 2017

@author: stu
"""

def rec_fact(count):
    if count > 0:
        return count * rec_fact(count - 1)
    elif count == 0:
        return 1


rec_fact(10)