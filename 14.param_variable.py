# 可变参数，参数个数可以为0,1,2…
# 参数numbers接收到的是一个tuple
def calc(*numbers):
	sum = 0
	for i in numbers:
		sum += i * i
	return sum

print(calc(1, 2, 3, 4))

# 已有的list或tuple转为可变参数
l = [5, 6, 7]
print(calc(*l))
