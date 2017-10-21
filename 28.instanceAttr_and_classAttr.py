# 实例属性-给实例绑定属性的方法是通过实例变量或self变量
# 类属性-直接在class中定义属性，这种属性归类所有，但类的所有实例都可以访问到

class Student(object):
  name = 'Student'
  age = 24
  def __init__(self, name):
    self.name = name

s = Student('zhangsan')
s.score = 55
print(s.name) # 'zhangsan'，因为s有name属性，所以不需要查找类的属性
print(s.age) # 24，因为s没有age属性，所以查找类的属性
