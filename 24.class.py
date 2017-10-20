# 类和实例

class Student(object):
  # 类中的函数第一个参数永远都是self，且调用时不需传入该参数
  def __init__(self, name, score ):
    self.name = name
    self.score = score

  # 封装方法，外部直接调用，不需知道实现细节
  def print_score(self):
    print('%s: %s' % (self.name, self.score))

  def get_grade(self):
    if self.score >= 80:
      return 'A'
    elif self.score >= 60:
      return 'B'
    else:
      return 'C'

s1 = Student('zhangsan', 3)
s1.print_score()
print(s1.get_grade())
    