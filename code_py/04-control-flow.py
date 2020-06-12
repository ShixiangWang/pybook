# if condition:
#     语句1
#     语句2
#     ...
# else:
#     语句1
#     语句2
#     ...
In [1]: number = 5

In [2]: number > 2
# Out[2]: True
In [3]: number > 3 and number <=5
# Out[3]: True

In [4]: fiction1 = "哈利波特"
In [5]: fiction2 = "侏罗纪世界"

In [6]: fiction1 == fiction2
# Out[6]: False
In [7]: if number < 2:
   ...:     print('数字太小了')
   ...: else:
   ...:     print('数字太大了')
   ...:
数字太大了
In [9]: if fiction1 == fiction2:
   ...:     print('原来我们都喜欢电影《' + fiction1 + '》')
   ...: else:
   ...:     print('你喜欢电影《'+fiction1+'》'+'，我喜欢电影《'+fiction2+'》')
   ...:
你喜欢电影《哈利波特》，我喜欢电影《侏罗纪世界》
In [10]: fiction1 = input("你喜欢的科幻电影是:")
    ...: if fiction1 == fiction2:
    ...:     print('原来我们都喜欢电影《' + fiction1 + '》')
    ...: else:
    ...:     print('你喜欢电影《'+fiction1+'》'+'，我喜欢电影《'+fiction2+'》')
    ...:
# 你喜欢的科幻电影是:环太平洋
# 你喜欢电影《环太平洋》，我喜欢电影《侏罗纪世界》

# if condition1：
#     代码块1
# elif condtion2:
#     代码块2
# else

In [13]: number = 2
    ...: if number < 0:
    ...:     print("{}是一个负数".format(number))
    ...: elif number > 0:
    ...:     print("{}是一个正数".format(number))
    ...: else:
    ...:     print("{}既不是正数也不是负数".format(number))
    ...:
# 2是一个正数
In [15]: print("{}是一个数字".format(2))
    ...: print("{0}是一个比{1}大的数字".format(10,5))
    ...: print("{1}是一个比{0}小的数字".format(10,5))
    ...:
# 2是一个数字
# 10是一个比5大的数字
# 5是一个比10小的数字
In [17]: number = 42
    ...: number_type = '偶数' if number % 2 == 0 else '奇数'
    ...: print("{} 是一个 {} ".format(number, number_type))
    ...:
# 42 是一个 偶数
In [18]: number = 10
    ...: if number % 2 == 0 and number % 5 == 0:
    ...:     print("数字{}是2和5的公倍数".format(number))
    ...:
# 数字10是2和5的公倍数
In [19]: number = 22
    ...: if (not number % 2 == 0) and (number < 10):
    ...:     print(number)
    ...: else:
    ...:     print("输入的数不满足条件")
    ...:
# 输入的数不满足条件
In [23]: 1 in [1, 2, 4, 5]
# Out[23]: True
In [24]: if 2 in [1,2,3,5,7,9]:
    ...:     print("这个列表肯定不全是奇数，因为包含了数字2")
    ...:
# 这个列表肯定不全是奇数，因为包含了数字2

# print(1)
# print(2)
# print(3)
# ...
# print(100)
In [25]: for i in range(1, 101):
    ...:     print(i)
    ...:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ...
# 100
In [26]: for i in range(1, 6):
    ...:     print(i)
    ...: else:
    ...:     print("For循环结束了。")
    ...:
# 1
# 2
# 3
# 4
# 5
# For循环结束了。
In [27]: for i in range(1,6):
    ...:     print(i)
    ...:
    ...: print("For循环结束了")
    ...:
# 1
# 2
# 3
# 4
# 5
# For循环结束了
In [28]: for n, x in enumerate('亲爱的你好吗？'):
    ...:     print(n, x)
    ...:
# 0 亲
# 1 爱
# 2 的
# 3 你
# 4 好
# 5 吗
# 6 ？
In [29]: for n, x in enumerate('亲爱的你好吗？', start=1):
    ...:     print(n, x)
    ...:
# 1 亲
# 2 爱
# 3 的
# 4 你
# 5 好
# 6 吗
# 7 ？
In [30]: odd = [1, 3, 5]
    ...: even = [2, 4, 6]
    ...: for i, j in zip(odd, even):
    ...:     print("和为{}".format(i+j))
    ...:
# 和为3
# 和为7
# 和为11
numbers = list(range(1,101))
result = []
for num in numbers:
    result.append(num * num)
result = [num * num for num in numbers]
import time

numbers = list(range(1,100001))
fl_square_numbers = []

# 计算时间
t0 = time.perf_counter()

# ------------ for 循环 ------------
for num in numbers:
    fl_square_numbers.append(num * num)

# 计算时间
t1 = time.perf_counter()

# ------- 列表推导式 -------
lc_square_numbers = [num * num for num in numbers]

# 执行结果
t2 = time.perf_counter()
fl_time = t1 - t0
lc_time = t2 - t1
improvement = (fl_time - lc_time) / fl_time * 100

# 对结果对齐并设定保留的小数点位数
print("For循环运行时间:           {:.4f}".format(fl_time))
print("列表推导式运行时间:         {:.4f}".format(lc_time))
print("提升时间:                 {:.2f}%".format(improvement))

if fl_square_numbers == lc_square_numbers:
    print("\n两种计算方式结果相等")
else:
    print("\n两种方式计算结果不相等")
For循环运行时间:           0.0293
列表推导式运行时间:         0.0082
提升时间:                 72.14%

两种计算方式结果相等
In [34]: numbers = [2, 12, 3, 25, 24, 21, 5, 9, 12]
In [35]: odd_numbers  = []
    ...: even_numbers = []
    ...: [odd_numbers.append(num) if(num % 2) else even_numbers.append(num) for num in numbers]
    ...:
# Out[35]: [None, None, None, None, None, None, None, None, None]

In [36]: odd_numbers
# Out[36]: [3, 25, 21, 5, 9]
In [37]: even_numbers
# Out[37]: [2, 12, 24, 12]
In [38]: odd_numbers  = [num for num in numbers if num % 2]
    ...: even_numbers = [num for num in numbers if not num % 2]
    ...:

In [39]: odd_numbers
# Out[39]: [3, 25, 21, 5, 9]
In [40]: even_numbers
# Out[40]: [2, 12, 24, 12]
In [41]: books = {"夏洛克*福尔摩斯":98, "哈利波特":80, "达芬奇密码":88}
In [42]: for book_name,book_score in books.items():
    ...:     print(book_name, book_score, sep=":")
    ...:
# 夏洛克*福尔摩斯:98
# 哈利波特:80
# 达芬奇密码:88
In [43]: for book_key in books.keys():
    ...:     print(book_key)
    ...:
# 夏洛克*福尔摩斯
# 哈利波特
# 达芬奇密码

In [44]: for book_score in books.values():
    ...:     print(book_score)
    ...:
# 98
# 80
# 88
In [45]: st_grades = [2, 3, 1, 1, 3, 5, 4, 6, 6, 1]
In [46]: grades_count = dict()  # 初始化字典

In [47]: for st_grade in st_grades:
    ...:     if st_grade in grades_count:
    ...:         grades_count[st_grade] += 1  # 如果某年级已有学生，则对该年级计数加1
    ...:     else:
    ...:         grades_count[st_grade] = 1   # 如果某年级第一次对学生计数，则令该年级的计数为1
    ...:

In [48]: grades_count
# Out[48]: {1: 3, 2: 1, 3: 2, 4: 1, 5: 1, 6: 2}
import random  # 导入random模块
NUMBER = random.randint(0,999)  # 生成[0, 999]范围内的数字

while True:
  guess = int(input("请输入数字（0-999）：\n"))
  if guess == NUMBER:
    print("恭喜！猜对了！")
    break
  elif guess > NUMBER:
    print("太大了...请重新猜！")
  else:
    print("太小了...请重新猜！")

In [1]: number_list = [1, 2, 4, 5, 7, 8, 10]
In [2]: import math

In [3]: for i in number_list:
   ...:     print(math.factorial(i))
# 1
# 2
# 24
# 120
# 5040
# 40320
# 3628800
In [4]: number_list = []
   ...: for i in range(1, 1001):
   ...:     if i % 3 == 0:
   ...:         continue
   ...:     else:
   ...:         number_list.append(i)
   ...:
   ...: len(number_list)
# Out[4]: 667
number_list = [ i for i in range(1, 1001) if i % 3 != 0 ]
[ print(math.factorial(i)) for i in range(1, 1001) if i % 3 != 0 ]
In [5]: a = 1
   ...: while True:
   ...:     print(a)
   ...:     a += 1
   ...:     if a == 10:
   ...:         break
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
In [6]: for i in range(5,10):
   ...:     print(i)
   ...:     if i > 7:
   ...:         break
# 5
# 6
# 7
# 8
In [7]: a = 10
   ...: while a <= 12:
   ...:     a += 1
   ...:     for i in range(1,7):
   ...:         print(i)
   ...:         if i == 5:
   ...:             break
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
if x < 0:
    print('负数！')
elif x == 0:
    # 未来要做的事情：....
    pass
else:
    print('正数！')
In [8]: %pwd
# Out[8]: '/Users/wsx'
In [8]: %ls
Applications/    Library/         Public/          work_script.pbs*
Desktop/         Movies/          go/
Documents/       Music/           test.txt
Downloads/       Pictures/        tmp/
In [9]: f = open('test.txt', 'r')
In [10]: f1 = open('test1.txt', 'r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-10-ef17b5d7a1d3> in <module>
----> 1 f1 = open('test1.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
In [11]: f.read()
# Out[11]: '这是文本的第一行\n这是文本的第二行\n这是文本的第三行\n这是文本的最后一行\n'
In [12]: f.close()
try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
with open('test.txt', 'r') as f:
    print(f.read())
In [13]: for line in f.readlines():
    ...:     print(line.strip())  # 把末尾的'\n'删掉
这是文本的第一行
这是文本的第二行
这是文本的第三行
这是文本的最后一行
In [14]: f = open('/Users/wsx/Pictures/cover.png', 'rb')
In [15]: f.read()  # 下面输出的结果太多，因此省略
# Out[15]: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00 ...
In [16]: f = open('/Users/wsx/Documents/gbk.txt', 'r', encoding='UTF-8')
In [17]: f.read()
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-17-571e9fb02258> in <module>
----> 1 f.read()

/Volumes/Data/miniconda3/lib/python3.6/codecs.py in decode(self, input, final)
    319         # decode input (taking the buffer into account)
    320         data = self.buffer + input
--> 321         (result, consumed) = self._buffer_decode(data, self.errors, final)
    322         # keep undecoded input until the next call
    323         self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd5 in position 0: invalid continuation byte
In [18]: f = open('/Users/wsx/Documents/gbk.txt', 'r', encoding='gbk')
In [19]: f.read()
# Out[19]: '这是GBK编码的文本，如果你不正确解码就看不到正确内容喔~'
In [20]: f = open('test.txt', 'w')
In [21]: f.write('我给文本加一行\n')
# Out[21]: 8
In [22]: f.write('我再加一行，这是最后一行')
# Out[22]: 12
In [23]: f.close()
with open('test.txt', 'w') as f:
  f.write('我给文本加一行\n')
  f.write('我再加一行，这是最后一行')
In [24]: with open('test.txt', 'r') as f:
    ...:     for line in f.readlines():
    ...:         print(line.strip())
我给文本加一行
我再加一行，这是最后一行
