# 关键字参数,允许传入0或任意多个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def person(name, age, **kw):
	print('name:', name, '--- age:', age, '--- other:', kw)

person('zhangsan', 32)
person('lisi', 23, city = 'nanjing')
person('wangwu', 34, gender = 'M', job = 'programer')

extra = {'city': 'nanjing', 'job': 'taofen'}
person('mazi', 25, **extra)
