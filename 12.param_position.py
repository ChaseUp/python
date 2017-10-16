# 位置参数-调用函数时，传入的两个值按位置顺序赋给函数形参
def power(x, n):
	sum = 1
	while n > 0:
		sum *= x
		n -= 1
	return sum

print(power(4, 3))
