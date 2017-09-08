#python3数据结构

#列表当做堆栈
#append从尾端添加,pop从尾端弹出
'''
stack=[3,4,5]
stack.append(6)
stack.append(7)
print("第一次打印",stack)
stack.pop()
print("第一次弹出后",stack)
stack.pop()
print("第二次弹出后",stack)
'''


#列表当做队列
#append从尾端添加,popleft从首端弹出
"""
from collections import  deque
queue=deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
first=queue.popleft()
print("弹出的第一个",first)
print(queue)
second=queue.popleft()
print("弹出的第二个",second)
print(queue)

"""

#列表推导式

"""
vec=[2,4,5]
one_vec=[3*x for x in vec]
print(one_vec)

two_vec=[[x,x**2] for x in vec]
print(two_vec)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
one_freshfruit=[weapon.strip() for weapon in freshfruit]
print(one_freshfruit)


ifstatement=[ x**3 for x in vec if x>3]
print("ifstatement",ifstatement)

vec1=[2,4,6]
vec2=[4,3,-9]
vec_tall=[x*y+x+y for x in vec1 for y in vec2]
print("vec_tall",vec_tall)
vec_altogether=[vec1[i]*vec2[i] for i in range(len(vec1))]
print("vec_altogether",vec_altogether)

roustr=[str(round(355/113,i)) for i in range(1,6)]
print(roustr)

"""

#嵌套列表解析

"""
matrix=[
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]

tr_one=[ [ row[i] for row in matrix] for i in range(4)]
print(tr_one)

"""

#del语句
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
del a[2:4]
print(a)

"""

#元组和序列

"""
t=12345,54321,'hello'
print(t[0])
print(t)

"""


#集合set
"""
a = set('abracadabra')
b = set('alacazam')
print(a-b)
print(a&b)
"""

#字典

"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
print(tel)
lis=list(tel.keys())
print(lis)
value1=[tel[i] for i in list(tel.keys())]
print(value1)
print('guido' not in tel)

dict_one=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('dict',dict_one)

dict_two={x:x**2 for x in (2,4,5)}
print('dict_two',dict_two)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k,v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
	print('What is your {0}?  It is {1}.'.format(q, a))

"""

#反向遍历

# for i in reversed(range(1,10,2)):
# 	print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(basket):
	print(f)

