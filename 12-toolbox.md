# 第 12 章 数据分析工具箱

**本章内容提要**:

- 再讲函数
- 作用域 （这两点前面都讲过，看看有什么可以补充的）
- lambda 表达式
- 迭代器
- 生成器
- 装饰器？
- 魔术命令

 ### 序列解包

 多个赋值操作可以同时进行。

 x, y, z = 1, 2, 3
 print(x, y, z)

 可以交换多个变量：

 x, y = y, x

 这里做的事情叫做序列解包，将多个值的序列解开，然后放到左侧的变量序列中。

 当函数或者方法返回元组（或其他可迭代对象）时，这个操作尤为有用。
 如果某方法以元组返回，那么该元组可以直接赋值到两个变量中。
 同样，它允许函数返回一个以上的值并打包成元组，然后通过一个赋值语句很容易访问。
当然等号两侧数量要一致，否则会报错。

### 断言

与其让程序在晚些时候崩溃，不如在错误条件出现时直接让它崩溃。使用 assert

如果需要确保程序中的某个条件一定为真时才能让程序正常工作的话，assert 语句就有用了。

assert 会检查一个表达式，如果返回逻辑值 False，就会生成断言错误。assert 也可以带第二个参数用来详细地描述错误。

```
>>> a = 10
>>> assert a > 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert a > 10, "a is not equal to 10"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: a is not equal to 10
```

程序员经常将断言放到函数的开始部分用于检查输入是否合法，以及在函数调用后使用以检查输出是否合法。


### 使用 exec 和 eval 执行和求值字符串

用于动态编程。

```
>>> exec("print('Hello world')")
Hello world
```

它可能会干扰命名空间（作用域）

```
>>> from math import sqrt
>>> exec('sqrt = 1')
>>> sqrt(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

可以指定命名空间来避免

```
>>> scope = {}
>>> exec('sqrt = 1', scope)
>>> scope['sqrt']
1
```

exec 语句会执行一系列 Python 语句，而 eval 计算以字符串形式书写的表达式，并返回结果值。

```
>>> eval('sqrt = 1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    sqrt = 1
         ^
SyntaxError: invalid syntax
>>> eval('sqrt + 1')
2
```

eval 也可以使用命名空间。

```
>>> scope = {}
>>> scope['x'] = 2
>>> scope['y'] = 3
>>> eval('x * y', scope)
6
```


### 作用域

```
>>> x = 1
>>> scope = vars()
>>> scope['x']
1
>>> scope['x'] += 1
>>> scope['x']
2
>>> type(scope)
<class 'dict'>
```

在执行 x = 1 赋值语句后，符号 x 引用到值 1.这就像字典一样，键引用值。当然，变量和所对应的值用的时一个不可见的字典，实际上这已经很接近真实情况，内建的 vars 函数可以返回这个字典。

这个就叫做命名空间或作用域。除了全局作用域外，每个函数调用都会创建一个新的作用域。

屏蔽问题：当局部变量名和全局变量名同名时，前者会屏蔽后者。这种情况下如果想要使用全局变量，可以使用globals函数。

globals函数返回全局变量字典，而locals返回局部变量的字典。

如果想要将局部变量x声明为全局变量，使用 global x

### 函数式编程

TODO: 截图 71

闭包：函数工厂

返回函数。

```
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
```

函数的使用方法和其他对象基本一样，可以分配给变量，作为参数传递以及从其他函数返回。
尽管Python不倚重函数，但也可以进行函数式程序设计。

这里要提到一些有用函数

map 将序列中的元素全部传递给一个函数 

filter 基于一个返回布尔值的函数对元素进行过滤

上面两者可以用列表推导式替换

lambda 表达式可以创建匿名函数

reduce （使用函数聚合）



### 捕获异常

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


### 产生异常

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

### 常用字符串方法

```python
print(", ".join(["spam", "eggs", "ham"]))

print("Hello ME".replace("ME", "wrold"))

print("This is a sentence.".startswith("This"))

print("This is a sentence.".endswith("sentence."))

print("This is a sentence.".upper())
print("THIS IS A SENTENCE.".lower())

print("spam, eggs, ham".split())
```

### 利用迭代器读入大型数据集

Python open() 函数本身就返回迭代器

```python
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:
        data = file_object.readline()
        if not data:
            break
        # Yield the line of data
        yield data

with open('xxx.csv') as file:
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
``` 

Pandas read_csv 迭代器，使用 chunksize 选项，会生成 reader 迭代器。

```python
import pandas as pd

df_reader = pd.read_csv('xxx.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))
```

### 魔术命令

常见魔术命令列表，举几个最常见的作为示例

