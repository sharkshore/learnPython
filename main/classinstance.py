#类实例

class MyClass:
	"一个简单的类实例"
	i=12345
	def __init__(self):
		self.data=[1,3,5]
	def f(self):
		return "hello,world"

x=MyClass()
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


class Complex:
	def __init__(self,r,i):
		self.r=r
		self.i=i

class Child(MyClass,Complex):
	pass
