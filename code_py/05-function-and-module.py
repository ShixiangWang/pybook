# 用 w 表示体重，h 表示身高
w1 = 70.2
w2 = 60.6
w3 = 54.3
h1 = 1.90
h2 = 1.73
h3 = 1.65
BMI_1 = w1 / h1 ** 2
BMI_2 = w2 / h2 ** 2
BMI_3 = w3 / h3 ** 2
In [1]: help(abs)
In [2]: abs?
Signature: abs(x, /)
Docstring: Return the absolute value of the argument.
Type:      builtin_function_or_method
In [3]: abs(-1)
# Out[3]: 1
In [4]: abs(1)
# Out[4]: 1
In [5]: abs('a')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-f2001f88707b> in <module>
----> 1 abs('a')

TypeError: bad operand type for abs(): 'str'

In [6]: abs(1, 2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-6c188a838f2b> in <module>
----> 1 abs(1, 2)

TypeError: abs() takes exactly one argument (2 given)
In [7]: max(2,1,3,4,5,2,3,10,2,4,5)
# Out[7]: 10
In [8]: a = abs
In [9]: a(-10)
# Out[9]: 10
In [10]: def fib(n):
    ...:      """打印斐波那契数列到n"""
    ...:      a, b = 0, 1
    ...:      while a < n:
    ...:          print(a, end=' ')
    ...:          a, b = b, a+b
    ...:      print()

In [11]: fib(10) # 调用函数，打印
0 1 1 2 3 5 8
In [12]: fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
 def fib(n):
    """打印斐波那契数列到n"""
    print("n是局部变量，它的值是"+str(n)) # 打印函数的局部变量n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
In [13]: c = 10
    ...: fib(c)
    ...:
    ...: print(n)
n是局部变量，它的值是10
0 1 1 2 3 5 8
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-9748ce91e137> in <module>
      2 fib(c)
      3
----> 4 print(n)

NameError: name 'n' is not defined
In [14]: fib(0)
n是局部变量，它的值是0
In [15]: print(fib(0))
n是局部变量，它的值是0
None # 这里是函数最后返回的None值
In [16]: def factorial(n):
    ...:     if n == 1:
    ...:         return 1
    ...:     else:
    ...:         return n * factorial(n-1)

In [17]: factorial(1)
# Out[17]: 1

In [18]: factorial(5)
# Out[18]: 120

In [19]: factorial(10)
# Out[19]: 3628800
In [20]: factorial(1000)
# Out[20]: 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

In [21]: factorial(100000)
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
<ipython-input-21-43ad924d46ef> in <module>
----> 1 factorial(100000)

<ipython-input-16-b3332bd42a71> in factorial(n)
      3         return 1
      4     else:
----> 5         return n * factorial(n-1)

... last 1 frames repeated, from the frame below ...

<ipython-input-16-b3332bd42a71> in factorial(n)
      3         return 1
      4     else:
----> 5         return n * factorial(n-1)

RecursionError: maximum recursion depth exceeded in comparison
In [22]: def power(x, n):
    ...:     s = 1
    ...:     while n > 0:
    ...:         n = n - 1
    ...:         s = s * x
    ...:     return s

In [23]: power(2, 2)
# Out[23]: 4
In [24]: power(2, 3)
# Out[24]: 8
In [25]: power(x = 2, 5)
  File "<ipython-input-40-b1e390a5e3ac>", line 1
    power(x = 2, 5)
                ^
SyntaxError: positional argument follows keyword argument

In [26]: power(2, n = 5)
# Out[26]: 32
In [27]: power(x = 2, n = 5)
# Out[27]: 32
In [28]: def ask_ok(prompt, retries=4, reminder='Please try again!'):
    ...:     while True:
    ...:         ok = input(prompt)
    ...:         if ok in ('y', 'ye', 'yes'):
    ...:             return True
    ...:         if ok in ('n', 'no', 'nop', 'nope'):
    ...:             return False
    ...:         retries = retries - 1
    ...:         if retries < 0:
    ...:             raise ValueError('invalid user response')
    ...:         print(reminder)
In [29]: ask_ok("你真想退出吗？")
你真想退出吗？y
# Out[29]: True

In [30]: ask_ok("你真想退出吗？", 2)
你真想退出吗？fgfg
Please try again!
你真想退出吗？fewe
Please try again!
你真想退出吗？gdhgds
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-24-e2ab09b6f802> in <module>
----> 1 ask_ok("你真想退出吗？", 2)

<ipython-input-22-16d7c37266ff> in ask_ok(prompt, retries, reminder)
      8         retries = retries - 1
      9         if retries < 0:
---> 10             raise ValueError('invalid user response')
     11         print(reminder)

ValueError: invalid user response

In [31]: ask_ok("你真想退出吗？", 1, "不好意思，只能是yes或no！")
你真想退出吗？npe
不好意思，只能是yes或no！
你真想退出吗？yes
# Out[31]: True
In [32]: def f(a, L=[]):
    ...:     L.append(a)
    ...:     return L

In [33]: print(f(1))
    ...: print(f(2))
    ...: print(f(3))
[1]
[1, 2]
[1, 2, 3]
In [34]: def f(a, L=None):
    ...:     if L is None:
    ...:         L = []
    ...:     L.append(a)
    ...:     return L

In [35]: print(f(1))
    ...: print(f(2))
    ...: print(f(3))
[1]
[2]
[3]
In [36]: def calcSquareSum(*numbers):
    ...:     sum = 0
    ...:     for n in numbers:
    ...:         sum = sum + n * n
    ...:     return sum

In [37]: calcSquareSum(1, 2, 3)
# Out[37]: 14
In [38]: calcSquareSum()
# Out[38]: 0

In [39]: input = [3, 4, 5]
In [40]: calcSquareSum(*input)
# Out[40]: 50
In [41]: def print_params(*params):
   ...:      print(params)
   ...:

In [42]: print_params(1, 3, 5, 7, 9)
(1, 3, 5, 7, 9)
In [43]: def print_params2(name, *params):
   ...:      print(name, params)
   ...:
In [44]: print_params2("Admin", 1, 2, 3, 4)  # 我们会看到 name 和 params 是分开的
Admin (1, 2, 3, 4)
In [45]: print_params({"a":1, "b":2})  # 我们得到的是元组而不是字典
({'a': 1, 'b': 2},)
In [46]: def person(name, age, **kw):  # 这里的kw就是关键字参数
    ...:     print('性别：', name, '年龄', age, '其他', kw)

In [47]: person("Shixiang", 25)
性别： Shixiang 年龄 25 其他 {}

In [48]: person("小丹", 25, city = "上海", job = "数据分析工程师")
性别： 小丹 年龄 25 其他 {'city': '上海', 'job': '数据分析工程师'}
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""这是一个计算阶乘的模块，
它利用了math模块和sys模块"""

__author__ = 'Shixiang'

import sys
import math

def fact():
    args = sys.argv
    if len(args)==1:
        print('请重新运行并输入一个数字。')
    elif len(args)==2:
        print(math.factorial(int(args[1])))
    else:
        print('这个函数只接收一个参数，而且必须是数字！')

if __name__=='__main__':
    fact()
if __name__=='__main__':
    fact()
In [49]: !python3 fib.py 3
6
In [50]: %run fib.py 3
6

In [51]: %run fib.py 5
120
import sys, os, time
import sys
import os
import time
import sys as system
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from os import *
In [1]: import somemodule
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-b58142f7538b> in <module>()
----> 1 import somemodule

ModuleNotFoundError: No module named 'somemodule'
In [2]: import sys

In [3]: sys.path
# Out[3]:
['',
 '/home/zd/anaconda3/bin',
 '/home/zd/anaconda3/lib/python37.zip',
 '/home/zd/anaconda3/lib/python3.7',
 '/home/zd/anaconda3/lib/python3.7/lib-dynload',
 '/home/zd/anaconda3/lib/python3.7/site-packages',
 '/home/zd/anaconda3/lib/python3.7/site-packages/IPython/extensions',
 '/home/zd/.ipython']
