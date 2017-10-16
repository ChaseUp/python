# 有序数据集合-列表
l = ['zhangsan', 'lisi', 'wangwu']

print(l[1])
print(l[-1]) # 取倒数第一个
print(len(l))

l.append('mazi') # 末尾添加
print(l)

l.insert(1, 'Jack') # 向索引1的位置添加
print(l)

l.pop() # 删除末尾元素
print(l)

l.pop(1) # 删除指定位置元素
print(l)
