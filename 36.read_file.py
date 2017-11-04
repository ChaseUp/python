# 文件读写时都有可能产生IOError，为了确保关闭文件，使用以下写法
try:
  f = open('./txt/test.txt', 'r')
  print(f.read())
finally:
  if f:
    f.close()

print('------')

# 更简洁的写法
with open('./txt/test.txt', 'r') as f:
  print(f.read())

print('------')

# 每次读取一行
with open('./txt/test.txt', 'r') as f:
  for line in f.readlines():
    print(line.strip())

print('------')

# 每次读取固定字节数
with open('./txt/test.txt', 'r') as f:
  print(f.read(4))

# file-like Object：像open函数返回的这种有个read()方法的对象。除了file外还可以是内存的字节流，网络流，自定义流等

print('------')

# 读取二进制文件，如图片、视频等，用'rb'模式打开
with open('./img/test.jpg', 'rb') as f:
  print(f.read(50))

# 写文件
with open('./txt/hello.txt', 'w') as f:
  f.write('hello world!')
