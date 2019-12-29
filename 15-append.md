# 第 15 章 未言及的内容

**本章内容提要**:

- 魔术命令
- 面向对象编程

本章作为全书的最后一个章节，附加介绍两个未言及但可能有用的内容：第一个是 IPython 的魔术命令，第二个是面向对象编程知识。

## 15.1 魔术命令

魔术命令是 IPython 在 Python 语法基础上增强的功能，一般以 % 作为前缀，魔术命令用于简洁地解决标准数据分析中的各种常见问题，如列出当前目录文件，运行脚本。

下面列出了一些常见的魔术命令和它的描述。

```python
%paste  # 粘贴代码
%run    # 执行外部脚本
%timeit # 计算代码运行时间
%magic  # 获取可用魔术命令描述与示例
%lsmagic # 获取可用魔术命令列表
%ls  # 列出当前目录列表
%pwd # 获取当前所在（工作）目录
%cd  # 切换工作目录
%mkdir # 创建文件夹
%cp # 拷贝文件
%rm # 删除文件
```

魔术命令相当有用，它解决了数据分析时想要实时与系统进行交互并测试代码的痛点。

在 IPython Shell 或 Jupyter Notebook 中输入 %lsmagic 即可查看所有的魔术命令。

```python
In [4]: %lsmagic                                                  
Out[4]: 
Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %autoindent  %automagic  %bookmark  %cat  %cd  %clear  %colors  %conda  %config  %cp  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %m
an  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %
pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %
unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%sv
g  %%sx  %%system  %%time  %%timeit  %%writefile

Automagic is ON, % prefix IS NOT needed for line magics.
```

一般而言，魔术命令的作用可以通过名字进行猜测。如果我们不确定，可以在后面跟一个问号查看对应的文档。

```python
In [5]: %ls?                                                
Repr: <alias ls for 'ls -F --color'>
```

结果显示 %ls 命令是 ls -F 命令的缩写，ls 命令是 Unix 系统进行文件管理的命令之一，用于查看目录下的文件列表。其他的 Unix 命令都有魔术命令的相应实现，包括 mkdir、cp、pwd 等。

运行 %ls 命令，发现当前目录下没有任何文件或目录。

```python
In [6]: %ls 

```

我们使用 %mkdir 创建一个目录 new 再次进行检查。

```python
In [7]: %mkdir new
In [8]: %ls                                                       
new/
```

使用 %pwd 查看我们工作目录在操作系统中的位置。

```python
In [9]: %pwd                                                   
Out[9]: '/home/shixiang/Proj/pybook/test_ipython_shell'
```

使用 %cd 切换到另一个目录，如上面新建的 new 目录。

```python
In [10]: %cd new                                          
/home/shixiang/Proj/pybook/test_ipython_shell/new
In [11]: %pwd                                               
Out[11]: '/home/shixiang/Proj/pybook/test_ipython_shell/new'
```

%timeit 是一个非常有用的魔术命令，它可以计算 Python 代码的执行时间。

```python
In [12]: %timeit Result = [i ** 2 for i in range(100)]                                          
47.6 µs ± 386 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

该命令会自动多次执行命令（10000 次）以获得稳定的结果，当使用多行输入时我们需要对命令多加一个百分号。

```python
In [13]: %%timeit 
    ...: Result = [] 
    ...: for i in range(100): 
    ...:     Result.append(i * i) 
    ...:                                                                                                                                                                                     
16.7 µs ± 178 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

## 15.2 面向对象编程

 面向对象编程（object-oriented programming，OOP）是许多编程语言都有的特性，Python 也不例外。
 不过，数据处理和分析时我们一般很少自己创建自定义的类，除非是开发一些数据处理工具软件，用类来表示一些核心的数据结构，如 Pandas 库的 DataFrame。
 本节向读者简单介绍面向对象编程的一些基本概念和操作方法，以便于读者能够了解这一前面遗漏的 Python 基础知识。

面向对象的核心概念是类（Class）和实例或对象（Object），类是对象的蓝图，对象是类的实例化。如学生是一个类，某学生小周就是一个对象。

我们假设学生有名字、年龄、身高和成绩 4 个属性，使用 Python 创建一个 Student 类如下：

```python
In [1]: class Student:  
   ...:     def __init__(self, name, age, height, score): 
   ...:         self.name = name 
   ...:         self.age = age 
   ...:         self.height = height 
   ...:         self.score = score 
```

有了类以后，我们可以创建不同的学生实例，如小周、小张、小李等等。

类中定义的函数称为方法，每个类都需要一个 \_\_init\_\_() 函数用于初始化。类的方法第一个参数永远是 self，指向其本身。
后续的参数就是用户可以实际输入的参数，我们按照格式就可以创建一个对象。 

```python
In [2]: Student('小周', 20, 180, 98)                                                    
Out[2]: <__main__.Student at 0x7fe95c4eeb50>
```

在方法中我们可以执行计算或者将一些数据存储起来，存储数据的变量称为类的属性。如初始化函数中的 self.name、self.age 等。

当我们创建好一个对象后，我们可以使用成员操作符获取对象的属性值。

```python
In [3]: zhou = Student('小周', 20, 180, 98)
In [4]: zhou.score                                                
Out[4]: 98
In [5]: zhou.height                                                    
Out[5]: 180
In [6]: zhou.age                                                     
Out[6]: 20
```

除了初始化方法，我们还可以定义其他方法进行计算。例如某班级的平均分为 70 分，我们定义一个方法计算
小周成绩与班级平均分的差值。

我们先为 Student 类加上计算差值的方法：

```python
In [7]: class Student:  
   ...:     def __init__(self, name, age, height, score): 
   ...:         self.name = name 
   ...:         self.age = age 
   ...:         self.height = height 
   ...:         self.score = score 
   ...:     def diff(self, average_score): 
   ...:         print(self.score - average_score) 
   ...:     
```

重新创建对象 zhou：

```python
zhou = Student('小周', 20, 180, 98)
```

计算差值：

```python
In [9]: zhou.diff(70)                                                    
28
```

基于上面的知识，我们可以根据自己的需要创建类并添加任意多的属性和方法。

面向对象编程还有一个比较重要的概念是继承（Inheritance），它可以有效地代表不同类的层级
关系和重用代码。

例如，上面我们以及创建了一个 Student 类，现在我们想要创建一个 Studnet2 类，该类在 Student
类的基础上多了两个属性 class_name 和 teacher_name 用来表示班级名和班主任名字。

实现代码如下：

```python
In [15]: class Student2(Student): 
    ...:     def __init__(self, name, age, height, score, class_name, teacher_name): 
    ...:         Student.__init__(self, name, age, height, score) 
    ...:         self.class_name = class_name 
    ...:         self.teacher_name = teacher_name 
    ...:                     
```

注意，在新的类初始化方法中，我们需要调用 Student 类的初始化。接着我们重新创建一个新的对象 zhou。

```python
In [16]: zhou = Student2('小周', 20, 180, 98, "Class A", "Mr. Zhang")    
```

我们依然可以使用 Student 类的属性和方法。

```python
In [17]: zhou.name                                                        
Out[17]: '小周'
In [18]: zhou.diff(70)                                                    
28
```

## 15.3 章末小结

本章介绍了 IPython 魔术命令和面向对象编程两个补充内容。了解和掌握常见的魔术命令是非常有用的，
它可以辅助读者快速地与操作系统进行交互、完成一些常见任务。面向对象编程则提供了新的编程视角，
虽然自定义类在数据分析中不常用，但它依然适用于解决一些特定的问题，以及辅助读者了解常见分析库中
一些类的使用，如 NumPy 中的 ndarray 和 Pandas 中的 DataFrame。