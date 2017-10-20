# 继承-子类自动继承父类的属性和方法
# 多态-子类和父类存在相同的属性，子类覆盖父类的属性

class Animal(object):
  def run(self):
    print('Animal is running.')

class Dog(Animal):
  def eat(self):
    print('Dog is eating.')

class Cat(Animal):
  def run(self):
    print('Cat is running.')

d1 = Dog()
c1 = Cat()

d1.run()
c1.run()
    