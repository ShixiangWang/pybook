# 第 7 章 Matplotlib

**本章内容提要**：

- Matplotlib库简介
- 基本图形绘制

简单的图形可以给数据分析师带来比其他任何设备更多的信息。在上一章中，本书介绍了Python数据分析最核心的底层库NumPy、基于ndarray对象的数组操作方法与基本统计。本章将开始指引读者从更直观的角度——图形了解数据的分布与规律，学习如何绘制和自定义图形。

## 7.1 Matplotlib入门

### 7.1.1 Matplotlib库简介	

数据可视化是数据分析最核心的工作之一，它既能帮助我们探索数据，如寻找异常值，也能够帮助我们汇总分析结果，即所谓的“一图胜千言”。Python有着众多的库可以进行静态或动态的数据可视化，其中最流行的是Matplotlib（https://matplotlib.org/），本书主要关注它，以它为对象向读者介绍如何使用Matplotlib、合理地选择和创建图形。

Matplotlib库的历史并不是很久远，它是John Hunter在2002年启动的一个项目，目的是为Python构建商业科学计算软件MATLAB的绘图接口，于2003年发布0.1版本。Matplotlib的最重要特点是它可以许多的操作系统和图形后端工作得很好，这意味着我们可以不管使用什么操作系统或是想要什么输出格式的图形（PDF、JPG、PNG、GIF等）都可以依靠它。这种跨平台，一切皆可用的特性成为了Matplotlib最大的长处，并为Matplotlib带来了大量的基础用户和活跃的开发者。

目前，Matplotlib已经和IPython合作，简化了在IPython Shell和Jupyter Notebook中进行交互式绘图的方式。除此之外，Python社区出现了许多以Matplotlib为底层的可视化计算库，其中最有名的是Seaborn（https://seaborn.pydata.org/），在本书后续的章节我们会学习它。

### 7.1.2 通用技巧

在深入了解如何使用Matplotlib创建图形之前，本书先介绍一些Python社区通用的约定和使用技巧。

#### 导入Matplotlib

在导入NumPy包时，我们使用Python社区约定的np替代numpy。这里，我们也使用Matplotlib的一些标准简写用于导入。

```python
In [1]: import matplotlib as mpl
In [2]: import matplotlib.pyplot as plt
```

后续读者将看到，plt是使用Matplotlib绘图最常用的简写，这是因为用户大部分绘图只会用到pyplot子模块中的功能特性。

#### 设置风格

使用plt.style()函数可以为创建的图形设置合适的美学风格。下面代码可以确保生成的图形使用经典的Matplotlib风格：

```python
In [3]: plt.style.use('classic')
```

https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html

### 7.1.3 如何展示图形

Matplotlib最佳的使用方法依赖于用户如何使用它，通常有3种应用绘图的场景：脚本、IPython Shell和Jupyter Notebook。

#### 使用脚本绘制

如果读者想要在脚本中使用Matplotlib，通常需要plt.show()函数发挥作用。该函数会寻找当前活跃的所有图形队形，打开一个或多个交互式的窗口展示图形。

假设下面是代码文件plot.py的内容：

```python
# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
```

接下来在终端中运行该脚本，读者将看到一个显示图形的窗口弹出来。在此处，plt.show()函数在后台进行了多项工作，它与系统的交互式图形后端进行交流，而Matplotlib向我们隐藏了所有的细节。

注意，如果是编写脚本文件进行绘图，一个文件尽量只使用一次plt.show()函数，如果使用多次，图形后端行为将不可预测。

#### 从IPython Shell绘制

在IPython Shell中使用Matplotlib非常方便，如果用户指定Matplotlib模式，IPython可以工作得非常好。启动IPython后键入魔术命令“%matplotlib”能够激活该模式。 

```python
In [4]: %matplotlib
Using matplotlib backend: Qt5Agg

In [5]: import matplotlib.pyplot as plt
```

这时候，调用plt.plot()函数就会打开一个图形窗口，接下来的绘图指令都可以更新这个图。有时候，一些对图形属性的更改不会及时生效，我们可以利用plt.draw()函数强制执行。

#### 在Jupyter Notebook中绘制

在Jupyter Notebook中使用Matplotlib进行交互式绘图也是使用魔术命令“%matplotlib”，它跟在IPython Shell中的工作方式差不多。读者可以使用以下两种选项：

* `%matplotlib notebook`会在Notebook中嵌入交互式图形
* `%matplotlib inline`会在Notebook张嵌入静态图形

最常使用的是第二种方式。

```python
In [1]: %matplotlib inline
```

After running this command (it needs to be done only once per kernel/session), any cell within the notebook that creates a plot will embed a PNG image of the resulting graphic:

```python
In [4]: import numpy as np
		x = np.linspace(0, 10, 100)

		fig = plt.figure()
		plt.plot(x, np.sin(x), '-')
		plt.plot(x, np.cos(x), '--');
```

这一章用ipython notebook写

### 7.1.4 保存图形

### 7.1.5 绘图接口



## 7.2 基本图形绘制

### 7.2.1 线图

### 7.2.2 散点图

### 7.2.3 直方图



### 7.3.4 自定义图形

## 7.4 章末小结



