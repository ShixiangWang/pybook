# 第 11 章 数据分析工具箱

**本章内容提要**:

- 辅助函数与工具
- 作用域与求值计算
- 异常捕获
- 函数式编程
- 生成器与装饰器
- 正则表达式

本章的涉及的内容非常广泛，相对本书其他章节而言较为驳杂，主旨是介绍数据分析可能会利用上的工具函数和方法，也包含 Python 高级编程相关的理论知识。

## 11.1 辅助函数与工具

### 11.1.1 序列解包

在 Python 中，多个赋值操作可以同时进行，这可以通过元组实现：

```python
x, y, z = 1, 2, 3
print(x, y, z)
```

利用该方法可以交换多个变量：

```python
x, y = y, x
```

这精简了下面代码：

```python
temp = x
x = y
y = temp
```

这种特性叫做序列解包，将多个值的序列解开，然后放到左侧的变量序列中。当函数或者方法返回元组（或其他可迭代对象）时，这个操作尤为有用。

如果某方法以元组返回，那么该元组可以直接赋值到两个变量中。同样，它允许函数返回一个以上的值并打包成元组，然后通过一个赋值语句很容易访问。

当然，等号两侧元素数量要一致，否则会报错。

### 11.1.2 断言

与其让程序在晚些时候崩溃，不如在错误条件出现时直接让它崩溃，这样可以尽早锁定程序中的错误，节省时间和调试成本。这种情况下，assert 语句可以排上用场。

assert 会检查一个表达式，如果返回逻辑值 False，就会生成断言错误。assert 也可以带第二个参数用来详细地描述错误。

```python
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
```

程序员经常将断言放到函数的开始部分用于检查输入是否合法，以及在函数调用后使用以检查输出是否合法。


### 11.1.3 常用字符串方法

本小节主要通过代码示例简要介绍常用的字符串方法，其中一些函数在前面章节中有过介绍和使用。

```python
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
```

## 11.2 作用域与求值计算

### 11.2.1 作用域

我们已经知道，在函数内部命名的变量不会影响函数外部的变量，也就是说，每个变量都有自己作用的范围。这不仅仅适用于函数，也适用于其他 Python 对象。

```python
In [11]: x = 1
In [12]: scope = vars()
In [13]: scope['x']
Out[13]: 1
In [14]: scope['x'] += 2
In [15]: scope['x']
Out[15]: 3
In [16]: type(scope)
Out[16]: dict
```

上述代码在执行 x = 1 赋值语句后，符号 x 引用到值 1。这就像字典一样，键引用值。当然，变量和所对应的值用的是一个不可见的字典，实际上这已经很接近真实情况，内建的 vars() 函数可以返回这个字典。这个字典就叫做命名空间或作用域。除了全局作用域外，每个函数调用都会创建一个新的作用域。

由于同名变量的存在产生了屏蔽问题：当局部变量名和全局变量名同名时，前者会屏蔽后者。这种情况下如果想要使用全局变量，可以使用 globals() 函数。globals 函数返回全局变量字典，而 locals() 返回局部变量的字典。

```python
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
```

如果想要将局部变量 x 声明为全局变量，使用代码 global x。

```python
In [36]: a = 10
In [37]: def change_global():
    ...:     global a
    ...:     a = 5
    ...:

In [38]: change_global()
In [39]: a
Out[39]: 5
```

### 11.2.2 使用 exec() 和 eval() 执行计算

有时候，我们想要从字符串中创建 Python 代码，这可以用于动态编程。exec() 和 eval() 函数提供了这方面的支持。

```python
In [40]: exec("print('Hello world')")
Hello world
```

它可能会干扰命名空间（作用域）。

```python
In [41]: from math import sqrt
In [42]: exec('sqrt = 1')
In [43]: sqrt(4)
---------------------------------------------------------------------
TypeError                           Traceback (most recent call last)
<ipython-input-43-317e033d29d5> in <module>
----> 1 sqrt(4)

TypeError: 'int' object is not callable
```

上述代码报错的原因在于我们在全局空间中创建了一个变量 sqrt 并赋值 1，它屏蔽了先前从 math 模块中导入的 sqrt 函数。

我们可以指定命名空间来避免上述问题。

```python
In [44]: scope = {}
In [45]: exec('sqrt = 1', scope)
In [46]: scope['sqrt']
    ...: 1
Out[46]: 1
```

exec() 函数会执行一系列 Python 语句，而 eval() 函数计算以字符串形式书写的表达式，并返回结果值。

```python
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
Out[48]: 4
```

eval() 函数也可以使用命名空间。

```python
In [48]: eval('sqrt + 3')
Out[48]: 4
In [49]: scope = {}
In [50]: scope['x'] = 3
In [51]: scope['y'] = 5
In [52]: eval('x * y', scope)
Out[52]: 15
```

## 11.3 异常的捕获和处理

### 11.3.1 捕获异常

在第 4 章中我们其实已经学习过如何捕获异常，即使用 try...finally 读/写文件，确保无论发生什么都要对文件进行关闭操作。这里本书会更加详细地介绍异常、异常捕获和处理的方法。

异常是由于不同的原因产生的出乎意料的结果，有以下几个常见类型：

- ImportError - 导入失败
- IndexError - 索引超出序列范围
- NameError - 使用了未知的变量
- SyntaxError - 代码不能被正确解析
- TypeError - 函数参数输入了错误的数据类型
- ValueError - 函数调用正常，但返回值有问题

当 Python 程序抛出这些异常后，我们很容易就能够通过异常类型理解其原因，困难之处在于如何锁定异常发生的位置以及对异常进行处理。而对于小型程序和常见的数据分析任务，锁定异常的发生地点也通常比较容易，一般通过逐行输入代码运行即可找到。我们下面聚焦于异常的处理。

处理异常的基本语句是 try/except，我们将可能产生异常的代码放入 try 语句块中，而将处理语句放入 except 语句块中。如果运行代码时真的产生异常，Python 会停止执行错误代码块，而跳转到执行 except 语句块。

下面看一个简单的例子：

```python
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("完成计算！")
except ZeroDivisionError:
    print("因为除以 0 导致错误！")
```

try 语句块中可以有多条不同的 except 语句用于处理不同的异常情况。另外，多种异常也可以通过括号放入到单个 except 语句中：

```python
try:
    var = 10
    print(var + "hello")
    print(var / 2)
except ZeroDivisionError:
    print("除数为0！")
except (ValueError, TypeError):
    print("错误发生了！")
```


如果一条 except 语句没有指明任何的异常类型，那么所有的错误都将被捕获。请读者尽量少用这样的操作，因为会捕获到意想不到的错误并导致程序处理失败。

```python
try:
    wd = "hello world"
    print(wd / 0)
except:
    print("发生了一个错误")
```

我们可以使用 finally 语句保证无论发生什么错误，都会运行一些代码，如正确关闭文件。finally 语句放置在 try/except 语句之后，无论前面执行了 try 语句块的代码还是执行了 except 语句的代码，finally 语句总是会被运行。

```python
try:
    print("Hello World!")
    print(1 / 0)
except: ZeroDivisionError:
    print("不能被0整除！")
finally:
    print("无论上面干啥，我都会运行！")
```


### 11.3.2 产生异常

通过使用 raise 语句，我们可以生成异常信息。

```python
print(1)
raise ValueError
print(2)
```

异常都可以带描述性的参数：

```python
name = '123'
raise NameError("Invalid name!")
```

在 except 语句块中，不带参数的 raise 语句可以用来重新生成已经发生的异常。

```python
try:
    5 / 0
except:
    print("发生了一个异常")
    raise
```

## 11.4 函数式编程

函数式编程是一种以函数为基础的编程方式，函数的使用方法和其他对象基本一样，可以分配给变量，作为参数传递以及从其他函数返回。尽管 Python 不倚重函数，但也可以进行函数式程序设计。


### 11.4.1 高阶函数

函数式编程的一个关键部分是高阶函数。高阶函数以函数作为参数，或者以函数作为返回结果。

```python
def do_twice(func, args):
    return fun(func(args))

def add_two(x):
    return x + 2

print(do_twice(add_two, 1))
```

```python
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
```

函数式编程需要使用纯函数。纯函数没有副作用并且返回值只依赖于它的参数。

```python
# Pure function
def pure_func(x, y):
    return x + y * x

# Impure function
# 这个函数改变了 a_list 的状态
# 所以不是纯函数
a_list = []
def impure_func(args):
    a_list.append(args)
```

使用纯函数有一些优点，也有一些缺点。

- 更容易推断和测试
- 更高效
- 更容易并行

不过有时候比较难写，另外一些情况需要函数的副作用而纯函数无法提供该特性。

lambda 表达式可以创建匿名函数，这在第八章有简单使用过。lambda 函数可以赋给变量，并且可以向正常函数一样使用。不过这种情况使用 def 定义函数更好。

```python
double = lambda x: x * 2
print(double(4))
```

### 11.4.2 常用高阶函数

内置函数 map()、filter() 以及 reduce() 都是非常实用的用于操作可迭代对象（如列表、元组）的高阶函数。

map() 函数将序列中的元素全部传递给一个函数，并返回一个可迭代对象。

```python
In [54]: def double(x):
    ...:     return x * 2
    ...:
    ...: data = [11, 22, 33, 44]
    ...: res = map(double, data)
    ...: print(list(res))
    ...:
[22, 44, 66, 88]
```

这里可以直接使用匿名函数：

```python
In [55]: print(list(map(lambda x: x* 2, data)))
[22, 44, 66, 88]
```

filter() 基于一个返回布尔值的函数对元素进行过滤

```python
In [56]: list(filter(lambda x: x % 2 == 0, data))
Out[56]: [22, 44]
```

reduce() 可以进行聚合。

```python
In [3]: from functools import reduce
In [4]: def add(x, y):
   ...:     return x+y
   ...:

In [5]: reduce(add, [1,2,3,4,5])
Out[5]: 15
```

### 11.4.3 itertools 模块

itertools 是 Python 的一个标准库，提供了许多用于函数式编程的函数。

其中一类函数用于生成无限迭代器，包括 count()、cycle() 和 repeat()。

- count() 函数从一个数开始计数到无限
- cycle() 函数无限迭代一个可迭代对象（如列表或字符串）
- repeat() 函数重复一个序列有限或无限次

下面以 count() 作为简单示例：

```python
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
```

上面代码输出了序列 11-21，因为是无限迭代器，所以需要通过 break 辅助跳出循环。

itertools 库中也有一些类似 map() 和 filter() 的函数，如 takewhile() 函数可以从可迭代对象中根据预测函数提取元素，chain() 函数可以将多个可迭代对象串联为一个，accumulate() 函数可以对可迭代对象求和。下面代码仅作简单的示例。

```python
In [23]: from itertools import chain, takewhile, accumulate
In [24]: list(chain(list(range(1,5)), list(range(6,10))))
Out[24]: [1, 2, 3, 4, 6, 7, 8, 9]
In [25]: nms = list(accumulate(range(20)))
In [26]: nms
Out[26]:
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
```

## 11.5 生成器与装饰器

### 11.5.1 生成器

生成器是一类像列表、元组的可迭代对象。生成器不像列表支持索引，但是同样可以使用 for 循环进行迭代（可迭代对象都可以使用 for 循环迭代，这是迭代器的一个特性）。

创建生成器的方式比较特别，需要使用函数和一个新的关键字 yield。下面我们看一个生成 1-9 序列的例子。

```python
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
Out[3]: <generator object range2 at 0x7fde103f1f50>
In [4]: range(1, 10)
Out[4]: range(1, 10)
```

从 for 循环中的使用来看，跟列表和元组完全没有差别，但 range2() 的结果跟我们学习过的 range() 是相似的，它们返回的是对象而非实际的序列。我们可以直接使用 list() 显式地将生成器转换为列表。

```python
In [5]: list(range(1, 10))
Out[5]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [6]: list(range2(9))
Out[6]: [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

这里读者可能会有点困惑，生成器和列表到底有什么区别呢？这里的关键在于理解生成器的一个特性：它是惰性求值的。我们再来观察下 range2() 函数：

```python
def range2(i):
    while i > 0:
        yield i
        i -= 1
```

相比于直接返回要生成的序列，这里我们定义了计算下一个值的规则，即 i -= 1，在调用该生成器后，计算机不会立马执行所有的计算，而是存储该规则，等待我们需要时再执行，这一点我们可以利用 next() 函数进行验证。

```python
In [7]: a = range2(10)
In [8]: next(a)
Out[8]: 10
In [9]: next(a)
Out[9]: 9
```

这种按需计算的方式显著地提升了计算的性能，一方面生成器降低了内存的使用（文件不需要一次性读入），另一方面我们不必等待所有的序列生成后才能开始使用。读者可能没有发现，文件的读取使用的就是生成器，open() 函数读入的对象需要逐行存储或计算，并非一次性存储到内存中。

### 11.5.2 利用生成器读入大型数据集

Python open() 函数本身就返回迭代器，所以我们可以非常容易地创建生成器以读入大的数据集。下面的代码可以用于参考模板：

```python
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
```

Pandas 库的 read_csv() 函数更方便，使用 chunksize 选项，会生成 reader 生成器。

```python
import pandas as pd
df_reader = pd.read_csv('xxx.csv', chunksize=10)
print(next(df_reader))
```

### 11.5.3 装饰器

装饰器是一种可以修饰（改）其他函数的函数，这在不更改原函数的情况下拓展原函数的特性非常好用。例如，我们想要在一个函数调用运行前后添加信息输出。

我们创建一个函数 hello() 代表实际的工作函数，创建装饰器 add_text() 用来完成对 hello() 的额外修饰。

```python
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
```

下面看看我们增加对 hello() 的修饰会让它有什么不同。

```python
In [17]: hello = add_text(hello)

In [18]: hello()
== This is head of function ==
Hello world!
== This is the end of function ==
```

我们在 add_text() 中添加的信息成功在运行时输出了。现在我们关注装饰器的创建，从逻辑上理解它的结构：它以一个函数作为输入，并在内部定义一个嵌套函数作为返回值。这样，当实际上一个函数被作为参数传入时，该函数被重塑为一个新的函数 wrap() 并被作为结果返回，完成了一个新的函数构建，但从外观来看，我们感觉到原函数被“修饰”了。

为了简化装饰器的分配，Python 允许在原函数定义前使用符号 @ 指派装饰器，从而简化了代码的编写。

```python
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
```


## 11.6 正则表达式

正则表达式是一种操作字符串的强大工具。它是一种领域专属语言（domain specific language, DSL），意思是它以一种库的形式呈现在各类现代编程语言中，而不仅仅 Python 中。这与结构化查询语句 SQL 是类似的。

正则表达式通常有两大用处：

- 验证字符串匹配莫种模式，如验证邮箱格式、电话号码
- 对字符串执行替换，如将美式英语转换为英式英语

Python 提供了一个标准库 re 用于操作正则表达式。在我们定义好正则表达式后，函数 re.match() 可以用来查看是否它匹配一个字符串的起始。如果匹配成功，则返回一个匹配对象；如果匹配失败，返回 None。为了避免混淆，我们这里都使用原生字符串 r'string' 创建正则表达式。

```python
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
```

另外有函数 re.search() 用于在字符串任意之处寻找匹配的模式，re.findall() 寻找匹配一个模式的所有子串。

```python
In [6]: print(re.search(pattern, 'xspamxx'))
<re.Match object; span=(1, 5), match='spam'>
In [7]: print(re.findall(pattern, 'xspamxxspamspam'))
['spam', 'spam', 'spam']
```

我们可以看到上面 re.search() 返回的结果是一个 Match 对象，有几个常用的方法可以获取匹配的信息。

```python
In [8]: match = re.search(pattern, 'xspamxx')
In [9]: match.group()
Out[9]: 'spam'
In [10]: match.start()
Out[10]: 1
In [11]: match.end()
Out[11]: 5
In [12]: match.span()
Out[12]: (1, 5)
```

re 模块最常用的函数之一可能就是 sub() 了，它可以基于正则表达式实现字符串部分内容的替换。

```python
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
```

当不修改 count 时，默认会替换字符串中所有匹配的模式。

```python
In [14]: to_sub = 'apple orange apple'
In [16]: re.sub(r'apple', 'juice', to_sub)
Out[16]: 'juice orange juice'
In [17]: re.sub(r'apple', 'juice', to_sub, count=1)
Out[17]: 'juice orange apple'
```

元字符是一类特殊的字符，它们在正则表达式中有特别的含义和用处，是正则表达式的核心，常见常用的主要有下面一些：

- 锚定符
    - ^ —— 用于锚定行首
    - $ —— 用于锚定行尾
- 数目符
    - . —— 任意一个字符
    - ? —— 0 个或 1 个
    - \+ —— 一个或以上
    - \* —— 任意个（包括 0 个）
    - {m, n} —— 至少 m 个，至多 n 个
- 可选符
    - [abc] —— a b c 三个中任意一个
    - [^abc] —— 不能是 a b c 中任意一个（即排除 a b c）
    - [a-z] —— 所有小写字母
    - [A-Z] —— 所有大写字母
    - [0-9] —— 所有数字

锚定符用于定义正则表达式的起始和结尾。

```python
In [22]: print(re.search(r'^apple', ' apple'))  # 限定必须以 a 起始
None
In [23]: print(re.search(r'apple$', 'apple '))  # 限定必须以 e 结束
None
In [24]: print(re.search(r'apple', ' apple'))
<re.Match object; span=(1, 6), match='apple'>
In [25]: print(re.search(r'apple', 'apple '))
<re.Match object; span=(0, 5), match='apple'>
```

数目符和可选符用于占位、筛选和模糊匹配。

```python
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
```

假设我们需要匹配 11 位的手机号码，格式如下：

```
TEL: 12345678912
```

正则表达式可以写为

```python
r'^TEL: [0-9]{11}$'
```

下面测试看看：

```python
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
```

第一次当我们输入正确格式的数据时，返回了匹配。后面所有的字符串都有所不同，因此都不能匹配。不知道读者是否感受到了正则表达式的强大，如果工作中有遇到可以用正则表达式解决的问题，赶紧用起来吧。

## 11.7 章末小结

本章的涉及的内容非常广泛，相对本书其他章节而言较为驳杂，主旨是介绍数据分析可能会利用上的工具函数和方法，也包含 Python 高级编程相关的理论知识。