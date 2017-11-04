# 在内存中读写
from io import StringIO
from io import BytesIO

# StringIO只能操作str
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# 可以用一个str初始化StringIO，然后像读文件一样读取
f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

# 如果要操作二进制数据，要使用BytesIO
fb = BytesIO()
fb.write('中文'.encode('utf-8'))
print(fb.getvalue())
