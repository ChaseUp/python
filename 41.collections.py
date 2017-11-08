# namedtuple，创建一个自定义tuple对象且规定的tuple对象元素的个数，并可以用属性而非索引来引用某个tuple元素
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque：使用list存储数据时按索引访问元素很快，但插入和删除元素很慢，deque是为了高效的实现插入和删除的双向列表，适合用于队列和栈
# deque实现了append、appendleft、pop、popleft等方法
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict：使用dict时，如果引用的key不存在，就会抛出KeyError，如果希望key不存在时返回一个默认值，就可以使用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict：使用dict时，key是无序的，在对dict做迭代时无法确定key的顺序，如果要保持key的顺序，可以使用OrderedDict
# OrderedDict的key会按照插入时的顺序，而不是key本身的顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)
# OrderedDict 可以实现一个FIFO（先进先出）的dict，当容量超出时，先删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):
  def __init__(self, capacity):
    super(LastUpdatedOrderedDict, self).__init__()
    self._capacity = capacity

  def __setitem__(self, key, value):
    containsKey = 1 if key in self else 0
    if len(self) - containsKey >= self._capacity:
      last = self.popitem(last = False)
      print('remove', last)
    if containsKey:
      del self[key]
      print('set', (key, value))
    else:
      print('add', (key, value))
    OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(2)
luod['a'] = 1
luod['b'] = 2
luod['c'] = 3
print(luod)

# Counter是一个简单的计数器，例如统计字符出现的次数。Counter实际上是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programming':
  c[ch] = c[ch] + 1
print(c)
