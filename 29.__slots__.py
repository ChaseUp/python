# __slots__-限制实例的属性，__slots__只对当前类有效，对子类无效，除非在子类中也定义__slots__，则子类的__slots__为自身的加父类的
# 正常情况下，创建一个class实例后，可以给任何实例绑定属性和方法，这就是动态语言的灵活性
from types import MethodType
class Student(object):
  __slots__ = ('name', 'set_age', 'age', 'score') # 用tuple定义允许绑定的属性名称

s1 = Student()
# 添加属性
s1.name = 'zhangsan'
# 添加方法,注：给一个实例绑定方法，对另一个实例是不起作用的
def setage(self, age): # 定义函数作为实例方法
  self.age = age

s1.set_age = MethodType(setage, s1) # 给实例绑定一个方法
s1.set_age(25)
print(s1.age)

# 动态给类添加方法，所有实例都可以调用该方法
def set_score(self, score):
  self.score = score
Student.set_score = set_score

s2 = Student()
s2.set_score(89)
print(s2.score)
