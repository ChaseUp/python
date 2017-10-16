# 组合参数，组合使用5种参数，顺序必须为位置参数、默认参数、可变参数、命名关键字参数、关键字参数

def f1(a, b, c = 0, *args, **kw):
	print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'kw:', kw)

def f2(a, b, c = 0, *, d, **kw):
	print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)

f1(1, 2)
f1(1, 2, 3, 4, 44)
f1(1, 2, 3, 4, 44, d = 5, e = 6)

f2(1, 2, d = 'ddd')
f2(1, 2, d = 'ddd', e = 'eee', f = 'fff')
