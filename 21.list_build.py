# 列表生成器
import os
# 生成列表[1 * 1, 2 * 2, ..., 10 * 10]
l1 = [x * x for x in range(1, 11)]
print(l1)

# 生成列表[2 * 2, 4 * 4, ..., 10 * 10]
l2 = [x *x for x in range(1, 11) if x % 2 == 0]
print(l2)

# 使用两个变量
l3 = [k + '=' + v for k, v in {'a': '1', 'b': '2'}.items()]
print(l3)

# 双重循环
l4 = [m + n for m in 'ABC' for n in 'xyz']
print(l4)

# 将字符串变成小写
l5 = [s.lower() for s in ['Hello', 'Python']]
print(l5)

# 列出当前目录下所有文件和目录名
d = [d for d in os.listdir('.')]
print(d)
