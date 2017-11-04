import unittest
from mydict import Dict
# 以test开头的方法是测试方法，否则不被认为是测试方法，测试的时候不执行
# 对每一类测试编写一个test_xxx的方法，通过断言判断输出是否是期望的值，最常用的断言是assertEqual
# 另一种重要的断言是期待抛出指定类型的error,如通过d['empty']访问不存在的key时，断言会抛出KeyError,而通过d.empty访问不存在的key时，期待抛出AttributeError
# setUp与tearDown方法在每次调用一个测试方法前后分别被执行，测试需要连接数据库时使用较多

class TestDict(unittest.TestCase):
    def setUp(self):
        print('set up...')

    def tearDown(self):
        print('tear down...')

    def test_init(self):  
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(d, dict)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 通过以下方法执行测试，或输入命令行时加入额外参数，如python -m unittest mydict_test.py
if __name__ == '__main__':
    unittest.main()
