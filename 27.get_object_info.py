import types

# 判断基本数据类型
print(type(123) == int) # True
print(type('abc') == str) #True

# 判断对象是否是函数
def fn():
  pass
print(type(fn) == types.FunctionType) # True
print(type(abs) == types.BuiltinFunctionType) # True
print(type((x for x in range(10))) == types.GeneratorType) # True

# 判断class的类型，使用type很不方便，可以使用isinstance()函数
class Animal(object):
  pass

class Dog(Animal):
  pass

class Husky(Dog):
  pass

a = Animal()
d = Dog()
h = Husky()
print('---------')
print(isinstance(a, Animal)) # True
print(isinstance(h, Animal)) # True
print(isinstance(a, Husky)) # False

print('---------')

# 判断一个变量是否是某几个类型中的一个
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir(),获取一个对象的所有属性和方法
# 类似__xxx__的方法在Python中都有特殊用途，如__len__方法返回长度，当调用len()时，在len()内部事实上自动调用该对象的__len__方法
print(dir('abc'))
print('abc'.__len__())

# 操作一个对象的状态:getattr()、setattr()以及hasattr()
# 注：只有在不知道对象信息的时候，才需要获取对象信息，如果可以直接写obj.x，就不要写成getattr(obj, 'x')
class MyObject(object):
  def __init__(self):
    self.x = 5

  def fn(self):
    pass

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(getattr(obj, 'x'))
print(getattr(obj, 'fn'))
print(setattr(obj, 't', 666))
print(obj.t)
