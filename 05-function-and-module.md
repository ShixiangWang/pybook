# 第 5 章 函数与模块 {#function-and-module}

**本章内容提要**：

- 为什么使用函数
- 函数的创建与使用
- 模块与包
- 第三方模块的下载与使用

在上一章中，本书介绍了如何使用控制与循环结构来自动化反复进行的操作。
尽管利用这些控制流操作可以极大简化一些处理任务，但针对一些日常的工作任务，我们可能需要频繁地拷贝大段的代码，进行修改。
这种简化的力度仍显不够，而且极容易出错，因此我们需要新的工具来提升程序编写的效率。
在这种情况下，我们可以自己创建函数或者使用标准模块/三方模块中提供的简便函数。
本章将向读者详尽地介绍如何创建函数和设定函数参数，以及使用第三方模块。

## 5.1 函数

### 5.1.1  为什么使用函数

在第 2 章中，本书已经介绍过使用身高和体重值便可以计算出 BMI 指数。
假设读者现在需要计算 3 个人的 BMI 指数，于是使用如下代码：
  
```python
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
```

此处代码中出现了规律的重复。读者可以首先思考下用循环的方式进行优化：将体重数据与身高数据分别存储在列表中，
然后使用 for 循环遍历并计算 BMI 指数。然而这种优化方式有两个问题，一是代码的输入量并没有减轻，
二是如果接下来要计算另一个人的 BMI 指数，还需要重新创建输入列表。
  
函数是最基本的代码抽象方式，借助函数，读者可以不用关注底层的具体计算过程，而从更高层次对问题进行思考。
读者如果将核心的计算步骤抽象为函数表示，将极大地简化上述问题的处理。
例如，步骤 BMI = w / h\*\*2 写为更有意义的函数 calcBMI()，每次调用 calcBMI(w, h) 就可以计算一次 BMI 指数，
而且函数本身只需要写一次就可以多次调用。

几乎所有的编程语言都支持函数，Python 当然也不例外，读者在前面章节中其实也已经多次见过函数的使用。
Python 不但能非常灵活地创建函数，而且本身内置很多可用的函数，开箱即用。
  

### 5.1.2 函数的调用  

Python 内置的函数无需进行导入操作，只需要知道函数的名称和参数，读者就可以直接在代码中调用。
例如，abs() 函数可以求取绝对值，它只需要一个输入参数。读者可以输入「help(函数名)」或者「函数名? 」查看函数的文档，
以下用 abs() 函数进行演示。
  
```python
In [1]: help(abs)                                                               
In [2]: abs?                                                                    
Signature: abs(x, /)
Docstring: Return the absolute value of the argument.
Type:      builtin_function_or_method
```

读者将需要进行绝对值处理的数值作为参数输入 abs() 函数即可实现调用。
  
```python
In [3]: abs(-1)                                                                 
Out[3]: 1

In [4]: abs(1)                                                                  
Out[4]: 1
```

读者在进行函数调用时需要注意输入参数的数目和类型，如果数目或类型与函数预期的不一致，
Python 会抛出 TypeError 错误，并给出错误信息。
  
```python
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
```

有些函数可以接收任意多个数目的参数，如 max()，它可以返回一组数的最大值。
  
```python
In [7]: max(2,1,3,4,5,2,3,10,2,4,5)                                             
Out[7]: 10
```

本质上，函数名其实是指向一个函数对象的引用（在 Python 里一切都是对象，变量都是对对象的引用，方便我们使用）。
所以，读者完全可以把函数名赋值给一个变量，这相当于给函数起了个别名，有时候可以简化使用。
  
```python
In [8]: a = abs                                                                 

In [9]: a(-10)                                                                  
Out[9]: 10
```

当然，这里将 abs() 函数重命名为 a() 是不可取的，它降低了代码的可读性和可维护性。

### 5.1.3 函数的创建

有时候，Python 内置的函数以及三方模块的函数不能满足工作需求，读者需要自己创建函数，因而本小节将指导读者如何自己创建函数。

Python使用 def 关键字对函数进行定义：在 def 语句后依次写出函数名、括号、参数与英文冒号，并在随后的代码块中编写函数体，
如果想要返回一些结果，则使用 return 语句。下面定义了一个 fib 函数，用于打印到指定参数为止得到的斐波那契数列。
  
```python
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
```

根据上述的代码，现在对函数的创建进行更详细地介绍：关键字 def 引入了函数的定义，
它的后面必须跟上一个函数名以及用括号括起来的正式参数列表。
构建函数体的代码语句从下一行开始，而且必须正确缩进。函数体的第一个语句是一个可选的字符串文本，
它称为函数说明字符串（docstring）。在函数中包含 docstring 是良好代码的体现，
这样别人在使用该函数时能很容易理解该函数的功能及用法。

### 5.1.4 函数作用域

执行函数会引入新的符号表，它用于函数指定的局部变量。也就是说，函数本身形成了一个相对独立的命名空间，即函数作用域，
它在寻找变量值时会先从函数内部寻找，如果没有找到，它会在函数外部寻找。如果在函数外部都没有找到，Python 就会抛出错误。
通常，当调用函数时，函数的实际参数值就会被引入为一个函数的局部变量。
  
为了更好地帮助读者理解局部变量的概念，现在对 fib() 函数进行简单的修改。
  
```python
 def fib(n):     
    """打印斐波那契数列到n""" 
    print("n是局部变量，它的值是"+str(n)) # 打印函数的局部变量n
    a, b = 0, 1 
    while a < n: 
        print(a, end=' ') 
        a, b = b, a+b 
    print()    
```

然后对该函数进行以下调用：

```python
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
```

这里在函数外创建了一个变量 c，存储 fib() 函数实际要传入的数值，然后调用函数。
在函数定义部分，我们使用了变量 n 来指示输入参数，因此函数内部创建了一个局部变量 n 来指示实际传入变量 c 的值。
不过 n 的作用范围仅限于函数内部，读者如果在函数的外部使用该变量，Python 会抛出变量 n 未定义的错误。
  
上面的函数运行最后是将结果打印出来，大多数时候我们更希望将结果存储在变量中，这时需要利用 return 语句。
实际上，即使用户没有显式地在函数中使用 return 语句进行结果的返回，Python 也会调用 return 语句返回 None 值，
不过 None 值通过会被 Python 解释器抑制，只有使用 print 语句才能显式地观测到它。
  
```python
In [14]: fib(0)                                                                 
n是局部变量，它的值是0
In [15]: print(fib(0))                                                          
n是局部变量，它的值是0
None # 这里是函数最后返回的None值
```
  
### 5.1.5 递归函数

函数的实际调用就是一行语句，因此用户可以在函数中调用不同的函数，只要知道如何正确地传递各个参数以及处理好函数返回的结果。
这种方式大大简化了代码阅读的复杂性，各个函数自身的运行逻辑被封装在内部，使用者只需要关注如何合理地调用它们处理问题。
大多数情况，读者看到的是一个函数调用其他函数。除此之外，函数还可以实现自我调用，这种函数称为递归函数。
因其具有函数嵌套与自我调用的特点，这一小节本书着重对其进行介绍。
  
一个介绍递归函数最好的例子就是计算阶乘。阶乘的相关概念本书在上一章的 continue 语句部分已经介绍过，此处不再赘述。
  
阶乘可以直观展示为 n! = 1 x 2 x 3 x ... x n 的形式，也可以展示为递归的方式 n! = (n-1)! x n，
读者可以通过图5-1中不断循环的捧着画框的蒙娜丽莎对递归进行直观地理解。
  
此时如果令函数 factorial(n) 为 n!，那么递归的函数表示法为：factorial(n) = factorial(n-1) x n。

![图5-1 递归可视化：捧着画框的蒙娜丽莎](images/chapter5/mnlisha.png)

现在用实际的代码表征这一过程，并对结果进行测试。

```python
In [16]: def factorial(n): 
    ...:     if n == 1: 
    ...:         return 1 
    ...:     else: 
    ...:         return n * factorial(n-1)                                      

In [17]: factorial(1)                                                           
Out[17]: 1

In [18]: factorial(5)                                                           
Out[18]: 120

In [19]: factorial(10)                                                          
Out[19]: 3628800
```

factorial(5) 的计算过程可以表示如下：
  
```
===> factorial(5)
===> 5 * factorial(4)
===> 5 * (4 * factorial(3))
===> 5 * (4 * (3 * factorial(2)))
===> 5 * (4 * (3 * (2 * factorial(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
```

相比对使用循环进行阶乘的运算，递归在逻辑上更加清晰，定义更加简单，不过运算过程更为抽象。
理论上，所有的递归函数都可以写成循环的形式。在使用递归函数时需要注意必须有一个明确的递归结束条件，以避免无限调用。
  
递归函数的最大问题是效率低，占用了大量的内存和时间，当递归次数过多时容易发生栈溢出。
发生栈溢出的原因是，在计算机中函数的调用时通过堆栈（stack）来实现的，每进行一次调用，栈帧就会增加一层，每当函数返回，
栈帧就减少一层，然而计算机提供的栈帧不是无限大的，就像我们不可能真正地在上面蒙娜丽莎画像上画出无限个捧着画框的子图，
当递归调用次数过多时，就会发生栈溢出。
  
```python
In [20]: factorial(1000)                                                        
Out[20]: 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

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
```

上面代码运行结果显示当计算 1000 的阶乘时，计算机还能正常运行并计算出结果，而将输入参数设为 100,000 时，
Python 直接报错提示递归已经超出支持的最大深度。

## 5.2 函数的参数

定义函数的时候把参数的名字和位置确定下来，就完成了函数的接口的定义。
对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
这就如同用铅笔写字、素描或做其他事情，读者无需知道铅笔的制造过程。反之，函数创建者应当考虑函数内部的逻辑，
合适地设定函数的参数以方便使用者能够轻松调用。

Python 的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

### 5.2.1 默认参数

最有用的形式是给为一个或多个参数指定一个默认参数值，这样创建出来的函数用户通过设定少量参数即可调用。
  
例如，下面的 ask_ok() 函数：它向用户发出询问，如果用户同意并输入 y 或 ye 或 yes，函数都会返回 True；
如果用户不同意并输入 n 或 no 或 nop 或 nope，函数会返回 False；其他情况会提示用户再次输入。
  
```python
In [22]: def ask_ok(prompt, retries=4, reminder='Please try again!'): 
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
```

该函数可以通过几种不同的方式调用：
  
* 仅给出一个必需参数：ask_ok("你真想退出吗？")。
* 指定一个可选参数：ask_ok("你真想退出吗？", 2)。
* 或者给出所有的参数：ask_ok("你真想退出吗？", 1, "不好意思，只能是yes或no！")
  
下面对这几种调用方式进行简单的测试。
  
```python
In [23]: ask_ok("你真想退出吗？")                                               
你真想退出吗？y
Out[23]: True

In [24]: ask_ok("你真想退出吗？", 2)                                            
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

In [25]: ask_ok("你真想退出吗？", 1, "不好意思，只能是yes或no！")               
你真想退出吗？npe
不好意思，只能是yes或no！
你真想退出吗？yes
Out[25]: True
```

可以看到，无论是简单调用还是复杂调用，函数只需要定义一个，因此默认参数降低了函数的使用难度，也给函数的使用提供了灵活性。
  
虽然默认参数非常有用，但使用不当会出现较大的问题。下面定义了一个简单的函数来说明这个问题。
  
```python
In [26]: def f(a, L=[]): 
    ...:     L.append(a) 
    ...:     return L                                                           

In [27]: print(f(1)) 
    ...: print(f(2)) 
    ...: print(f(3))                                                            
[1]
[1, 2]
[1, 2, 3]
```
  
结果非常奇怪，在第 2 次和第 3 次调用时前面的结果居然还在，可是在函数定义时设定了默认参数为空列表！
这是因为 Python 只对函数的默认值计算一次，所以当默认参数是可变对象如列表、字典时，参数会累积变化，
看起来它继承了前面调用的输入。为了解决这个问题，我们需要将默认参数设定为不可变对象 None。
  
```python
In [28]: def f(a, L=None): 
    ...:     if L is None: 
    ...:         L = [] 
    ...:     L.append(a) 
    ...:     return L                                                           

In [29]: print(f(1)) 
    ...: print(f(2)) 
    ...: print(f(3))                                                            
[1]
[2]
[3]
```

现在无论调用多少次，函数也不会出现问题了。

### 5.2.2 关键字参数

关键字参数允许用户传入任意个（包括零个）包含参数名的参数，它通过在参数名前加两个星号进行指定，这些参数会在函数的内部自动组装为字典。
这一点可以通过下面的代码验证。
  
```python
In [30]: def person(name, age, **kw):  # 这里的kw就是关键字参数
    ...:     print('性别：', name, '年龄', age, '其他', kw)                     

In [31]: person("Shixiang", 25)                                                 
性别： Shixiang 年龄 25 其他 {}

In [32]: person("小丹", 25, city = "上海", job = "数据分析工程师")              
性别： 小丹 年龄 25 其他 {'city': '上海', 'job': '数据分析工程师'}
```
  
关键字参数在一些特定的场景下非常有用，如在软件做一个用户注册功能时设定可选项：如果不使用关键字参数，
一种解决方式是为用户没有输入的选项创建一个默认值（默认参数），而通过默认参数可以轻松地区分什么是必填项什么是可选项，
例如注册时除了用户名、密码外，其他都可以是可选项。
  
另外，用户可以采用与函数定义相同的方式传入关键字参数值，即传入字典。
  
```python
In [33]: extra = {'city':"上海", 'job':"数据分析工程师"} 
    ...: person("小丹", 25, **extra)                                            
性别： 小丹 年龄 25 其他 {'city': '上海', 'job': '数据分析工程师'}
```

### 5.2.3 命名关键字参数

上面我们看到关键字参数允许用户传入任意的参数，而创建函数时往往想对它们施加限制，这个可以通过命名关键字参数实现。
与关键字参数使用 \*\* 引导不同（虽然语义上相近），命名关键字参数需要用星号 \* 将其与其他参数分隔，星号符后面的参数作为关键字参数。
  
稍微对前面定义的函数 person() 进行修改可以得到使用命名关键字参数的版本。
  
```python
In [34]: def person(name, age, *, city, job): 
    ...:     print('性别：', name, '年龄', age, '城市：', city, '工作：',job)   

In [35]: person("小丹", 25, city = "上海", job = "数据分析工程师")              
性别： 小丹 年龄 25 城市： 上海 工作： 数据分析工程师
```

用户使用命名关键字参数时必须指定参数名，不然就会发生报错。
  
```python
In [36]: person("小丹", 25, city = "上海", "数据分析工程师")                    
  File "<ipython-input-36-fbeaee515b08>", line 1
    person("小丹", 25, city = "上海", "数据分析工程师")
                                         ^
SyntaxError: positional argument follows keyword argument
```

上面报错信息显示关键字参数后面跟着位置参数，这说明了两点：一是传入函数的最后一个参数没有被识别为命名关键字参数，
二是该参数被识别为了位置参数。那么位置参数又是什么呢？
  
### 5.2.4 位置参数

位置参数的含义可以比较直观的理解，它是通过位置指定的参数。既然关键在于位置，那么参数名就显得不那么重要了。
位置参数是创建函数时通常使用的参数，下面用一个简单例子说明。
  
创建一个函数用来计算数值 x 的 n 次幂。
  
```python
In [37]: def power(x, n): 
    ...:     s = 1 
    ...:     while n > 0: 
    ...:         n = n - 1 
    ...:         s = s * x 
    ...:     return s                                                           

In [38]: power(2, 2)                                                            
Out[38]: 4

In [39]: power(2, 3)                                                            
Out[39]: 8
```

这里 power(x, n) 函数两个参数 x 和 n 都是位置参数，在调用时传入的值会依次传给 x 和 n。
  
有意思的是，如果显式地指定参数名，会存在报错的情况，如下所示：
  
```python
In [40]: power(x = 2, 5)                                                        
  File "<ipython-input-40-b1e390a5e3ac>", line 1
    power(x = 2, 5)
                ^
SyntaxError: positional argument follows keyword argument


In [41]: power(2, n = 5)                                                        
Out[41]: 32

In [42]: power(x = 2, n = 5)                                                    
Out[42]: 32
```

可以发现，在几种调用方式中，如果先输入带参数名的参数（被解析为了关键字参数），后面就不能接位置参数了。这一点读者在调用函数时需要注意。
  
### 5.2.5 可变参数

Python 中除了关键字参数可以传递任意参数，可变参数也能传递任意参数。
它的定义也与关键字参数类似，仅需要在参数前面加一个星号，函数内部会将其自动组装为元组。
  
下面定义一个函数来计算输入参数的平方和。
  
```python
In [43]: def calcSqureSum(*numbers): 
    ...:     sum = 0 
    ...:     for n in numbers: 
    ...:         sum = sum + n * n 
    ...:     return sum                                                         

In [44]: calcSqureSum(1, 2, 3)                                                          
Out[44]: 14

In [45]: calcSqureSum()                                                                 
Out[45]: 0

In [46]: input = [3, 4, 5]                                                      

In [47]: calcSqureSum(*input)                                                           
Out[47]: 50
```

## 5.3 模块

实际完成一个软件开发或者数据分析流程的代码量往往是巨大的，一个文件里所存储的代码越长就越不容易维护。
为了编写可维护的代码，程序员通常将函数按照功能进行分组并将它们放到不同的文件中去，这样每个文件中的代码就少了很多，功能专一，
因此便于查找、调试错误，增加功能特性等，很多编程语言都采用这种组织代码的方式。

Python 中，每一个以 .py 为文件扩展名的代码文件都是一个模块（Module）。
模块大大提高了代码的可维护性和应用范围，编写代码不需要从头开始，用户可以选择直接引用别人已经创建好的优秀模块，
这包括 Python 内置的模块和来自第三方的模块。数据分析常常就是建立在众多的计算模块基础之上，
如 Numpy、Pandas 和 Scipy 等，基于这些行业标准级别的模块，读者可以快速实现数据的读取、操作、分析、可视化以及结果输出。
  
模块学习的核心在于了解模块、安装模块以及学习使用模块提供的函数。下面分别进行介绍。
  
### 5.3.1 模块与包结构

上面提到，一个 .py 文件就是一个模块，例如一个 abc.py 文件就是一个叫 abc 的模块。
因为世界上非常多的 Python 使用者，大家在创建模块时文件名都会采用易用易懂的命名规则，所以模块名很容易与其他的模块冲突。
为了解决这个问题，Python 引入了包对模块进行组织。包其实就是一个包含众多模块的目录，只要包名不与别的包名冲突，
那么该包所有的模块都不会产生冲突。
  
下面展示了一个名字为 fib 包的结构，该包下面有 3 个模块，这里的 abc.py 模块名字不再是 abc，而是 fib.abc。
  
```shell
fib
├── __init__.py
├── abc.py
└── fib.py
```

每一个包目录下都会有一个 \_\_init\_\_.py文件，它的模块名为包名 fib，该文件可以为空，也可以有 Python 代码，
它必须存在于包的目录下，不然 Python 会将该目录当做普通目录，而非包。
  
包也可以嵌套存在，组成多层次的包结构，如下所示：
  
```shell
fib
├── __init__.py
├── abc.py
└── fib.py
└── calc
  ├── __init__.py
  ├── def.py
  └── calculation.py
```

这里 def.py 的模块名是 fib.calc.def。每多一个层级，其中的模块名就多一个层级，层级之间用英文句号 \. 区分。
模块名要遵循 Python 变量命名规范，不要使用中文、特殊字符。
  
### 5.3.2 模块的创建
  
本小节以内置的 sys 和 math 模块为例，编写一个 fact 模块，用于计算阶乘。
  
首先用文本编辑器创建一个以 .py 为文件拓展名的文本文件，然后输入以下代码：

```python
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
```

上面代码中的第 1、2 行是标准的注释，其中第一行的注释可以让该模块直接在 Linux 系统和 macOS 系统上运行，
第 2 行注释指定代码文件使用标准的 UTF-8 编码。这两行注释是标准的规范，请读者在编写模块时务必遵守。
  
接下来的一行是字符串，它是对整个模块的功能说明，一般称为文档字符串（docstring），这跟编写函数是一致的。
任何模块/函数代码的第一个字符串都被视为文档注释。
  
\_\_author\_\_ = 'Shixiang' 这里使用专门的变量记录模块的作者，别人在使用时可以查看模块的创作者是谁。
  
上述提及的内容是 Python 模块文件的标准版本，是一个可选项，读者可以删除不写，但本书建议读者都使用标准的写法。
  
随后的内容是真正的代码部分，使用 import 关键字可以直接导入已经安装好的 Python 模块，
导入后 Python 用户就可以使用模块名来引用模块提供的函数、参数等等。
这里利用 sys 和 math 变量名我们可以访问这两个模块的所有功能。
  
fact 模块使用了 sys 模块的 argv 值以及 math 模块中的 factorial() 函数。
argv 变量用 list 的形式存储了 Python 命令行的所有参数，其中第一个参数永远是被运行 Python 文件的文件名称，
这里即是 fact.py，第二个是需要模块使用者输入的数字。
  
在实际运行 fact 模块前，我们再来看看最后两行代码的含义。
  
```python
if __name__=='__main__':
    fact()
```

当使用命令行运行 fact 模块时，Python 解释器会将特殊变量 \_\_name\_\_ 变为 \_\_main\_\_，但如果在其他地方导入 fact 模块，
该判断语句将失效。这种操作方便我们通过命令行测试代码，但直接在代码中使用 import 导入该模块也依然有效。
  
通过命令行运行代码需要打开操作系统的终端，并将其切换到 fib.py 文件所在的目录。下面美元符号是终端提示符，读者无需理会。
  
```shell
$ python3 fib.py
请重新运行并输入一个数字。
$ python3 fib.py 3
6
```

IPython 提供了更便捷的方式运行 .py 文件（这些方式在 IPython Shell、Jupyter Notebook 以及 nteract 软件中操作是一致的），
一种方式与命令行运行类似，在命令前加一个英文感叹号，这样 IPython 会将其自动解析为系统命令运行。
  
```python
In [51]: !python3 fib.py 3
6
```
  
IPython 还提供了魔术命令 %run 运行模块文件，更多魔术命令请在 IPython 中输入 %magic 阅读与学习。
  
```python
In [52]: %run fib.py 3
6

In [53]: %run fib.py 5
120
```

### 5.3.3 模块的作用域

前面本书介绍过函数的作用域，模块也有其作用域。在一个模块中，读者可以定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量希望仅仅在模块内部使用。
  
在 Python中，模块的作用域是通过符号前缀 \_ 来实现的。正常的函数和变量名是公开的，可以被直接引用，
如 abc、weight123。而类似 \_\_xxx\_\_ 这样的变量是特殊变量，它们虽然也可以被直接引用，但是有些特殊用途，
例如上面的阶乘模块代码中，\_\_author\_\_、\_\_name\_\_ 就是特殊变量，另外模块定义的文档注释也可以用特殊变量 \_\_doc\_\_ 访问。
非公开（或称私有）的函数名或变量名类似 \_xxx 和 \_\_xxx，它们不应该被直接引用（而非不能），如 \_abc，\_\_abc。
  
在模块的逻辑中，它会将私有函数或变量隐藏起来，这样可以实现更高层级的代码封装和抽象。
例如，某个模块只实现一个功能函数，但因为实现代码复杂，作者写了很多的函数组合实现各个细节部分，使用一个主函数调用，
因而作者只想提供主函数作为公开函数，其他的函数对用户不可见。
这种情况下使用私有函数对用户也是有好处的，用户只需要关注实现功能的主函数，其中的内部逻辑无需了解，私有函数都其公开反而是一种干扰。
  
因此，在编写模块时，读者不需要使用的函数或变量全部定义为私有函数或私有变量，需要使用的函数或变量则定义为公开函数或私有变量。

### 5.3.4 三方模块的安装

Python 本身内置了非常多的模块（约 200 个），涵盖了众多的功能需求，安装 Python 后就可以立刻使用，
如 sys 模块包含系统相关的参数与函数、builtins 模块包含内置对象、os 模块包含多方面的操作系统接口、math 模块提供了数学处理函数。
  
当内置模块不能满足需求时，如果想要实现的功能代码并不复杂，读者可以先尝试自己编写代码解决。
如果想要实现的功能太过复杂，超过自身的能力，读者可以通过网络搜索实现相关功能的三方模块。
PyPI（Python Package Index）是 Python 的软件仓库，它目前提供了接近 16 万个 Python 软件包，涵盖互联网世界的各个领域。
Anaconda 是 Python 常用计算包的软件仓库，它目前提供了近 2000 个计算软件包，涵盖了数据分析领域各个方面。
  
PyPI 和 Anaconda 提供的软件包分别可以通过 pip 工具和 conda 工具进行安装，它们具有极为相似的语法，简单易上手。
  
因为本书的学习是基于 Anaconda 的，所以这里介绍 conda 工具的使用。
  
conda 工具是一个命令行工具，在终端命令行中使用 --help 选项可以列出所有 conda 支持的命令以及它们的解释。
  
```shell
$ conda --help
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (/Users/wsx/.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    install      Installs a list of packages into a specified conda
                 environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove. See conda remove --help.
    search       Search for packages and display associated information. The
                 input is a MatchSpec, a query language for conda packages.
                 See examples below.
    update       Updates conda packages to the latest compatible version. This
                 command accepts a list of package names and updates them to
                 the latest versions that are compatible with all other
                 packages in the environment. Conda attempts to install the
                 newest versions of the requested packages. To accomplish
                 this, it may update some packages that are already installed,
                 or install additional packages. To prevent existing packages
                 from updating, use the --no-update-deps option. This may
                 force conda to install older versions of the requested
                 packages, and it does not prevent additional dependency
                 packages from being installed. If you wish to skip dependency
                 checking altogether, use the '--force' option. This may
                 result in an environment with incompatible packages, so this
                 option must be used with great caution.
    upgrade      Alias for conda update. See conda update --help.

optional arguments:
  -h, --help     Show this help message and exit.
  -V, --version  Show the conda version number and exit.
```

如果是在 IPython 环境中，读者使用 !conda --help 也可以返回与上述一致的结果。
  
常用的操作是搜索、安装以及删除（卸载）包，分别对应 search、install 和 remove 子命令。
  
下面是搜索 ipython 包的例子。
  
```shell
$ conda search ipython
Loading channels: done
# Name                  Version           Build  Channel             
ipython                    0.13          py26_0  pkgs/free           
ipython                    0.13          py27_0  pkgs/free           
ipython                  0.13.1          py26_0  pkgs/free           
ipython                  0.13.1          py26_1  pkgs/free           
ipython                  0.13.1          py27_0  pkgs/free           
ipython                  0.13.1          py27_1  pkgs/free           
ipython                  0.13.1          py33_0  pkgs/free           
ipython                  0.13.1          py33_1  pkgs/free           
ipython                  0.13.2          py26_0  pkgs/free           
ipython                  0.13.2          py27_0  pkgs/free           
ipython                  0.13.2          py33_0  pkgs/free           
ipython                   1.0.0          py26_0  pkgs/free           
ipython                   1.0.0          py27_0  pkgs/free           
ipython                   1.0.0          py33_0  pkgs/free   
... 此处省略若干行
```

上述结果中可以看到存在不同的 Python 版本和包版本，所以读者安装时需要注意自己使用的 Python 版本以及想要安装的包版本。
默认情况下，conda 会根据用户的 Python 版本安装最新版本的包，用户也可以通过等号进行版本指定。
  
```shell
$ conda install ipython  # conda 自动安装ipython包的最新版本
$ conda install ipython=0.13  # conda 安装ipython包，这里指定版本为0.13
```

为了检测是否包已经安装成功，可以在 IPython 中用 import 语句导入包，如果没有报错，则安装成功。
  
### 5.3.5 模块的使用

本书在前面介绍的章节中已经在不时地使用着模块，Python 通过import关键字可以导入模块，然后使用它。
本小节旨在更加详细地介绍导入模块的方法以及简介模块搜索路径的知识。
  
当存在多个模块需要导入使用时，读者只需要用英文逗号将模块名分割即可。例如下面导入 3 个模块：
  
```python
import sys, os, time
```

不过，Python 风格指南建议将每个导入语句单独一行书写。
  
```python
import sys
import os
import time
```

有时模块的名字过长或者不好理解，每次编写显得很麻烦，读者可以使用 as 语句将模块名重命名。
  
```python
import sys as system
```

现在 sys 模块就有了 system 的别名。Python 中有不少包都有着公认的别名，如 numpy 导入为 np。
使用英文句号（成员操作符）可以导入指定模块的子模块，matplotlib 包的子模块 pyplot 就常被导入为 plt。
  
```python
import numpy as np
import matplotlib.pyplot as plt
```

有时候我们仅想要使用某个模块特定的函数，这可以通过 from 语句进行导入，例如从 math 模块中导入阶乘函数 factorial()。
  
```python
from math import factorial
```

这样读者可以直接使用 factorial() 函数了。如果使用 import math 的方式，读者必须通过 math.factorial() 才能调用该函数。
  
如果想要导入模块的全部内容，可以使用星号符。
  
```python
from os import *
```

这样导入的好处是调用起来方便，不需要使用成员操作符，但带来的麻烦更大，当导入的多个模块存在同名函数或变量时，
这样 Python 的命名空间很混乱，你不知道你使用的到底是哪一个，因此本书不推荐使用该方式导入模块函数。

使用模块时读者除了需要了解几种不同的导入方式，还需要注意模块的搜索路径。

当 Python 用户加载模块时，Python 会在指定的路径下搜索对应的 .py 文件，如果找不到就会报错：

```python
In [1]: import somemodule
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-b58142f7538b> in <module>()
----> 1 import somemodule

ModuleNotFoundError: No module named 'somemodule'
```
  
默认情况下 Python 会搜索 Python 自身的系统环境变量（找到安装包所在路径）以及当前目录（用户可能自己创建的模块路径）。
Python 的搜索路径可以通过 sys 模块的 path 变量获取，如下所示：

```python
In [2]: import sys

In [3]: sys.path
Out[3]:
['',
 '/home/zd/anaconda3/bin',
 '/home/zd/anaconda3/lib/python37.zip',
 '/home/zd/anaconda3/lib/python3.7',
 '/home/zd/anaconda3/lib/python3.7/lib-dynload',
 '/home/zd/anaconda3/lib/python3.7/site-packages',
 '/home/zd/anaconda3/lib/python3.7/site-packages/IPython/extensions',
 '/home/zd/.ipython']
```

有两种办法可以添加自定义的搜索路径：一种是修改上面所见的 sys.path 变量，因为它是一个列表，
所以可以通过 append() 方法添加路径（字符串），该操作在 Python 退出后会失效，这意味着每一次进入 Python 都需要重新设置；
另一种方法是设置环境变量 PYTHONPATH，该变量内容会被自动加入到模块搜索路径中，一旦设定，永久有效。
不过该方法需要读者掌握一定系统知识，因此本书不作详细介绍。

## 5.4 章末小结

函数和模块是 Python 用户常见的操作对象，因此熟练地掌握如何使用和创建函数、使用模块极为重要。
本章从函数的使用、创建、参数设定，模块的安装、导入与创建以及相关注意事项方面都作了详尽的介绍，读者在实际的操作中需要多加练习。
关于编写函数与模块有两条注意事项：一个好的函数一般来说调用者（用户）需要设定的参数数目很少，因此读者在编写时需要合适设置一些默认参数；
创建模块时名字不能和 Python 自带的模块名称一样，否则会产生冲突。



