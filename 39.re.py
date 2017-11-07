# 正则表达式
# \d可以匹配一个数字，\w可以匹配一个数字或字母，如'00\d'可以匹配'007'，'\w\w\d'可以匹配'py3'
# .可以匹配任意字符，如'py.'可以匹配'py3'、'py!'
# 匹配变长的字符：*匹配任意多个字符，包含0个；+匹配一或多个字符；?匹配0或1个字符；
#   {n}匹配n个字符，如'\d{3}\s+\d{3,8}'，匹配任意多个空格隔开的带三位区号的电话号码，注意3和8中间逗号两边不能有空格
# []表示范围，[0-9a-zA-Z\_]，匹配一个数字字母或下划线，[0-9a-zA-Z\_]+匹配一或多个数字字母下划线
# [a-zA-Z\_][0-9a-zA-Z\_]*匹配以字母或下划线开头，后接任意个由数字字母下划线组成的字符串，即Python的合法变量
# A|B可以匹配A或B，(p|P)ython可以匹配'python'或'Python'
# ^表示开头，$表示结尾，py可以匹配'python'，^py$只能匹配'py'
import re
num = '101-3845432'
if re.match(r'\d{3}\-\d{3,8}', num):
  print('is tel number.')
else:
  print('is not tel number.')

# 切分字符串
str1 = re.split(' ', 'a b  c')
str2 = re.split(r'\s+', 'a b  c')
print(str1)
print(str2)

# 提取子串，用()表示要提取的分组(Group)
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-3545644')
print(m.group(0), m.group(1), m.group(2))
