# 第 9 章 Markdown 基础 {#markdown}

**本章内容提要**：

- 为什么学习 Markdown
- Markdown 支持软件
- Markdown 基础语法
- Markdown 文档范例

xxx简要介绍

## 9.1 Markdown 简介

Markdown 由 John Gruber 于 2004 年创建，它是一种轻量级标记语言。轻量级标记语言是指一类用简单语法表述文字格式的文本语言，
即直接能从字面上进行阅读和理解。Markdown 的目的是提供一种容易阅读、容易书写的纯文字格式，它吸收了电子邮件中许多已有的标记特性，
并可以有效地转换为富文本语言，如 HTML。

由于 Markdown 轻量、易读、易写的特性，并且支持图片、表格、数学公式，目前许多网站都采用 Markdown 来编写帮助文档或发布消息，
比较有名的有 GitHub、reddit 和 Stack Overflow。另外，Markdown 也常用与博文、书籍的撰写。
甚至当前网络应用、App 专门提供 Markdown 服务，如简书、Slack。

随着时间的推移，出现了许多 Markdown 的实现。这些实现的目的是在 Markdown 基础语法之上添加一些额外的功能，
如列表、脚注等。另外，在数据分析领域，一种新型的文档出现了，它可以将文本嵌入运行的代码中，称为动态文档，
而文本书写的语法正是 Markdown。目前流行的动态文档主要有 2 种，一种是 Jupyter Notebook，它支持多种编程语言，
包括 R、Python；另一种是 Rmarkdown，它在 Markdown 的基础上增加了 R 语言代码块的
执行功能（也有对 Python、Shell 的支持，但功能较弱）。

动态文档的出现使得数据分析不再像是在写单纯的功能脚本，而是图文并茂的文章，而且增强了交互性和可重复性，
已经是当下数据分析人员必备的一个技能之一。
在本章接下来的内容中，本书将对 Markdown 的基础语法进行简要介绍并结合 Python 分析实际使用进行举例。

## 9.2 Markdown 语法

### 9.2.1 块元素

#### 段落

Markdown 中，段落是通过一个及以上空行来分割的。如下所示：

```
这是第一段话

这是第二段话
```

如果只是使用回车键，内容还是属于一段，文字是连接起来的。
例如，「这是第一句话。这是第二句话。」可以写为如下形式：

```
这是第一句话。
这是第二句话。
```

#### 标题

Markdown 支持 6 级标题，一般前四级比较常用。
指定标题的方式是在文字前面添加井号键，有几个就是几级标题。

```
# 这是一级标题

## 这是二级标题

### 这是三级标题

#### 这是四级标题

##### 这是五级标题

###### 这是六级标题
```

注意井号后面加一个空格。

#### 引用

Markdown使用符号 > 起始一段块引用。引用也可以有多段文字，换行以单独的 > 为一行。

```
> 这里有3段引用，前面2段引用是在一起的，最后一段引用是独立的。
>
> 这是第2段引用。


> 这是第3段引用。
```

下面则是 Markdown 显示的效果。

> 这里有3段引用，前面2段引用是在一起的，最后一段引用是独立的。
>
> 这是第2段引用。


> 这是第3段引用。

#### 列表

输入「\* 元素1」就可以创建一个无序列表，除了使用星号 \*，还可以使用 +、-。一般常用 \* 或者 -。
而输入「1. 元素1」可以创建有序列表。

Markdown 源代码如下：

```
## 无序列表

* 石头
* 剪刀
* 布

## 有序列表

1. 石头
2. 剪刀
3. 布
```

#### 任务列表

在列表符号后面使用 [ ] 或 [x] 可以分别标记未完成或完成状态。例如：

```
## 作业完成情况

- [ ] 语文
- [x] 数学
- [ ] 物理
- [ ] 英语
- [x] 化学
```

注意，标记未完成时括号内一定要有一个空格。

#### 代码块

代码块以 3 个符号 \` 起始（键盘上<ESC>键下方的撇号），同样以 3 个 \` 结束。
除了对代码格式比较友好，很多支持 Markdown 的工具、网站对代码块都自动高亮的功能。

~~~gfm
下面是一个例子：

```
def test():
    print("Hello World!")
```


语法高亮：

```python
def test():
    print("语法高亮")
```
~~~

#### 数学块

有不少 Markdown 编辑器通过 MathJax 支持 LaTex 数学表达式。


数学公式使用两个美元符 \$\$ 开始和结束。

```
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$
```

效果如下：

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$

这里只是展示 Markdown 支持这种数学公式，LaTex 语法本身读者需要参考其他资料学习使用。

#### 表格

使用「|列1|列2|」就可以添加 2 列表格，标题行和内容行使用「|---|」进行分隔。

```
| 标题1   | 标题2 |
| -------| ----- |
| Cell1  | Cell3 |
| Cell2  | Cell4 |
```

| 标题1   | 标题2 |
| -------| ----- |
| Cell1  | Cell3 |
| Cell2  | Cell4 |

对齐可以通过对分隔行增加英文冒号 : 标记实现。

```
| 左对齐  | 中心对齐 | 右对齐 |
| :----- |:-------:| -----:|
| c1     | 这一列   | $16 |
| c2     | 是中心   | $120 |
| c3     | 对齐     | $11 |
```

| 左对齐  | 中心对齐 | 右对齐 |
| :----- |:-------:| -----:|
| c1     | 这一列   | $16 |
| c2     | 是中心   | $120 |
| c3     | 对齐     | $11 |

#### 脚注

```
你可以像这样添加脚注[^footnote]。

[^footnote]: 这是一段脚注文字
```

效果如下：

你可以像这样添加脚注[^footnote]。

[^footnote]: 这是一段脚注文字


#### 水平线

在空行中使用 \*\*\* 或者 --- 就可以生成一条水平分隔线。

### 9.2.2 内联元素

#### 链接

Markdown 支持行内和参考两种链接方式，链接的文字都是写在方括号内。

行内链接的写法如下：

```
[这个链接](https://baidu.com)会跳转到百度
```

[这个链接](https://baidu.com)会跳转到百度

参考链接的写法如下：

```
[这个链接][id]会跳转到百度

[id]: https://baidu.com
```

[这个链接][id]会跳转到百度

[id]: https://baidu.com

#### URL

URL 使用 2 个尖括号将文本包围，与链接不同的是 URL 的显示的就是尖括号内的文字，不能自定义显示内容。


```
<https://baidu.com>

<xxx@163.com>
```

<https://baidu.com>

<xxx@163.com>


#### 图片

图片跟链接相似，但是需要在链接的前面添加一个英文感叹号 ! 符号。

```
![说明文字](图片路径.jpg)
![说明文字](图片路径.png)
```

![](https://www.baidu.com/img/dong_96c3c31cae66e61ed02644d732fcd5f8.gif)

路径可以是 URL，可以是计算机本地的绝对路径或相对路径。

#### 强调与加粗

Markdown 使用星号或下划线强调文字。

```
*使用星号*

_使用下划线_
```

*使用星号*

_使用下划线_


使用两个符号则是进行加粗。

```
**使用2个星号**

__使用2个下划线__
```

#### 删除线

Markdown 使用2个波浪线 ~ 对文字进行删除标记。

```
~~这是一段被删除线标记的文字~~
```

~~这是一段被删除线标记的文字~~

#### 下划线

下划线需要原生 HTML 标签支持。

```
<u>这段文字会被下划线标记</u>
```

<u>这段文字会被下划线标记</u>

#### 上标与下标

Markdown 上标使用单个波浪号 ~，下标使用 ^。下面写法可以创建水分子和 X 的平方。

```
H~2~O

X^2^
```

H~2~O

X^2^


#### 行内代码

前面提到了代码块，但有时候代码很短，需要使用行内代码，这时候用单个的符号 \` 即可。

```

`x = y = 3`

```

`x = y = 3`

#### 行内公式

行内公式使用单个美元符 \$ 开始和结束：

```
$y = a \times x + b$
```

效果如下：

$y = a \times x + b$


## 9.3 联合 Python 与 Markdown

上节提到的 Markdown 语法内容颇多，它们虽然简单，但也需要时间学习和掌握。
本节以「绘制引力波曲线」为题写一个简单的 Markdown 文章，以帮助读者对 Markdown 的整体使用有更深的了解。

~~~gfm
# 绘制引力波曲线

## 数据下载与准备

第一个引力波文件：[H1_Strain.wav](http://python123.io/dv/H1_Strain.wav)

第二个引力波文件：[L1_Strain.wav](http://python123.io/dv/L1_Strain.wav)

引力波参考文件：[wf_template.txt](http://python123.io/dv/wf_template.txt)

## 导入包

```
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.io import wavfile
```

## 导入数据

```
  rate_h, hstrain= wavfile.read(r"H1_Strain.wav","rb")
  rate_l, lstrain= wavfile.read(r"L1_Strain.wav","rb")
  ​
  reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose() #使用python123.io下载文件
  # website:      http://python123.io/dv/grawave.html
   
  htime_interval = 1/rate_h
  ltime_interval = 1/rate_l
  fig = plt.figure(figsize=(12, 6))
```

```
  # 丢失信号起始点
  htime_len = hstrain.shape[0]/rate_h
  htime = np.arange(-htime_len/2, htime_len/2 , htime_interval)
  plth = fig.add_subplot(221)
  plth.plot(htime, hstrain, 'y')
  plth.set_xlabel('Time (seconds)')
  plth.set_ylabel('H1 Strain')
  plth.set_title('H1 Strain')
```

```
  ltime_len = lstrain.shape[0]/rate_l
  ltime = np.arange(-ltime_len/2, ltime_len/2 , ltime_interval)
  pltl = fig.add_subplot(222)
  pltl.plot(ltime, lstrain, 'g')
  pltl.set_xlabel('Time (seconds)')
  pltl.set_ylabel('L1 Strain')
  pltl.set_title('L1 Strain')
   
  pltref = fig.add_subplot(212)
  pltref.plot(reftime, ref_H1)
  pltref.set_xlabel('Time (seconds)')
  pltref.set_ylabel('Template Strain')
  pltref.set_title('Template')
  fig.tight_layout()
   
  plt.savefig("Gravitational_Waves_Original.png")
  plt.show()
  plt.close(fig)
```
~~~

![](https://upload-images.jianshu.io/upload_images/3884693-5b47a4c4dee32cbc.png)


## 9.4 章末小结

