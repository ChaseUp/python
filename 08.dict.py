# 字典-dict（map结构），key不能是可变的，与list相比，数据无序，查找速度快，占用内存大
d = {'zhangsan': 12, 'lisi': 98, 'wangwu': 100}
print(d['zhangsan'])

### key不存在会报错，避免方式有两种
# 1.判断存在再操作
if 'mazi' in d:
	print(d['mazi'])
else:
	print('mazi is not exist in d.')

# 2.第二个参数表示默认返回值，不代表复制，并不改变原有dict
print(d.get('mazi', 0))

# 删除某项值
d.pop('zhangsan')
print(d)
