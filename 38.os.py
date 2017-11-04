# 内置的os模块可以直接调用操作系统提供的接口函数
import os
# 查看操作系统
print(os.name)
# 查看环境变量
print(os.environ)
# 查看具体某个环境变量
print(os.environ.get('PATH'))

# 操作文件和目录
# 查看当前目录的决定路径
print('path:', os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
test_dir = os.path.join(os.path.abspath('.'), 'testdir')
# 创建目录
os.mkdir(test_dir)
# 删除目录
os.rmdir(test_dir)

# 注：
# 两个路径合成一个路径时不能用字符串拼接，应使用os.path.join()方法，这样可以正确处理不同操作系统下的路径分隔符
# 同理，拆分路径时也应使用os.path.split()方法，这样可以将路径拆分为两部分，后一部分总是最后级别的目录或文件名
# os.path.splitext()可以直接得到文件的扩展名，如 os.path.splitext('\it\python\txt\test.txt') >>> ('\it\python\txt', '.txt')
# 文件重命名 os.rename('test.txt', 'test.py')
# 删除文件 os.remove('test.py')
# os模块没有复制文件的接口，可以使用shutil模块

# 列出当前目录下的所有目录
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出当前目录下的所有py文件
pys = [x for x in os.listdir('.') if os.path.isdir(x) and os.path.splitext(x)[1] == '.py']
print(dirs)
print(pys)
