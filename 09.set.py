# 一组key的集合(不能是可变的)，但不存储value，且key不可重复，重复元素自动被过滤
# 要创建set，需提供一个list作为输入集合
s = set([1, 2, 3])
print(s)

# 添加元素
s.add(4)
print(s)

# 删除元素
s.remove(1)
print(s)

# set可以看成数学意义上两个无序和无重复元素的集合，因此可以做交集并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2
s4 = s1 | s2
print('s1&2:', s3)
print('s1|2:', s4)
