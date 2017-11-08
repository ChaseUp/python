# 常见的摘要算法有MD5、SHA1等，通过一个函数，把任意长度的数据转换为一个长度固定的数据串(通常用16进制的字符串表示)
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 若数据量很大，可以分多次调用update
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 其他更安全的算法有sha256和sha512等，但越安全的算法不仅越慢，而且摘要长度更长
