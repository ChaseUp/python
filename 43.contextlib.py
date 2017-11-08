# 任何对象，只要正确使用了上下文管理，就可以用于with语句
# 读写文件资源必须在使用完毕后正确关闭它们
try:
    f = open('./txt/test.txt', 'r')
    f.read()
finally:
    if f:
        f.close()
# 使用with语句
with open('./txt/test.txt', 'r') as f:
    f.read()

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s' % self.name)

with Query('Bob') as q:
    q.query()

# @contextmanager：__enter__和__exit__仍然很繁琐，contextlib提供了更简单的方法
from contextlib import contextmanager
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s' % self.name)

@contextmanager
def create_query2(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')

with create_query2('Tom') as q:
    q.query()
        
# @closing：如果一个对象没有上下文对象，可以用closing()将该对象变为上下文对象。例如用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

# closing也是一个经过@contextmanager装饰的generator,这个generator编写如下
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
