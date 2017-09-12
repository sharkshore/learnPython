class people:
	name=''
	age=0
	_weight=0
	def __init__(self,name,age,weight):
		self.name=name
		self.age=age
		self._weight=weight
	def speak(self):
		print("%s 说: 我 %d 岁。" %(self.name,self.age))


#单继承示例
class student(people):
	grade = ''
	def __init__(self,n,a,w,g):
		#调用父类的构函
		people.__init__(self,n,a,w)
		self.grade = g
	#覆写父类的方法
	def speak(self):
		print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

class speaker:
	topic=''
	name=''
	def __init__(self,n,t):
		self.name = n
		self.topic = t
	def speak(self):
		print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(student,speaker):
	a=''
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)

