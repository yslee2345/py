# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:02:43 2017

@author: stu
"""


# rpad 구현

def rpad(string, space, string_2):
    if space - len(string) >= 1:
        for i in range(space - len(string)):
            string = string + string_2
        return string
    else:
        return string[0:space]


# rpad 구현2 - Good Coding

def rpad2(string, space, string_2):
    return string + string_2 * (space - len(string))


print(rpad2('abcde', 10, '*'))


# lpad 구현
def lpad(string, space, string_2):
    if space - len(string) >= 1:
        for i in range(space - len(string)):
            string = string_2 + string
        return string
    else:
        return string[0:space]


print(lpad('abcde', 10, '*'))


# instr
def instr(string, target_string):
    for i in range(len(string)):
        if string[i] == target_string:
            return i + 1
    return 0


print(instr('ename', 'a'))

import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], instr(emp_list[1], 'N'))

# months_between 구현
import datetime

a = datetime.datetime.strptime('1991-12-08', '%Y-%m-%d')
b = datetime.datetime.strptime('1992-01-08', '%Y-%m-%d')
c = b - a

print(c.days)


# nvl구현
def nvl(str1, str2):
    if str1 == None:
        return str2
    return str1


print(nvl(None, '000'))


# decode 구현
def decode(str1, str2, retrn1, retrn2):
    if str1 == str2:
        return retrn1
    return retrn2


import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[2], decode(emp_list[2], 'SALESMAN', '세일즈맨', '기타'))

# 번역기
dic = {}
dic['나는'] = ('I', 0)
dic['소년'] = ('boy', 2)
dic['이다'] = ('am', 1)
dic['피자를'] = ('pizza', 2)
dic['먹는다'] = ('eat', 1)
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)):
    for j in input_list:
        if dic[j][1] == i:
            result = result + dic[j][0] + ' '
print(result)

# 행을 뽑아내서 하는 방법

import csv

emp_csv = csv.reader(open(r"D:\data\emp_comm.csv"))
emp_dic = []
seq = 1
for i in emp_csv:
    emp_dic.append({i})
    if seq == 1:
        break

for i in emp_csv:
    emp_dic.append({'deptno': i[0], 'dname': i[1], 'loc': i[2]})

for i in emp_dic:
    print(i['deptno'], i['dname'], i['loc'])


class Fruit(object):
    """다양하고 맛있는 과일을 생성하는 클래스."""

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor, self.poisonous))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")


lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# 다익스트라 알고리즘
arr_distance = [[0, 5, 10, 9, 999, 999, 999],
                [5, 999, 3, 999, 999, 11, 999],
                [10, 3, 999, 7, 3, 10, 999],
                [9, 999, 7, 999, 999, 7, 12],
                [999, 999, 3, 999, 999, 999, 999],
                [999, 11, 10, 7, 4, 999, 2],
                [999, 999, 999, 12, 999, 2, 999]
                ]



