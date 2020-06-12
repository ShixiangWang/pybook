x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
temp = x
x = y
y = temp
def func():
    a = 1
    b = 2
    c = 3
    return a, b, c

# 序列解包操作：
# 将函数结果直接赋值到多个变量中
# 按顺序一一对应
# d <- a
# e <- b
# f <- c
d, e, f = func()
# 获取一个元组结果
tup_res = func()
# 分别赋值
d = tup_res[0]
e = tup_res[1]
f = tup_res[2]
In [1]: a = 10
In [2]: assert a > 10
---------------------------------------------------------------------
AssertionError                      Traceback (most recent call last)
<ipython-input-2-92ef20669630> in <module>
----> 1 assert a > 10

AssertionError:

In [3]: assert a > 10, 'a 不大于 10'
---------------------------------------------------------------------
AssertionError                      Traceback (most recent call last)
<ipython-input-3-d19bab11044a> in <module>
----> 1 assert a > 10, 'a 不大于 10'

AssertionError: a 不大于 10
In [4]: print(", ".join(["spam", "eggs", "ham"]))  # 字符串拼接
spam, eggs, ham
In [5]: print("Hello ME".replace("ME", "wrold"))   # 字符串替换
Hello wrold
In [6]: print("This is a sentence.".startswith("This"))  # 判断字符串是否以 This 起始
True
In [7]: print("This is a sentence.".endswith("sentence."))  # 判断字符串是否以 sentence. 结束
True
In [8]: print("This is a sentence.".upper())  # 字母全部转换为大写
THIS IS A SENTENCE.
In [9]: print("THIS IS A SENTENCE.".lower())  # 字母全部转换为小写
this is a sentence.
In [10]: print("spam, eggs, ham".split())  # 字符串拆分
['spam,', 'eggs,', 'ham']
In [11]: x = 1
In [12]: scope = vars()
In [13]: scope['x']
# Out[13]: 1
In [14]: scope['x'] += 2
In [15]: scope['x']
# Out[15]: 3
In [16]: type(scope)
# Out[16]: dict
In [26]: a = 10
In [27]: def masking():
    ...:     a = 1
    ...:     print(a)
    ...:     los = locals()
    ...:     glo = globals()
    ...:     print(los['a'])
    ...:     print(glo['a'])
    ...:

In [28]: masking()
1
1
10
In [36]: a = 10
In [37]: def change_global():
    ...:     global a
    ...:     a = 5
    ...:

In [38]: change_global()
In [39]: a
# Out[39]: 5
In [40]: exec("print('Hello world')")
Hello world
In [41]: from math import sqrt
In [42]: exec('sqrt = 1')
In [43]: sqrt(4)
---------------------------------------------------------------------
TypeError                           Traceback (most recent call last)
<ipython-input-43-317e033d29d5> in <module>
----> 1 sqrt(4)

TypeError: 'int' object is not callable
In [44]: scope = {}
In [45]: exec('sqrt = 1', scope)
In [46]: scope['sqrt']
    ...: 1
# Out[46]: 1
In [47]: eval('sqrt = 1')
Traceback (most recent call last):

  File "/home/shixiang/miniconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3326, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)

  File "<ipython-input-47-e7321eeaf096>", line 1, in <module>
    eval('sqrt = 1')

  File "<string>", line 1
    sqrt = 1
         ^
SyntaxError: invalid syntax

In [48]: eval('sqrt + 3')
# Out[48]: 4
In [48]: eval('sqrt + 3')
# Out[48]: 4
In [49]: scope = {}
In [50]: scope['x'] = 3
In [51]: scope['y'] = 5
In [52]: eval('x * y', scope)
# Out[52]: 15
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("完成计算！")
except ZeroDivisionError:
    print("因为除以 0 导致错误！")
try:
    var = 10
    print(var + "hello")
    print(var / 2)
except ZeroDivisionError:
    print("除数为0！")
except (ValueError, TypeError):
    print("错误发生了！")
try:
    wd = "hello world"
    print(wd / 0)
except:
    print("发生了一个错误")
try:
    print("Hello World!")
    print(1 / 0)
except: ZeroDivisionError:
    print("不能被0整除！")
finally:
    print("无论上面干啥，我都会运行！")
print(1)
raise ValueError
print(2)
name = '123'
raise NameError("Invalid name!")
try:
    5 / 0
except:
    print("发生了一个异常")
    raise
def do_twice(func, args):
    return fun(func(args))

def add_two(x):
    return x + 2

print(do_twice(add_two, 1))
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
# Pure function
def pure_func(x, y):
    return x + y * x

# Impure function
# 这个函数改变了 a_list 的状态
# 所以不是纯函数
a_list = []
def impure_func(args):
    a_list.append(args)
double = lambda x: x * 2
print(double(4))
In [54]: def double(x):
    ...:     return x * 2
    ...:
    ...: data = [11, 22, 33, 44]
    ...: res = map(double, data)
    ...: print(list(res))
    ...:
[22, 44, 66, 88]
In [55]: print(list(map(lambda x: x* 2, data)))
[22, 44, 66, 88]
In [56]: list(filter(lambda x: x % 2 == 0, data))
# Out[56]: [22, 44]
In [3]: from functools import reduce
In [4]: def add(x, y):
   ...:     return x+y
   ...:

In [5]: reduce(add, [1,2,3,4,5])
# Out[5]: 15
In [22]: for i in count(11):
    ...:     print(i)
    ...:     if i > 20:
    ...:         break
    ...:
11
12
13
14
15
16
17
18
19
20
21
In [23]: from itertools import chain, takewhile, accumulate
In [24]: list(chain(list(range(1,5)), list(range(6,10))))
# Out[24]: [1, 2, 3, 4, 6, 7, 8, 9]
In [25]: nms = list(accumulate(range(20)))
In [26]: nms
# Out[26]:
[0,
 1,
 3,
 6,
 10,
 15,
 21,
 28,
 36,
 45,
 55,
 66,
 78,
 91,
 105,
 120,
 136,
 153,
 171,
 190]
In [27]: print(list(takewhile(lambda x: x <= 10, nms)))
[0, 1, 3, 6, 10]
In [1]: def range2(i):
   ...:     while i > 0:
   ...:         yield i
   ...:         i -= 1
   ...:
In [2]: for x in range2(9):
   ...:     print(x)
   ...:
9
8
7
6
5
4
3
2
1
In [3]: range2(9)
# Out[3]: <generator object range2 at 0x7fde103f1f50>
In [4]: range(1, 10)
# Out[4]: range(1, 10)
In [5]: list(range(1, 10))
# Out[5]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [6]: list(range2(9))
# Out[6]: [9, 8, 7, 6, 5, 4, 3, 2, 1]
def range2(i):
    while i > 0:
        yield i
        i -= 1
In [7]: a = range2(10)
In [8]: next(a)
# Out[8]: 10
In [9]: next(a)
# Out[9]: 9
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # 循环直到文件尾部
    while True:
        data = file_object.readline()
        if not data:
            break
        # 生成数据行
        yield data

with open('xxx.csv') as file:
    gen_file = read_large_file(file)

    # 打印文件的第一行
    print(next(gen_file))
import pandas as pd
df_reader = pd.read_csv('xxx.csv', chunksize=10)
print(next(df_reader))
In [16]: def add_text(func):
    ...:     def wrap():
    ...:         print("== This is head of function ==")
    ...:         func()
    ...:         print("== This is the end of function ==")
    ...:     return wrap
    ...:
    ...: def hello():
    ...:     print("Hello world!")
    ...:
In [17]: hello = add_text(hello)

In [18]: hello()
== This is head of function ==
Hello world!
== This is the end of function ==
In [19]: def add_text(func):
    ...:     def wrap():
    ...:         print("== This is head of function ==")
    ...:         func()
    ...:         print("== This is the end of function ==")
    ...:     return wrap
    ...:
    ...: @add_text
    ...: def hello():
    ...:     print("Hello world!")
    ...:

In [20]: hello()
== This is head of function ==
Hello world!
== This is the end of function ==
In [1]: import re
In [2]: pattern = r'spam'
In [3]: if re.match(pattern, 'spamxxx'):
   ...:     print('匹配成功')
   ...: else:
   ...:     print('匹配失败')
   ...:
匹配成功
In [5]: print(re.match(pattern, 'xspamxx'))
None
In [6]: print(re.search(pattern, 'xspamxx'))
<re.Match object; span=(1, 5), match='spam'>
In [7]: print(re.findall(pattern, 'xspamxxspamspam'))
['spam', 'spam', 'spam']
In [8]: match = re.search(pattern, 'xspamxx')
In [9]: match.group()
# Out[9]: 'spam'
In [10]: match.start()
# Out[10]: 1
In [11]: match.end()
# Out[11]: 5
In [12]: match.span()
# Out[12]: (1, 5)
In [13]: re.sub?
Signature: re.sub(pattern, repl, string, count=0, flags=0)
Docstring:
Return the string obtained by replacing the leftmost
non-overlapping occurrences of the pattern in string by the
replacement repl.  repl can be either a string or a callable;
if a string, backslash escapes in it are processed.  If it is
a callable, it's passed the Match object and must return
a replacement string to be used.
File:      ~/miniconda3/lib/python3.7/re.py
Type:      function
In [14]: to_sub = 'apple orange apple'
In [16]: re.sub(r'apple', 'juice', to_sub)
# Out[16]: 'juice orange juice'
In [17]: re.sub(r'apple', 'juice', to_sub, count=1)
# Out[17]: 'juice orange apple'
In [22]: print(re.search(r'^apple', ' apple'))  # 限定必须以 a 起始
None
In [23]: print(re.search(r'apple$', 'apple '))  # 限定必须以 e 结束
None
In [24]: print(re.search(r'apple', ' apple'))
<re.Match object; span=(1, 6), match='apple'>
In [25]: print(re.search(r'apple', 'apple '))
<re.Match object; span=(0, 5), match='apple'>
In [26]: print(re.search(r'[a-z]', 'happy new year'))
<re.Match object; span=(0, 1), match='h'>
In [27]: print(re.search(r'[a-z]', 'HAPPY NEW YEAR'))
None
In [28]: print(re.search(r'[A-Z]', 'HAPPY NEW YEAR'))
<re.Match object; span=(0, 1), match='H'>
In [29]: print(re.search(r'[A-Za-z]', 'HAPPY new YEar'))
<re.Match object; span=(0, 1), match='H'>

In [30]: print(re.search(r'[A-Z]', 'happy new year'))
None
r'^TEL: [0-9]{11}$'
In [31]: print(re.match(r'^TEL: [0-9]{11}$', 'TEL: 12345678912'))
<re.Match object; span=(0, 16), match='TEL: 12345678912'>
In [32]: print(re.match(r'^TEL: [0-9]{11}$', 'TEL: 1234567891'))
None
In [33]: print(re.match(r'^TEL: [0-9]{11}$', 'TEL: 12345678912 '))
None
In [34]: print(re.match(r'^TEL: [0-9]{11}$', 'EL: 12345678912'))
None
In [35]: print(re.match(r'^TEL: [0-9]{11}$', 'TEL:12345678912'))
None
