# 第 12 章 数据分析工具箱

**本章内容提要**:

- 再讲函数
- 作用域 （这两点前面都讲过，看看有什么可以补充的）
- lambda 表达式
- 迭代器
- 生成器
- 装饰器？

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




以下内容用于补充和修改函数章节。

一般来说，内建的 callable 函数可以用来判断函数是否可调用。

Python 在概念层次上只有位置参数和关键字参数。

可变参数其实是将参数收集为元组的行为。星号的意思时“收集其余的位置参数”。

```
>>> def print_params(*params):
...
>>> print_params("test")
('test',)
>>> print_params(1, 2, 3)
(1, 2, 3)
>>> def print_params(title, *params):
...  print(title)
...  print(params)
...
>>> print_params("Params:", 1, 2, 3)
Params:
(1, 2, 3)
```

同理， ** 用于关键字参数的收集操作。

```
>>> def print_params(**params):
...  print(params)
...
>>> print_params(x=1, y=2, z=3)
{'x': 1, 'y': 2, 'z': 3}
```

位置参数在关键字参数之前。

同样的原理，我们可以使用 * 和 ** 为函数提供任意参数，而不用手动输入。


