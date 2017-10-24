# 定制类-形如__xxx__的变量或函数在Python中都有特殊的用途
# __str__，打印实例，更直观的展示实例信息及其内部重要数据
# __repr__，不用print，命令行中直接输入实例即可展示直观信息
class Student(object):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return 'Student object (name: %s)' % self.name

  __repr__ = __str__

s = Student('zhangsan')
print(s)
s

# __iter__返回一个迭代对象，可用于for循环，循环不断调用__next__方法，直到遇到StopIteration
class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1 # 定义两个计数器

  def __iter__(self):
    return self # 实例本身就是迭代对象，故返回自己

  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 1000:
      raise StopIteration()
    return self.a # 返回下一个值

for n in Fib():
  print(n)

print('-----------')
# __getitem__，根据索引获取元素
class Fib2(object):
  def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
      a, b = b, a + b
    return a

f = Fib2()
print(f[3])

# __getattr__，正常情况下，调用不存在的属性时会报错，通过__getattr__()方法，可以动态的返回属性，当调用的属性不存在时，解释器会调用__getattr__尝试获取
class Student2(object):
  def __init__(self, name):
    self.name = name

  def __getattr__(self, attr):
    if attr == 'score':
      return 45
    raise AttributeError('\'Student2\' object has no attribute \'%s\'' % attr) # 省略该句则访问任何不存在的属性将会返回None
    
s2 = Student2('zhangsan')
print(s2.name)
print(s2.score)

# __call__，在实例本身上调用方法
class Student3(object):
  def __init__(self, name):
    self.name = name

  def __call__(self):
    print('my name is %s' % self.name)
    
s3 = Student3('zhangsan')
s3()
# 如此便模糊了对象与函数的界限，通过callable判断一个对象是否是可调用对象，
print(callable(Student('zhangsan')))
print(callable(Student3('zhangsan')))
