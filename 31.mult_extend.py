# 多重继承-假设四种动物：dog(狗) bat(蝙蝠) parrot(鹦鹉) ostrich(鸵鸟)，以类设计可以分为：mammal(哺乳类) bird(鸟类);runnable flyable;宠物类 非宠物类等等
# 正确的设计:
# 大类
class Animal(object):
  pass

class Mammal(Animal):
  pass

class Bird(Animal):
  pass

class Runnable(Animal):
  def run(self):
    print('running...')

class Flyable(Animal):
  def fly(self):
    print('flying...')

# 各种项目类
class Dog(Mammal, Runnable):
  pass
    
class Bat(Mammal, Flyable):
  pass    
