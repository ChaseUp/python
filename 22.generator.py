# 生成器(generator)-一边循环一遍计算的机制
# 创建generator最简单的方法：将一个列表生成式的[]改为()
l = [x * x for x in list(range(10))]
g = (x * x for x in list(range(10)))
print(l)
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
	print(i)

# 斐波那契数列,输出前max个数
def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		print(b)
		a, b, n = b, a + b, n + 1
	return('done')
fib(3)

# 将上述函数转为generator，只需将print换为yield
# generator和普通函数执行流程不一样，函数是顺序执行，遇到return或最后一行语句便返回；
# generator函数在每次调用next()时执行，遇到yield返回，再次执行时从上次返回的yield处继续执行
# 迭代器

def fib2(max):
	a, b, n = 0, 1, 0
	while n < max:
		yield(b)
		a, b, n = b, a + b, n + 1
	return('done')
print(fib2(3))

g = fib2(6)
while True:
	try:
		x = next(g)
		print(x)
	except StopIteration as e:
		print('generator return value:', e.value)
		break

print('-------------------------------')

# 杨辉三角形
def triangle(max):
	r, l = 1, [1]
	while r <= max:
		yield(l)
		l.append(0)
		l.insert(0, 0)
		l2, i = [], 0
		while i < len(l) - 1:
			l2.append(l[i] + l[i + 1])
			i += 1
		l = l2
		r += 1
	return 'done'

t = triangle(10)
while True:
	try:
		g = next(t)
		print(g)
	except StopIteration as e:
		print('generator return value:', e.value)
		break
