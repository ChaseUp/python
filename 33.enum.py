# 枚举类-Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
  print(name, '=>', member, ':', member.value) # value属性是自动赋值给成员的int类型常量，默认从1开始

# 若要精确控制枚举类型，可从Enum派生出自定义类
@unique # 装饰器可以帮助检查，确保没有重复值
class Weekday(Enum):
  Sun = 0 # Sun的value被设为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

# 访问这些枚举类有若干种方法
day1 = Weekday.Mon
print(day1) # Weekday.Mon
print(Weekday.Tue) # Weekday.Tue
print(Weekday['Fri']) # Weekday.Fri
print(Weekday.Sat.value) # 6
print(Weekday(1)) # Weekday.Mon
