names = ['zhangsan', 'lisi', 'wangwu']
for name in names:
	if name == 'lisi':
		continue # 循环中使用break和continue，while循环中同样适用
	print(name)

l = list(range(101)) # 通过range函数生成0-100的整数序列，再通过list函数将其转为list
sum = 0
for i in l:
	sum += i
print(sum)
