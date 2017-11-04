import logging
# try except-错误处理，最大的好处是可以跨域多层调用比如main()调用foo()，foo()调用bar(),此时bar出错了，只要main捕获到就可以处理
# 即不需要在每个可能出错的地方去捕获错误，只要在合适的层次捕获就可以了
try:
  print('try...')
  r = 10 / 0
  print('result: %s' % r)
except ValueError as e:
  print('except: %s' % e)
except ZeroDivisionError as e:
  print('except: %s' % e)
else:
  print('no error')
finally:
  print('finally...')
print('end.')
print('-----------------')

# 记录错误：如果不捕获错误，可以让Python解释器打印错误堆栈，但程序也被结束了
# 使用内置logging模块可以很容易的记录错误信息，既能捕获错误并打印，且可以让程序继续执行下去
def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
    bar('0')
  except Exception as e:
    logging.exception(e)

main()
print('END')
print('---------------')

# 抛出错误：当前函数不知道如何处理错误时，通过raise向上抛出错误，让上层调用者处理，上层调用者不知道如何处理，继续上抛，直至顶层调用者
def foo2(s):
  n = int(s)
  if n == 0:
    raise ValueError('invalid value %s' % s)
  return 10 / n

def bar2():
  try:
    foo2('0')
  except Exception as e:
    print('ValueError')
    raise

bar2()
