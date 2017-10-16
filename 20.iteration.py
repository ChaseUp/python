# 迭代-只要是可迭代对象，都可进行迭代
from collections import Iterable

for ch in 'abcd':
	print(ch)

d = {'a': '111', 'b': '222'}
for i in d:
	print(i, ':', d[i])

# dict的items()同时迭代key和value
for k, v in d.items():
	print(k, '=', v)

# 判断对象是否可迭代
print(isinstance('abc', Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance({'a': 'aa', 'b': 'bb'}, Iterable))
print(isinstance(12.34, Iterable))

for i, value in enumerate(['a', 'aa', 'b', 'bb']):
	print(i, value)
