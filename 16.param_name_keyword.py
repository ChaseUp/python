# 命名关键字参数，限制关键字参数的名字，只接收city和job作为关键字参数
# 分隔符*后面的参数视为命名关键字参数
def person(name, age, *, city, job):
	print(name, age, city, job)

#若函数中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name, age, *args, city, job):
	print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，否则将被视为位置参数
person('zhangsan', 23, city = 'nanjing', job = 'taofen')
