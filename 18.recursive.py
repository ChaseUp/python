# 递归，理论上所有的递归都能写成循环，但递归定义简单逻辑清晰
# n的阶乘，非递归写法
def fact(n):
	sum = 1
	while n > 1:
		sum *= n
		n -= 1
	return sum

# n的阶乘，递归写法
def fact2(n):
	if n > 1:
		return n * fact2(n - 1)
	else:
		return 1

print(fact(5))
print(fact2(5))

# 函数调用通过栈（stack）这种数据结构实现，每进入一个函数调用，栈就会加一层栈帧，每当函数返回，就会减少一层栈帧，因此递归调用过多就会导致栈溢出
# 解决方法是尾递归优化，尾递归指函数返回时调用自身，且return语句不能包含表达式，这样编译器或解释器就会进行尾递归优化，始终只占用一个栈帧
# 大部分编程语言没有针对尾递归优化，Python也是
def fact3(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print(fact3(6))
