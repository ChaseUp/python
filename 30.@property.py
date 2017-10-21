# 既能检查参数，又能用类似属性这样简单的方法访问类的变量
class Student(object):
  @property # 将一个getter方法变为属性，同时创建@scroe.setter装饰器，将一个setter方法变为属性，get和set都可以通过属性的方式访问了
  def score(self):
      return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer.')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 and 100.')
    self._score = value

s = Student()
s.score = 34 # 实际转化为s.set_score()
print(s.score)  # 实际转化为s.get_score()

print('------')
# 还可以定义只读属性
class Person(object):
  @property
  def birth(self):
      return self._birth
  
  @birth.setter
  def birth(self, value):
    if not isinstance(value, int):
      raise ValueError('birth must be an integer.')
    if value < 0:
      raise ValueError('birth must more than 0.')
    self._birth = value

  @property
  def age(self):
      return 2017 - self._birth

p = Person()
p.birth = 1990
print(p.age)
