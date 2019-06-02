# 第8章 Pandas入门 {#pandas-intro}

**本章内容提要**：

- Pandas数据结构介绍
- Series与DataFrame的创建
- Pandas对象索引与操作
- 基本统计分析

虽然NumPy库构成了Python数据科学计算的基石，但我们在实际进行数据处理时极少会使用到它。Python数据科学家/分析师们首选的工具是Pandas库，它强大的数据结构和灵活实用的操作、函数/方法征服了整个Python科学社区。本章将对Pandas的数据结构和基本操作方法进行介绍。

## 8.1 Pandas简介

Pandas的名字来自面板数据（Panel data）和数据分析（Data analysis）的组合，最初由AQR Capital Management于2008年开发，2009年底开源并逐步成长为Python的核心计算分析工具。Pandas库最初的目的是服务于金融分析，因此对时间序列分析有非常好的支持。

Pandas库基于NumPy库构建，纳入了大量计算分析库和标准的数据模型，比如由R语言数据框对象data.frame启发创建了著名的DataFrame数据结构。来自NumPy库的底层支持和高效数据结构表征和操作方法的实现让使用Pandas库清洗和分析数据变得快速又简单。

Pandas采用了NumPy库的编码风格，不过前者聚焦于表格和混杂数据的处理，而后者则适合数值数组数据的处理和计算分析。日常的商业和科研数据处理分析工作者面对的正是大量的表格和混杂数据，因此Pandas非常实用且应用广泛。

在正式学习Pandas之前，读者需要了解Pandas库导入约定：

```
import pandas as pd
```

而Pandas提供的数据结构Series和DataFrame使用非常频繁，所以直接将它们导入当前命名空间会非常方便：

```
from pandas import Series, DataFrame
```

## 8.2 Pandas的数据结构

Pandas主要有两个数据结构：Series和DataFrame，它们的存在可以帮助数据分析人员更容易地存储数据、高效地处理数据。日常的分析任务几乎都可以通过Pandas完成。

### 8.2.1 Series

Series形似字典，包含索引（也称数据标签）和数据两部分。不过，Pandas库是基于NumPy库构建的，所以Series实际上是通过一维的NumPy数组实现的。

下面代码分别使用了字典、NumPy数组和Series存储0、1、2。

```python
In [1]: import pandas as pd

In [2]: import numpy as np

In [4]: {'0':0, '1':1, '2': 2}
Out[4]: {'0': 0, '1': 1, '2': 2}

In [5]: np.arange(3)
Out[5]: array([0, 1, 2])

In [6]: pd.Series(range(3))
Out[6]: 
0    0
1    1
2    2
dtype: int64
```

读者可以看到，3种方式存储的数据是一致的，但Series对象的输出形式与前两者有所不同，它更方便理解和观察：左侧显示了数据标签，右侧显示了数据值，下方显示数据的类型是64位整型。

上面我们给`Series()`函数只传入了一个数据序列，并没有设置索引，因而函数会自动创建一个从0开始、与数据长度相同的整数型索引。读者可以使用index和values属性获取Series对象的标签和索引，下面展示了一个例子：

```python
In [7]: scores = pd.Series([80, 90, 97])

In [8]: scores.index
Out[8]: RangeIndex(start=0, stop=3, step=1)

In [9]: scores.values
Out[9]: array([80, 90, 97])
```

`scores.values`的结果证实了Series对象的数据值的确是一个一维的ndarray。`scores.index`的结果显示Series对象的索引是一个`RangeIndex`对象，它`range(3)`类似，这样存储的好处是当数据很大时，只需要3个信息：起点、终点和步长就可以表示所有的索引值。

在一般的情况下，我们希望数据索引能表示有更为明确含义的信息。例如，上面`scores`实际存储了某位同学的语数外成绩，下面的设置能够让这信息显示得更完整：

```python
In [10]: scores = pd.Series([80, 90, 97], index=[u'语文',u'数学',u'外语'])

In [11]: scores
Out[11]: 
语文    80
数学    90
外语    97
dtype: int64

In [12]: scores.index                                                                                      
Out[12]: Index(['语文', '数学', '外语'], dtype='object')

In [13]: scores.values                                                                                     
Out[13]: array([80, 90, 97])
```

读者通过对已经创建好的Series对象属性重新进行赋值，可以修改该对象。例如，我们将标签修改为英文或者是更改语文成绩为95。

```python
In [14]: scores2 = scores  # 创建一个新拷贝                                                                                  
In [15]: scores2.index = ['Chinese', 'Math', 'English']            

In [16]: scores2.values[0] = 95                                                                            
In [17]: scores2                                                                                           
Out[17]: 
Chinese    95
Math       90
English    97
dtype: int64

```

注意，上述将`scores`赋值为`scores2`后，修改`scores2`也会造成`scores`的修改。如果不想要它们相互影响，应当使用`copy()`方法生成`scores2`。

```python
In [19]: scores                                                                                            
Out[19]: 
Chinese    95
Math       90
English    97
dtype: int64

```

与字典操作相似，Series对象可以通过索引获取对象的值，索引可以是单个的值或是列表。

```python
In [21]: scores[['Math', 'Chinese']]                                                                       
Out[21]: 
Math       90
Chinese    95
dtype: int64

In [22]: scores['Math']                                                                                    
Out[22]: 90
```

当然，直接使用整数下标也是可行的。

Series结构上与字典非常相似，除了上述从列表创建Series，也可以直接通过字典创建。

```python
In [23]: score_dict = {u'语文':95, u'数学':90, u'外语':97}                          

In [24]: scores3 = pd.Series(score_dict)                                            

In [25]: scores3                                                                    
Out[25]: 
语文    95
数学    90
外语    97
dtype: int64
```

一些针对字典的操作也可以用于Series中，如判断'外语'是否存在。

```python
In [26]: u'外语' in scores3                                                         
Out[26]: True

In [27]: u'物理' in scores3                                                         
Out[27]: False
```

除了index与values属性，Series对象本身及其索引都有一个name属性，该属性可以用来设定更明确的数据含义。

```python
In [29]: scores3.name = 'xx中学期中成绩'                                            

In [30]: scores3.index.name = '学科'                                                

In [31]: scores3                                                                    
Out[31]: 
学科
语文    95
数学    90
外语    97
Name: xx中学期中成绩, dtype: int64
```

### 8.2.2 DataFrame

Series对象只能有效地表示一维的数据，而数据分析工作常常面对的是表格类型的数据，即一组有序的数据列，每一列都可以是不同的数据类型。Pandas库引入了DataFrame（中文念作“数据框”）用以表征表格数据，DataFrame包含行、列索引，可以看作用等长Series组成的字典。

最常用于创建DataFrame的方式是传入一个等长列表或ndarray组成的字典。

```python
In [32]: df = {'姓名': ['小明','小王','小张'], '语文':[80,85,90], '数学':[99,88,86] }                                                                          

In [33]: df                                                                         
Out[33]: {'姓名': ['小明', '小王', '小张'], '语文': [80, 85, 90], '数学': [99, 88, 86]}

In [34]: df = pd.DataFrame(df)                                                      

In [35]: df                                                                         
Out[35]: 
   姓名  语文  数学
0  小明  80  99
1  小王  85  88
2  小张  90  86
```

跟Series类似，如果创建DataFrame没有指定索引，会被自动加上。通过columns选项可以指定列标签（名）以及顺序。

```python
In [36]: df2 = pd.DataFrame(df, columns=['数学', '语文', '姓名'])                   

In [37]: df2                                                                        
Out[37]: 
   数学  语文  姓名
0  99  80  小明
1  88  85  小王
2  86  90  小张

```

如果传入的columns在数据中找不到，就会产生缺失值。

```python
In [38]: df3 = pd.DataFrame(df, columns=['数学', '语文','外语', '姓名'])            

In [39]: df3                                                                        
Out[39]: 
   数学  语文  外语  姓名
0  99  80 NaN  小明
1  88  85 NaN  小王
2  86  90 NaN  小张
```

行标签可以通过index选项指定，上面姓名可以设为行标签，这样就可以去除姓名这一列了。

```python

In [43]: df = {'姓名': ['小明','小王','小张'], '语文':[80,85,90], '数学':[99,88,86]}
    ...:                                                                            

In [44]: df3 = pd.DataFrame(df, columns=['数学', '语文'], index=['小明','小王','小张
    ...: '])                                                                        

In [45]: df3                                                                        
Out[45]: 
    数学  语文
小明  99  80
小王  88  85
小张  86  90
```

通过标签获取DataFrame数据需要通过名称或loc属性进行，前者访问行，后者访问列。

```python
In [51]: df3['数学']                                                                
Out[51]: 
小明    99
小王    88
小张    86
Name: 数学, dtype: int64

In [54]: df3.loc['小王']                                                            
Out[54]: 
数学    88
语文    85
Name: 小王, dtype: int64
```

可以发现返回的都是Series对象。

创建DataFrame还可以使用嵌套字典，字典外层的键会作为列标签，而内层的键会作为行标签。

```python
In [55]: df = {'语文':{'小明':80,'小王':85,'小张':90}, '数学':{'小明':99,'小王':88,'小张':86}}                                                                 

In [56]: pd.DataFrame(df)                                                           
Out[56]: 
    语文  数学
小张  90  86
小明  80  99
小王  85  88
```

DataFrame的index和columns属性可以设置name属性。

```python
In [58]: df3.index.name = '姓名'                                                    

In [59]: df3.columns.name = '学科'                                                  

In [60]: df3                                                                        
Out[60]: 
学科  数学  语文
姓名        
小明  99  80
小王  88  85
小张  86  90

```

DataFrame的values属性会返回DataFrame存储的数据，数据类型是二维的ndarrary。

```python
In [61]: df3.values                                                                 
Out[61]: 
array([[99, 80],
       [88, 85],
       [86, 90]])

```

## 8.3 Pandas对象基本操作

使用适合的Pandas数据结构（Series或DataFrame）存储需要分析的数据后，一般需要对数据进行筛选和操作，以获得最后所需的数据，然后可能是提供数据汇总报表、可视化乃至统计分析与建模。本节将介绍Pandas基本的数据操作功能，读者将学习操作Series和DataFrame对象的基本手段。

### 8.3.1 查看数据

在前面的内容中本书引入的数据都非常简单，我们直接打印输出就可以观察变量存储的数据。然而数据过长时，可能就不适用计算机显示器的显示屏，影响阅读和理解。在实际的操作中，我们仅需要观察少量的数据而不用打印所有的数据就可以了解数据的结构，Pandas引入了`head()`和`tail()`方法显示Series或DataFrame对象的头部和尾部数据，默认是5个（行）。

```python
In [62]: s1 = pd.Series(np.random.rand(1000))                                       

In [63]: s1.head()                                                                  
Out[63]: 
0    0.797903
1    0.458301
2    0.800034
3    0.078226
4    0.999968
dtype: float64

In [64]: d1 = pd.DataFrame({'a':np.random.rand(1000), 'b':np.random.rand(1000)})    

In [65]: d1.head()                                                                  
Out[65]: 
          a         b
0  0.298372  0.612369
1  0.952201  0.606749
2  0.608556  0.381032
3  0.297048  0.939676
4  0.364875  0.360786

In [66]: s1.tail()                                                                  
Out[66]: 
995    0.047546
996    0.752907
997    0.479628
998    0.007178
999    0.960005
dtype: float64

In [67]: d1.tail()                                                                  
Out[67]: 
            a         b
995  0.571106  0.175381
996  0.789444  0.520254
997  0.298536  0.305487
998  0.739158  0.594261
999  0.850966  0.328761

```

在方法中传入正整数作为参数即可修改显示的数目。

```python
In [68]: d1.head(10)                                                                
Out[68]: 
          a         b
0  0.298372  0.612369
1  0.952201  0.606749
2  0.608556  0.381032
3  0.297048  0.939676
4  0.364875  0.360786
5  0.013640  0.267650
6  0.854873  0.251575
7  0.349147  0.065307
8  0.816777  0.932590
9  0.612475  0.385550
```

### 8.3.2 转置

DataFrame的T属性可以获取转置结果。

```python
In [69]: d1.T                                                                       
Out[69]: 
        0         1         2      ...          997       998       999
a  0.298372  0.952201  0.608556    ...     0.298536  0.739158  0.850966
b  0.612369  0.606749  0.381032    ...     0.305487  0.594261  0.328761

[2 rows x 1000 columns]
```

### 8.3.3 重索引

重索引是Pandas库一个重要的方法，它用于创建符合指定索引顺序的新对象。

```python
In [73]: s2 = pd.Series(np.random.rand(5), index=['b', 'a', 'd', 'c', 'e'])         

In [74]: s2                                                                         
Out[74]: 
b    0.630239
a    0.173525
d    0.787798
c    0.176230
e    0.712007
dtype: float64

In [75]: s3 = s2.reindex(['a', 'b', 'c', 'd', 'e', 'f'])                            

In [76]: s3                                                                         
Out[76]: 
a    0.173525
b    0.630239
c    0.176230
d    0.787798
e    0.712007
f         NaN
dtype: float64

```

如果设置的索引值不存在，就引入了缺失值NaN。缺失值和非缺失值可以通过`is.null()`方法和`notnull()`方法进行判断。

```python
In [77]: s3.isnull()                                                                
Out[77]: 
a    False
b    False
c    False
d    False
e    False
f     True
dtype: bool

In [78]: s3.notnull()                                                               
Out[78]: 
a     True
b     True
c     True
d     True
e     True
f    False
dtype: bool
```

有时重索引需要做一些插值处理，这可以通过method选项设定，如ffill可实现前向填充。

```python
In [89]: s4 = pd.Series(np.random.randint(2, 10, 3), index = [0,2,4])               

In [90]: s4                                                                         
Out[90]: 
0    6
2    2
4    2
dtype: int64

In [91]: s4.reindex(np.arange(8), method='ffill')                                   
Out[91]: 
0    6
1    6
2    2
3    2
4    2
5    2
6    2
7    2
dtype: int64

```

针对DataFrame，`reindex()`方法可以修改行索引和列索引。如果只传入一个序列，只修改行索引。使用columns关键字参数则可以修改列索引。


```python
In [92]: d2 = pd.DataFrame(np.random.randint(2,20,9).reshape((3,3)), index=['c', 'b', 'e'], columns=['Test1', 'Test2', 'Test3'])                               

In [93]: d2                                                                         
Out[93]: 
   Test1  Test2  Test3
c      4     19     12
b     11      2      4
e      3     19     12

In [94]: d3 = d2.reindex(['a', 'b', 'c', 'd'])                                      

In [95]: d3                                                                         
Out[95]: 
   Test1  Test2  Test3
a    NaN    NaN    NaN
b   11.0    2.0    4.0
c    4.0   19.0   12.0
d    NaN    NaN    NaN

In [96]: d2.reindex(['a', 'b', 'c', 'd', 'e'], columns=[])                          
Out[96]: 
Empty DataFrame
Columns: []
Index: [a, b, c, d, e]

In [97]: d2.reindex(['a', 'b', 'c', 'd', 'e'], columns=['Test2', 'Test4', 'Test1', '
    ...: Test3'])                                                                   
Out[97]: 
   Test2  Test4  Test1  Test3
a    NaN    NaN    NaN    NaN
b    2.0    NaN   11.0    4.0
c   19.0    NaN    4.0   12.0
d    NaN    NaN    NaN    NaN
e   19.0    NaN    3.0   12.0
```

也可以只使用columns关键字参数重索引列。

```python
In [98]: d2.reindex(columns=['Test3', 'Test1', 'Test4', 'Test2'])                   
Out[98]: 
   Test3  Test1  Test4  Test2
c     12      4    NaN     19
b      4     11    NaN      2
e     12      3    NaN     19
```


### 8.3.4 删除数据

如果想要删除数据的列，可以使用del关键字。

```python
In [99]: d2                                                                         
Out[99]: 
   Test1  Test2  Test3
c      4     19     12
b     11      2      4
e      3     19     12

In [100]: del d2['Test3']                                                           

In [101]: d2                                                                        
Out[101]: 
   Test1  Test2
c      4     19
b     11      2
e      3     19
```

该操作对于行并不适用。Pandas提供了`drop()`方法用于数据项删除场景，读者只需要提供一个索引数组或列表。

```python
In [102]: d2.drop('b')                                                              
Out[102]: 
   Test1  Test2
c      4     19
e      3     19

In [103]: d2.drop(['b','c'])                                                        
Out[103]: 
   Test1  Test2
e      3     19

```

默认执行的删除操作对象是行，如果需要删除列，设定`axis='columns'`。

```python
In [104]: d2.drop('Test2', axis='columns')                                          
Out[104]: 
   Test1
c      4
b     11
e      3
```

注意，上面drop方法的调用是产生一个修改后的数据对象，有时候数据很大，我们可能需要就地修改，此时可以设定`inplace=True`。

### 8.3.5 重赋值

将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配。如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值：

```python
In [108]: d2['New_column'] = pd.Series([1])                                         

In [109]: d2                                                                        
Out[109]: 
   Test1  Test2  New_column
c      4     19         NaN
b     11      2         NaN
e      3     19         NaN

In [111]: d2['New_column'] = pd.Series([1, 2, 3])                                   

In [112]: d2                                                                        
Out[112]: 
   Test1  Test2  New_column
c      4     19         NaN
b     11      2         NaN
e      3     19         NaN

In [113]: d2['New_column'] = pd.Series([1, 2, 3], index=['c','b','e'])              

In [114]: d2                                                                        
Out[114]: 
   Test1  Test2  New_column
c      4     19           1
b     11      2           2
e      3     19           3

```

上面变量d2因为设定了自定义的索引，当我们给新的列添加数值时，如果没有相应地指定索引，因为索引不匹配，所以最后得到的结果都是NaN。

### 8.3.6 索引与过滤

Pandas库支持丰富的索引标签，更适用于实际复杂数据的选择过滤，因此需要理解多种操作方式。

#### 简单索引

对于Series对象，提取单个数据使用下标（从0开始）或标签值，提取多个数据可以使用列表或者切片。

```python
In [119]: s2                                                                        
Out[119]: 
b    0.630239
a    0.173525
d    0.787798
c    0.176230
e    0.712007
dtype: float64

In [120]: s2[1]                                                                     
Out[120]: 0.17352490256429942

In [121]: s2['a']                                                                   
Out[121]: 0.17352490256429942

In [122]: s2[['a','b','c']]                                                         
Out[122]: 
a    0.173525
b    0.630239
c    0.176230
dtype: float64

In [123]: s2['b':'d']                                                               
Out[123]: 
b    0.630239
a    0.173525
d    0.787798
dtype: float64
```

在索引的时候进行赋值，就会修改相应的数据。

```python
In [124]: s2['b':'d'] = [1, 2, 3]                                                   

In [125]: s2                                                                        
Out[125]: 
b    1.000000
a    2.000000
d    3.000000
c    0.176230
e    0.712007
dtype: float64
```

针对DataFrame对象标签索引是获取一个或多个列，而数值切片是提取行，如果只输入数值则会报错，需要额外注意。

```python
In [126]: d2['Test1']                                                               
Out[126]: 
c     4
b    11
e     3
Name: Test1, dtype: int64

In [127]: d2[0]                                                                     
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
~/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3077             try:
-> 3078                 return self._engine.get_loc(key)
   3079             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 0

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-127-f827a0df080c> in <module>
----> 1 d2[0]

~/anaconda3/lib/python3.7/site-packages/pandas/core/frame.py in __getitem__(self, key)
   2686             return self._getitem_multilevel(key)
   2687         else:
-> 2688             return self._getitem_column(key)
   2689 
   2690     def _getitem_column(self, key):

~/anaconda3/lib/python3.7/site-packages/pandas/core/frame.py in _getitem_column(self, key)
   2693         # get column
   2694         if self.columns.is_unique:
-> 2695             return self._get_item_cache(key)
   2696 
   2697         # duplicate columns & possible reduce dimensionality

~/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py in _get_item_cache(self, item)
   2487         res = cache.get(item)
   2488         if res is None:
-> 2489             values = self._data.get(item)
   2490             res = self._box_item_values(item, values)
   2491             cache[item] = res

~/anaconda3/lib/python3.7/site-packages/pandas/core/internals.py in get(self, item, fastpath)
   4113 
   4114             if not isna(item):
-> 4115                 loc = self.items.get_loc(item)
   4116             else:
   4117                 indexer = np.arange(len(self.items))[isna(self.items)]

~/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3078                 return self._engine.get_loc(key)
   3079             except KeyError:
-> 3080                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   3081 
   3082         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 0

In [128]: d2[:0]                                                                    
Out[128]: 
Empty DataFrame
Columns: [Test1, Test2, New_column]
Index: []

In [129]: d2[:1]                                                                    
Out[129]: 
   Test1  Test2  New_column
c      4     19           1
In [130]: d2[:2]                                                                    
Out[130]: 
   Test1  Test2  New_column
c      4     19           1
b     11      2           2

```


#### 利用逻辑操作索引

Pandas对象一大特点是可以通过逻辑比较操作快速筛选所需数据，与ndarray类似。下面代码演示了通过逻辑操作选择Series对象小于1子集的例子：

```
In [131]: s2                                                                        
Out[131]: 
b    1.000000
a    2.000000
d    3.000000
c    0.176230
e    0.712007
dtype: float64

In [132]: s2 < 1                                                                    
Out[132]: 
b    False
a    False
d    False
c     True
e     True
dtype: bool

In [133]: s2[s2 < 1]                                                                
Out[133]: 
c    0.176230
e    0.712007
dtype: float64

```

类似地，我们也可以将该操作应用于DataFrame对象，它进行的是行筛选。

```python
In [134]: d2                                                                        
Out[134]: 
   Test1  Test2  New_column
c      4     19           1
b     11      2           2
e      3     19           3

In [135]: d2[d2['Test2'] > 10]                                                      
Out[135]: 
   Test1  Test2  New_column
c      4     19           1
e      3     19           3
```

这个可以方便进行重赋值操作。

假设我们d2对象中存储的数大于10都是异常值，我们将它们重赋值为10。

```python
In [136]: d2[d2['Test2'] > 10] = 10                                                 

In [137]: d2                                                                        
Out[137]: 
   Test1  Test2  New_column
c     10     10          10
b     11      2           2
e     10     10          10
```

#### 使用loc和iloc索引

上面“简单索引”中针对DataFrame的索引含义不清晰，使用时很容易混淆，导致代码报错。为了方便且准确地获取，Pandas库引入了特殊运算符loc和iloc分别接受字符标签和整数标签。

先看一个示例，使用字符标签选取d2对象第2行的第2和第3列。

```python
In [138]: d2.loc['b', ['Test2', 'New_column']]                                      
Out[138]: 
Test2         2
New_column    2
Name: b, dtype: int64

```

这与下面代码的是等价的：

```python
In [139]: d2.iloc[1, [1,2]]                                                         
Out[139]: 
Test2         2
New_column    2
Name: b, dtype: int64
```

我们可以在方括号内自由地使用切片。

```python
In [140]: d2.iloc[:1, 1:]                                                           
Out[140]: 
   Test2  New_column
c     10          10

```

不仅如此，标签索引是可以级联的。例如，我们增加一级筛选，先选d2对象的第2行，然后大于10的列。

下面的输出显示了每一步的结果：

```python
In [143]: d2                                                                        
Out[143]: 
   Test1  Test2  New_column
c     10     10          10
b     11      2           2
e     10     10          10

In [144]: d2.iloc[1, ]                                                              
Out[144]: 
Test1         11
Test2          2
New_column     2
Name: b, dtype: int64

In [145]: d2.iloc[1, ][d2.iloc[1,] > 10]                                            
Out[145]: 
Test1    11
Name: b, dtype: int64

```

字符索引、整数索引、切片、iloc和loc操作符以及逻辑索引等都可以实现数据的筛选，可见对于想要的结果Pandas库提供了灵活多样的实现方式。

最后，下表对DataFrame各种索引方式进行简单汇总。

| 操作                      | 说明                           |
| ------------------------- | ------------------------------ |
| `df[val]`                 | 选取一或多列（列子集）         |
| `df.loc[val]`             | 使用标签选取一或多行（行子集） |
| `df.loc[:,val]`           | 使用标签选取列子集             |
| `df.loc[val1, val2]`      | 使用标签同时选择行与列         |
| `df.iloc[val]`            | 使用整数选取行子集             |
| `df.iloc[:, val]`         | 使用整数选取列子集             |
| `df.iloc[val1, val2]`     | 使用整数同时选择行与列         |
| `df.at[i_label, j_label]` | 使用标签获取指定位置标量值     |
| `df.iat[i, j]`            | 使用整数索引获取指定位置标量值 |
| `reindex`                 | 通过标签选取行或列             |



### 8.3.7 算术运算

Pandas对象可以进行算术运算，如果存在不同的标签，相同的标签才会对齐运算，这与NumPy数组是不同的。下面分别以Series和DataFrame举例说明。

```python
In [11]: s1 = pd.Series(range(5), index = ['c', 'a', 'b', 'e', 'f'])                                       

In [12]: s2 = pd.Series([2.1, 1.1,  3.2, -4], index = ['a', 'd', 'b', 'c'])                                

In [13]: s1                                                                                                
Out[13]: 
c    0
a    1
b    2
e    3
f    4
dtype: int64

In [14]: s2                                                                                                
Out[14]: 
a    2.1
d    1.1
b    3.2
c   -4.0
dtype: float64

In [15]: s1 + s2                                                                                           
Out[15]: 
a    3.1
b    5.2
c   -4.0
d    NaN
e    NaN
f    NaN
dtype: float64

```

由于一些标签不重叠，Pandas引入了NA值。注意，只要存在NA值，所有的算术操作结果都只会是NA值，NA值被广播了。

DataFrame是一张二维表，所以算术运算造成的对齐现象会同时在行和列上发生。

```python
In [16]: df1 = pd.DataFrame(np.arange(12.).reshape((3,4)), columns=['a', 'b', 'c', 'd'], index=['a', 'b', '
    ...: c'])                                                                                              

In [17]: df2 = pd.DataFrame(np.arange(16.).reshape((4,4)), columns=['a', 'e', 'c', 'd'], index=['b', 'a', '
    ...: d', 'c'])                                                                                         

In [18]: df1                                                                                               
Out[18]: 
     a    b     c     d
a  0.0  1.0   2.0   3.0
b  4.0  5.0   6.0   7.0
c  8.0  9.0  10.0  11.0

In [19]: df2                                                                                               
Out[19]: 
      a     e     c     d
b   0.0   1.0   2.0   3.0
a   4.0   5.0   6.0   7.0
d   8.0   9.0  10.0  11.0
c  12.0  13.0  14.0  15.0

In [20]: df1 + df2                                                                                         
Out[20]: 
      a   b     c     d   e
a   4.0 NaN   8.0  10.0 NaN
b   4.0 NaN   8.0  10.0 NaN
c  20.0 NaN  24.0  26.0 NaN
d   NaN NaN   NaN   NaN NaN
```

如果想要使用值进行填充，可以通过方法add()实现，给选项`fill_value`传入参数值。

```python
In [21]: df1.add(df2, fill_value=2)                                                                        
Out[21]: 
      a     b     c     d     e
a   4.0   3.0   8.0  10.0   7.0
b   4.0   7.0   8.0  10.0   3.0
c  20.0  11.0  24.0  26.0  15.0
d  10.0   NaN  12.0  13.0  11.0

```

其他算术操作类似，因此不再赘述。

### 8.3.8 函数应用

Pandas本身就是基于NumPy库构建的，前面我们也了解到DataFrame和Series存储数据使用的就是ndarray，因此Pandas对象除了支持Pandas库提供的函数和方法，也天然支持NumPy各类函数操作。

例如，求取绝对值。

```python
In [22]: np.abs(df1)                                                                                       
Out[22]: 
     a    b     c     d
a  0.0  1.0   2.0   3.0
b  4.0  5.0   6.0   7.0
c  8.0  9.0  10.0  11.0

In [23]: -np.abs(df1)                                                                                      
Out[23]: 
     a    b     c     d
a -0.0 -1.0  -2.0  -3.0
b -4.0 -5.0  -6.0  -7.0
c -8.0 -9.0 -10.0 -11.0

In [24]: np.abs(-np.abs(df1))                                                                              
Out[24]: 
     a    b     c     d
a  0.0  1.0   2.0   3.0
b  4.0  5.0   6.0   7.0
c  8.0  9.0  10.0  11.0

```

不过函数应用最精彩的操作来自于apply()函数，它可以传入一个函数作为参数对Pandas对象的行或列进行运算，如求取df1对象的列和。

```python
In [25]: df1.apply(sum)                                                                                    
Out[25]: 
a    12.0
b    15.0
c    18.0
d    21.0
dtype: float64
```

当然有时候为了避免函数命名的麻烦，也可以引入一个匿名函数。下面的操作实现求取每列的残差值。

```python
In [26]: df1.apply(lambda x: x - x.mean())                                                                 
Out[26]: 
     a    b    c    d
a -4.0 -4.0 -4.0 -4.0
b  0.0  0.0  0.0  0.0
c  4.0  4.0  4.0  4.0
```

默认是对每列应用函数，如果想要对行进行操作，设定选项`axis='columns'`即可。

```python
In [27]: df1.apply(lambda x: x - x.mean(), axis='columns')                                                 
Out[27]: 
     a    b    c    d
a -1.5 -0.5  0.5  1.5
b -1.5 -0.5  0.5  1.5
c -1.5 -0.5  0.5  1.5
```

掌握apply()方法的核心在于将行或列一组值当做标量对待，那么这里应用函数其实跟对标量用函数计算本质是一样的。


### 8.3.9 排序

数据的排序是一种重要的操作，对于Series对象和DataFrame对象，Panda库提供了sort_index()方法和sort_values()方法分别按标签和值进行排序。

```python
In [29]: s1 = pd.Series([2, 1, 3, 5, 4], index=['b', 'a', 'd', 'c', 'f'])                                  

In [30]: s1.sort_index()                                                                                   
Out[30]: 
a    1
b    2
c    5
d    3
f    4
dtype: int64

In [31]: s1.sort_values()                                                                                  
Out[31]: 
a    1
b    2
d    3
f    4
c    5
dtype: int64

```

默认是升序排列，设定`ascending=False`可以改为降序。

```python
In [32]: s1.sort_values(ascending=False)                                                                   
Out[32]: 
c    5
f    4
d    3
b    2
a    1
dtype: int64
```

DataFrame对象有2个维度，默认是按照行进行排序，如果想要该为按列排序，需要将axis选项设为1。

在操作DataFrame时，有一个排序参数非常实用，就是by。它可以根据某一列值进行排序，例如在实际处理中，我们可能需要根据月份和日期排序，而数据本身是杂乱的，这个选项就可以派上大用场。

```python
In [34]: df = pd.DataFrame({u'月份':[2, 1, 4, 3], u'日期':[29, 16, 14, 22], u'销量': [150, 44, 300, 68]})  

In [35]: df                                                                                                
Out[35]: 
   月份  日期   销量
0   2  29  150
1   1  16   44
2   4  14  300
3   3  22   68

In [36]: df.sort_values(by='月份')                                                                         
Out[36]: 
   月份  日期   销量
1   1  16   44
0   2  29  150
3   3  22   68
2   4  14  300

In [37]: df.sort_values(by='日期')                                                                         
Out[37]: 
   月份  日期   销量
2   4  14  300
1   1  16   44
3   3  22   68
0   2  29  150

In [38]: df.sort_values(by=['月份', '日期'])                                                               
Out[38]: 
   月份  日期   销量
1   1  16   44
0   2  29  150
3   3  22   68
2   4  14  300

In [39]: df.sort_values(by='销量')                                                                         
Out[39]: 
   月份  日期   销量
1   1  16   44
3   3  22   68
0   2  29  150
2   4  14  300
```

## 8.4 基本统计分析

Pandas对象本身存在一组常用的统计值计算方法，主要用于汇总，如计算总和，分位数等。

```python
In [40]: df.sum()                                                                                          
Out[40]: 
月份     10
日期     81
销量    562
dtype: int64

In [41]: df.quantile()                                                                                     
Out[41]: 
月份      2.5
日期     19.0
销量    109.0
Name: 0.5, dtype: float64

In [42]: df.quantile([0.1, 0.9])                                                                           
Out[42]: 
      月份    日期     销量
0.1  1.3  14.6   51.2
0.9  3.7  26.9  255.0

```

也有方法计算累计值，如累计和：

```python
In [43]: df.cumsum()                                                                                       
Out[43]: 
   月份  日期   销量
0   2  29  150
1   3  45  194
2   7  59  494
3  10  81  562

```

不过，我们常用describe()方法观测多个统计值，从数值的角度理解数据的大致分布情况。

```python
In [44]: df.describe()                                                                                     
Out[44]: 
             月份         日期         销量
count  4.000000   4.000000    4.00000
mean   2.500000  20.250000  140.50000
std    1.290994   6.751543  115.61286
min    1.000000  14.000000   44.00000
25%    1.750000  15.500000   62.00000
50%    2.500000  19.000000  109.00000
75%    3.250000  23.750000  187.50000
max    4.000000  29.000000  300.00000
```

下表列出常用的描述统计相关方法。

| 方法              | 说明                     |
| ----------------- | ------------------------ |
| count             | 非NA值数量               |
| describe          | 汇总统计                 |
| min、max          | 最小最大值               |
| argmin、argmax    | 最小值最大值整数索引位置 |
| idxmin、idxmax    | 最小值最大值标签位置     |
| quantile          | 分位数                   |
| mean、median、sum | 均值、中位数、总和       |
| mad               | 平均绝对离差             |
| var、std          | 方差、标准差             |
| cumsum、cumprod   | 累计和、累计积           |


## 8.5 章末小结

