# 默认参数，必选参数在前，默认参数在后(变化大的参数在前，变化小的参数在后)，默认参数必须指向不变对象
def power(x, n = 2):
	sum = 1
	while n > 0:
		sum *= x
		n -= 1
	return sum

print(power(5))

# 若有多个默认参数，调用时即可按顺序提供默认参数，也可不按顺序提供部分默认参数
def enroll(name, gender, age = 6, city = 'nanjing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)

enroll('zhangsan', 'M', 7) # 按顺序排，不传第四个参数即city，使用默认值
enroll('lisi', 'M', city = 'beijing') # 指定city，age使用默认值
