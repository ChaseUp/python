# 访问限制-类中以'__'开头的属性属于私有属性，外部无法访问，事实上私有属性被python解释器改为了_Student.__name，外部可以这样访问，但强烈不建议这么做

class Student(object):
  def __init__(self, name, score):
    self.__name = name
    self.__score = score

  def get_name(self):
    return self.__name

  def get_score(self):
    return self.__score

  # 通过内部方法设值，可以对输入进行校验
  def set_score(self, score):
    if type(score) == int and 0 <= score <= 100:
      self.__score = score
    else:
      print('score value is not legal.')

s1 = Student('zhangsan', 5)
# print(s1.__score) 报错，私有属性外部无法访问
print(s1._Student__name) # 可以访问，但不建议这么做
print(s1.get_score())
s1.set_score(34)
print(s1.get_score())
s1.set_score('34')
    