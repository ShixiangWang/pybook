# 第 13 章 Pandas 进阶

**本章内容提要**:

- 数据清洗
- 数据转换与整合
- DataFrame 进阶？？？
- 探索性数据分析
- 时间序列分析
- 高级索引
- 排序与重塑？？
- 分组计算
- 数据融合？？

![图13-1 Numpy 数组与 Pandas 数据结构对比](images/chapter13/numpy_pandas_comparison.png)

对比 NumPy (np) 和 Pandas (pd) 每个维度下的数据结构，不难看出

pd 多维数据表 = np 多维数组 + 描述

其中

Series = 1darray + index

DataFrame = 2darray + index + columns

Panel = 3darray + index + columns + item


Panel：三维数据。Panel 是 DataFrame 的容器。不过，需要指出的是 Panel 在未来版本中会被废除，因此不想花时间看的同学可跳过。

## 字符串函数

Pandas提供了一组字符串函数，可以方便地对字符串数据进行操作。 最重要的是，这些函数忽略(或排除)丢失/NaN值。
几乎这些方法都使用Python字符串函数(请参阅： http://docs.python.org/3/library/stdtypes.html#string-methods )。 因此，将Series对象转换为String对象，然后执行该操作。

https://www.yiibai.com/pandas/python_pandas_working_with_text_data.html


## 分类数据

https://www.yiibai.com/pandas/python_pandas_categorical_data.html

## 可视化

https://www.yiibai.com/pandas/python_pandas_visualization.html

## 函数应用

要将自定义或其他库的函数应用于Pandas对象，有三个重要的方法，下面来讨论如何使用这些方法。使用适当的方法取决于函数是否期望在整个DataFrame，行或列或元素上进行操作。

表合理函数应用：pipe()行或列函数应用：apply()元素函数应用：applymap()

## 迭代

Pandas对象之间的基本迭代的行为取决于类型。当迭代一个系列时，它被视为数组式，基本迭代产生这些值。其他数据结构，如：DataFrame和Panel，遵循类似惯例迭代对象的键。
简而言之，基本迭代(对于i在对象中)产生 -

Series - 值
DataFrame - 列标签
Pannel - 项目标签

要遍历数据帧(DataFrame)中的行，可以使用以下函数 -

iteritems() - 迭代(key，value)对iterrows() - 将行迭代为(索引，系列)对itertuples() - 以namedtuples的形式迭代行





## 合并


按键 (key) 合并可以分「单键合并」和「多键合并」。



单键合并


单键合并用 merge 函数，语法如下：



    pd.merge( df1, df2, how=s, on=c )



c 是 df1 和 df2 共有的一栏，合并方式 (how=s) 有四种：



左连接 (left join)：合并之后显示 df1 的所有行

右连接 (right join)：合并之后显示 df2 的所有行

外连接 (outer join)：合并 df1 和 df2 共有的所有行

内连接 (inner join)：合并所有行 (默认情况)


left join
pd.merge( df_price, df_volume, how='left' )

right join
pd.merge( df_price, df_volume, how='right' )

outer join
pd.merge( df_price, df_volume, how='outer' )

inner join
pd.merge( df_price, df_volume, how='inner' )


多键合并


多键合并用的语法和单键合并一样，只不过 on=c 中的 c 是多栏。

    pd.merge( df1, df2, how=s, on=c )


当 df1 和 df2 有两个相同的列 (Asset 和 Instrument) 时，单单只对一列 (Asset) 做合并产出的 DataFrame 会有另一列 (Instrument) 重复的名称。这时 merge 函数给重复的名称加个后缀 _x, _y 等等。

如果觉得后缀 _x, _y 没有什么具体含义时，可以设定 suffixes 来改后缀。比如 df1 和 df2 存储的是 portoflio1 和 portfolio2 的产品信息，那么将后缀该成 ‘1’ 和 ‘2’ 更贴切。

## 连接

Numpy 数组可相互连接，用 np.concat；同理，Series 也可相互连接，DataFrame 也可相互连接，用 pd.concat。



连接 Series


在 concat 函数也可设定参数 axis，



axis = 0 (默认)，沿着轴 0 (行) 连接，得到一个更长的 Series

axis = 1，沿着轴 1 (列) 连接，得到一个 DataFrame



被连接的 Series 它们的 index 可以重复 (overlapping)，也可以不同。



overlapping index
先定义三个 Series，它们的 index 各不同。

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])


沿着「轴 0」连接得到一个更长的 Series。

pd.concat([s1, s2, s3])

将 s1 和 s3 沿「轴 0」连接来创建 s4，这样 s4 和 s1 的 index 是有重复的。

将 s1 和 s4 沿「轴 1」内连接 (即只连接它们共有 index 对应的值)

pd.concat([s1, s4], axis=1, join='inner')

hierarchical index
最后还可以将 n 个 Series 沿「轴 0」连接起来，再赋予 3 个 keys 创建多层 Series。

连接 DataFrame 的逻辑和连接 Series 的一模一样。



沿着行连接 (axis = 0)

沿着行连接分两步



先把 df1 和 df2 列标签补齐

再把 df1 和 df2 纵向连起来

pd.concat( [df1, df2] )


得到的 DataFrame 的 index = [0,1,2,0,1]，有重复值。如果 index 不包含重要信息 (如上例)，可以将 ignore_index 设置为 True，这样就得到默认的 index 值了。

沿着列连接 (axis = 1)
先创建两个 DataFrame，df1 和 df2。

df1 = pd.DataFrame( np.arange(6).reshape(3,2), 
                    index=['a','b','c'],
                    columns=['one','two'] )
df1

沿着列连接分两步



先把 df1 和 df2 行标签补齐

再把 df1 和 df2 横向连起来

5数据表的重塑和透视


重塑 (reshape) 和透视 (pivot) 两个操作只改变数据表的布局 (layout)：



重塑用 stack 和 unstack 函数 (互为逆转操作)

透视用 pivot 和 melt 函数 (互为逆转操作)

## 重塑

DataFrame 和「多层索引的 Series」其实维度是一样，只是展示形式不同。而重塑就是通过改变数据表里面的「行索引」和「列索引」来改变展示形式。



列索引 → 行索引，用 stack 函数

行索引 → 列索引，用 unstack 函数


创建 DataFrame df (1 层行索引，1 层列索引)

symbol = ['JD', 'AAPL']
data = {'行业': ['电商', '科技'],
        '价格': [25.95, 172.97],
        '交易量': [27113291, 18913154]}
df = pd.DataFrame( data, index=symbol )
df.columns.name = '特征'
df.index.name = '代号'
df

stack: 列索引 → 行索引
列索引 (特征) 变成了行索引，原来的 DataFrame df 变成了两层 Series (第一层索引是代号，第二层索引是特征)。

c2i_Series = df.stack()
c2i_Series

unstack: 行索引 → 列索引
行索引 (代号) 变成了列索引，原来的 DataFrame df 也变成了两层 Series (第一层索引是特征，第二层索引是代号)。

i2c_Series = df.unstack()
i2c_Series

规律总结
对 df 做 stack 和 unstack 都得到了「两层 Series」，但是索引的层次不同，那么在背后的规律是什么？首先我们先来看看两个「两层 Series」的 index 包含哪些信息 (以及 df 的 index 和 columns)。

现在可以总结规律：



当用 stack 将 df 变成 c2i_Series 时，df 的列索引 c 加在其行索引 r 后面得到 [r, c] 做为 c2i_Series 的多层索引



当用 unstack 将 df 变成 i2c_Series 时，df 的行索引 r 加在其列索引 c 后面得到 [c, r] 做为 i2c_Series 的多层索引



基于层和名称来 unstack
对于多层索引的 Series，unstack 哪一层有两种方法来确定：



基于层 (level-based)

基于名称 (name-based)




1. 基于层来 unstack() 时，没有填层数，默认为最后一层。

2. 基于层来 unstack() 时，选择第一层 (参数放 0)

c2i_Series.unstack(0)


3. 基于名称来 unstack 

c2i_Series.unstack('代号')


多层 DataFrame


创建 DataFrame df (2 层行索引，1 层列索引)

data = [ ['电商', 101550, 176.92], 
         ['电商', 175336, 25.95], 
         ['金融', 60348, 41.79], 
         ['金融', 36600, 196.00] ]

midx = pd.MultiIndex( levels=[['中国','美国'],
                              ['BABA', 'JD', 'GS', 'MS']], 
                      labels=[[0,0,1,1],[0,1,2,3]],
                      names = ['地区', '代号'])

mcol = pd.Index(['行业','雇员','价格'], name='特征')

df = pd.DataFrame( data, index=midx, columns=mcol )
df

## 透视

数据源表通常只包含行和列，那么经常有重复值出现在各列下，因而导致源表不能传递有价值的信息。这时可用「透视」方法调整源表的布局用作更清晰的展示。



知识点
本节「透视」得到的数据表和 Excel 里面的透视表 (pivot table) 是一样的。透视表是用来汇总其它表的数据：

首先把源表分组，将不同值当做行 (row)、列 (column) 和值 (value)


然后对各组内数据做汇总操作如排序、平均、累加、计数等


这种动态将·「源表」得到想要「终表」的旋转 (pivoting) 过程，使透视表得以命名。


在 Pandas 里透视的方法有两种：



用 pivot 函数将「一张长表」变「多张宽表」，

用 melt 函数将「多张宽表」变「一张长表」，


从长到宽 (pivot)



当我们做数据分析时，只关注不同股票在不同日期下的 Adj Close，那么可用 pivot 函数可将原始 data「透视」成一个新的 DataFrame，起名 close_price。在 pivot 函数中



将 index 设置成 ‘Date’

将 columns 设置成 ‘Symbol’

将 values 设置 ‘Adj Close’



close_price 实际上把 data[‘Date’] 和 data[‘Symbol’] 的唯一值当成支点(pivot 就是支点的意思) 创建一个 DataFrame，其中



行标签 = 2019-02-21, 2019-02-22, 2019-02-25, 2019-02-26

列标签 = AAPL, JD, BABA, FB, GS



在把 data[‘Adj Close’] 的值放在以如上的行标签和列标签创建的 close_price 来展示。


从宽到长 (melt)


pivot 逆反操作是 melt。



前者将「一张长表」变成「多张宽表」

后者将「多张宽表」变成「一张长表」



具体来说，函数 melt 实际是将「源表」转化成 id-variable 类型的 DataFrame，下例将



Date 和 Symbol 列当成 id

其他列 Open, High, Low, Close, Adj Close 和 Volume 当成 variable，而它们对应的值当成 value

## 分组计算

用某一特定标签 (label) 将数据 (data) 分组的语法如下：



    data.groupBy( label )



单标签分组
首先我们按 Symbol 来分组：

grouped = data1.groupby('Symbol')
grouped
<pandas.core.groupby.groupby.DataFrameGroupBy
object at 0x7fbbc7248d68>


又要提起那句说了无数遍的话「万物皆对象」了。这个 grouped 也不例外，当你对如果使用某个对象感到迷茫时，用 dir() 来查看它的「属性」和「内置方法」。以下几个属性和方法是我们感兴趣的：



ngroups: 组的个数 (int)

size(): 每组元素的个数 (Series)

groups: 每组元素在原 DataFrame 中的索引信息 (dict)

get_groups(label): 标签 label 对应的数据 (DataFrame)



下面看看这些属性和方法的产出结果。

多标签分组
groupBy 函数除了支持单标签分组，也支持多标签分组 (将标签放入一个列表中)。

grouped2 = data1.groupby(['Symbol', 'Year', 'Month'])
print_groups( grouped2 )

6.3

整合 (aggregating)



做完分组之后 so what？当然是在每组做点数据分析再整合啦。



一个最简单的例子就是上节提到的 size() 函数，用 grouped 对象 (上面根据 Symbol 分组得到的) 来举例。

grouped.size()


除了上述方法，整合还可以用内置函数 aggregate() 或 agg() 作用到「组对象」上。用 grouped4 对象 (上面根据 Symbol, Year, Month 分组得到的) 来举例。

result = grouped4.agg( np.mean )
result.head().append(result.tail())

6.4

split-apply-combine



前几节做的事情的实质就是一个 split-apply-combine 的过程，如下图所示：

https://mmbiz.qpic.cn/mmbiz_png/e4kxNicDVcCGMVUbnH2BxNCcAgACx6iblP6pLTxaHdhwy3TViaaW8RoqrRYwMEyJQgGYBUoDTmiaE2QpJt85cIDvIg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1


该 split-apply-combine 过程有三步：



根据 key 来 split 成 n 组

将函数 apply 到每个组

把 n 组的结果 combine 起来

Apply 函数
在 split-apply-combine 过程中，apply 是核心。Python 本身有高阶函数 apply() 来实现它，既然是高阶函数，参数可以是另外的函数了，比如刚定义好的 top()。



将 top() 函数 apply 到按 Symbol 分的每个组上，按每个 Symbol 打印出来了 Volume 栏下的 5 个最大值。

data.groupby('Symbol').apply(top)

7总结


【合并数据表】用 merge 函数按数据表的共有列进行左/右/内/外合并。

【连接数据表】用 concat 函数对 Series 和 DataFrame 沿着不同轴连接。



【重塑数据表】用 stack 函数将「列索引」变成「行索引」，用 unstack 函数将「行索引」变成「列索引」。它们只是改变数据表的布局和展示方式而已。


【透视数据表】用 pivot 函数将「一张长表」变成「多张宽表」，用 melt 函数将「多张宽表」变成「一张长表」。它们只是改变数据表的布局和展示方式而已。

【分组数据表】用 groupBy 函数按不同「列索引」下的值分组。一个「列索引」或多个「列索引」就可以。



【整合数据表】用 agg 函数对每个组做整合而计算统计量。



【split-apply-combine】用 apply 函数做数据分析时美滋滋。

## 选项和自定义

https://www.yiibai.com/pandas/python_pandas_options_and_customization.html

Pandas提供API来自定义其行为的某些方面，大多使用来显示。
API由五个相关函数组成。它们分别是 -

get_option()
set_option()
reset_option()
describe_option()
option_context()


## 时间序列

### 日期

https://www.yiibai.com/pandas/python_pandas_date_functionality.html


### 时间差

https://www.yiibai.com/pandas/python_pandas_timedelta.html