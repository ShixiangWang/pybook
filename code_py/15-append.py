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
In [4]: %lsmagic
# Out[4]:
Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %autoindent  %automagic  %bookmark  %cat  %cd  %clear  %colors  %conda  %config  %cp  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %m
an  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %
pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %
unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%sv
g  %%sx  %%system  %%time  %%timeit  %%writefile

Automagic is ON, % prefix IS NOT needed for line magics.
In [5]: %ls?
Repr: <alias ls for 'ls -F --color'>
In [6]: %ls

In [7]: %mkdir new
In [8]: %ls
new/
In [9]: %pwd
# Out[9]: '/home/shixiang/Proj/pybook/test_ipython_shell'
In [10]: %cd new
/home/shixiang/Proj/pybook/test_ipython_shell/new
In [11]: %pwd
# Out[11]: '/home/shixiang/Proj/pybook/test_ipython_shell/new'
In [12]: %timeit Result = [i ** 2 for i in range(100)]
47.6 µs ± 386 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
In [13]: %%timeit
    ...: Result = []
    ...: for i in range(100):
    ...:     Result.append(i * i)
    ...:
16.7 µs ± 178 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
In [1]: class Student:
   ...:     def __init__(self, name, age, height, score):
   ...:         self.name = name
   ...:         self.age = age
   ...:         self.height = height
   ...:         self.score = score
In [2]: Student('小周', 20, 180, 98)
# Out[2]: <__main__.Student at 0x7fe95c4eeb50>
In [3]: zhou = Student('小周', 20, 180, 98)
In [4]: zhou.score
# Out[4]: 98
In [5]: zhou.height
# Out[5]: 180
In [6]: zhou.age
# Out[6]: 20
In [7]: class Student:
   ...:     def __init__(self, name, age, height, score):
   ...:         self.name = name
   ...:         self.age = age
   ...:         self.height = height
   ...:         self.score = score
   ...:     def diff(self, average_score):
   ...:         print(self.score - average_score)
   ...:
zhou = Student('小周', 20, 180, 98)
In [9]: zhou.diff(70)
28
In [15]: class Student2(Student):
    ...:     def __init__(self, name, age, height, score, class_name, teacher_name):
    ...:         Student.__init__(self, name, age, height, score)
    ...:         self.class_name = class_name
    ...:         self.teacher_name = teacher_name
    ...:
In [16]: zhou = Student2('小周', 20, 180, 98, "Class A", "Mr. Zhang")
In [17]: zhou.name
# Out[17]: '小周'
In [18]: zhou.diff(70)
28
