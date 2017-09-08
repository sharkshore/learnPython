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


#if
"""
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age<0:
	print("你是在逗我吧!")
elif age==1:
	print("相当于 14 岁的人。")
elif age==2:
	print("相当于 22 岁的人。")
elif age>2:
	human=22+(age-2)*5
	print("对应人类年龄: ", human)

"""

#if嵌套

"""
num=int(input("输入一个数字:"))
if num%2==0:
	if num%3==0:
		print("你输入的数字可以整除 2 和 3")
	else:
		print ("你输入的数字可以整除 2，但不能整除 3")
else:
	if num%3==0:
		print ("你输入的数字可以整除 3，但不能整除 2")
	else:
		print  ("你输入的数字不能整除 2 和 3")

"""

#while
"""
n=100
sum=0
counter=1
while counter<= n:
	sum=sum+counter
	counter+=1

print("1 到 %d 之和为: %d" % (n,sum))

"""

#while,else
"""
count=0
while count<5:
	print("count","小于5")
	count+=1
else:
	print(count,"大于或等于5")
	
"""

#简单语句组
"""
flag=1
while(flag):print('欢迎访问')
print("goodbye")


languages=['C','C++','Perl','Python']
for x in languages:
	print(x)

"""
#for循环示例

"""
sites = ["Baidu", "Google","Runoob","Taobao"]
for s in sites:
	if s=='2Baidu':
		print('菜鸟')
		break
	print("循环数据"+s)
else:
	print('没有循环教程')
print('完成循环')

"""

#range
# for i in range(5):
# 	print(i)

# for k in range(5,9):
# 	print(k)

# for j in range(5,50,3):
# 	print(j)

# ls=list(range(5,50,3))
# nls=[i**3 for i in ls]
# print(nls)

#pass

"""
for letter in 'Runoob':
	if letter =='o':
		pass
		print('执行pass块')
	print('当前字母',letter)
print('Goodbye')

"""

