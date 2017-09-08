#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'BF100395'
__mtime__ = '2017/9/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

#函数定义
"""
def area(width,height):
	return width*height

def print_welcom(name):
	print("welcome",name)

print_welcom('shark')

print('面积:',area(2,5))
"""

#不可变对象
"""
def ChangeInt(a):
	a=10
b=2
ChangeInt(b)
print(b)
"""

#可变对象
"""
def changeList(mylist):
	"修改传入的列表"
	mylist.append([1,2,3,4])
	print('函数内取值:',mylist)
	return
mylist=[4,5,6,7]
changeList(mylist)
print(mylist)

"""

#必须参数
"""
def printme(str):
	"打印任何传入的字符串"
	print(str)
	return
printme()

"""
#关键字参数

"""
def printinfo(name,age):
	"打印任何传入的参数"
	print('名字',name)
	print('年龄',age)

printinfo(age=22,name='xiaoming')

"""
"""
def printinfo(name,age=33):
	"打印任何传入的字符串"
	print ("名字: ", name);
	print ("年龄: ", age);

printinfo('xiaoming',55)
print("--------------------------")
printinfo('heihei')

"""

#不定长参数

"""
def printinfo(arg1,*arg2):
	"打印任何传入的参数"
	print('输出:')
	print(arg1)
	print(arg2)
	for v in arg2:
		print(v)
	return

printinfo(10)
printinfo(70,60,50)
"""


#匿名函数
"""
sum=lambda arg1,arg2:arg1+arg2+arg2*arg1
print('相加后的值',sum(10,20))
print('相加后的值',sum(20,30))
"""

#return语句
def sum(arg1,arg2):
	"返回2个参数的和"
	total=arg1+arg2
	print('函数体内:',total)
	return total

total=sum(10,20)
print('函数外',total)



