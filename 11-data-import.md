# 第 11 章 数据导入

**本章内容提要**:

- 常见文本类型的读写
- 网页数据解析
- 读写数据库

“三军未动，粮草先行”。数据是数据分析的起点，也是数据分析的核心之一。现实世界中的数据类型是多种多样的，有来自计算机本地存储的 Excel 文件、CSV 文件中的，也有来自网页数据，专用数据库中的，还有需要调用程序 API 获取的。本章将从实际数据处理常见的类型出发，讲解如何利用工具导入它们，为后续的数据分析和可视化提供源泉。

## 11.1 常见文件类型

### 11.1.1 CSV 文件

在数据分析领域，最常见和最为推荐的文本文件当属于 CSV（comma separated values, 逗号分隔值）文件。CSV 文件格式简单，易于导入、存储乃至直接阅读。

下面给出一个 CSV 文件内容简单示例，因为格式一致，所以后续介绍的操作可以拓展到任意行的数据上去。

```
姓名,年龄,班级
周某某,9,3班
王某某,10,6班
```

我们可以非常清楚地理解上面的内容，它可能来自某个学校学生的登记表。这里有一点值得提醒读者注意，CSV 文件采用的分隔符是英文逗号，而非中文常用的逗号。另外，在欧洲地区一些国家中，它们是使用英文分号 ; 来作为逗号分隔符的，读者如果见到也不用奇怪。

我们可以将上面的内容保存，一般规定以 csv 作为文件后缀名。当然，文件内容和文件后缀名是没有关系的，采用通用命名是为了方便理解。很多 txt 后缀名文件也是采用的 csv 格式。

现在我们将其保存为文件 records.csv。保存的方法可以使用记事本、文本编辑器等，Windows 用户推荐下载和使用 Notepad++ 软件进行文本文件的编辑，不推荐读者使用 Excel。

现在假设我们拿到了这样一个叫做 records.csv 的文件，我们想要利用 Python 打开并查看它，该如何实现呢？

读者不妨先进行思考和查阅网络资料再进一步阅读。

#### 使用字符串方法

在第 4 章向读者介绍过 open() 函数，这里我们需要处理的文本每一行内容都是以英文逗号分隔，我们可以很自然地想到使用 open() 函数打开文件并使用 split() 方法进行切分。

```python
In [1]: records = []

In [2]: with open("records.csv", "r", encoding='utf-8') as f:
   ...:     for line in f.readlines():
   ...:         records.append(line.strip().split(','))
   ...:

In [3]: records
Out[3]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班
']]
```

上述代码首先创建了一个列表，作为存储文本内容的容器。之前文件保存的时候使用的是 utf-8 编码，所以打开也使用相同的编码。接着使用 readlines() 方法读入所有的行并进行 for 循环迭代。对于读入的每一行，我们首先使用 strip() 方法去掉每一行末尾的换行符，然后使用 split() 方法将内容按照英文逗号进行分割，得到子列表并将其添加到 records 列表。上述的操作都是基于文本是字符串，可以看到年龄那一栏存储的方式就是字符串，如果要做后续分析，读者需要在之前将其转换为整型。

读者需要注意要打开的文件路径，这里使用 records.csv 需要保证该文件必须在 Python 的当前工作目录下才可以运行。在 IPython Shell 或 Jupyter Notebook 中，使用命令 !pwd 可以查看当前的工作目录，而 !ls 可以查看当前工作目录下的文件。

```python
In [2]: !ls
records.csv  records.tsv  records.txt

In [3]: !pwd
/c/Shixiang/pybook/files/chapter11
```

#### 使用 csv 标准模块

因为 csv 文件的频繁使用，Python 提供了一个标准模块 csv 以进行 CSV 文件的读入、写入以及格式化等操作。

上一个例子可以通过下面类似的代码实现，注意这里并没有将数据保存到列表中，而是直接打印到屏幕上。

```python
In [4]: import csv
In [5]: with open("records.csv", "r", encoding='utf-8') as f:
   ...:     csv_reader = csv.reader(f)
   ...:     for row in csv_reader:
   ...:         print(','.join(row))
   ...:
姓名,年龄,班级
周某某,9,3班
王某某,10,6班
```

可以观察到，csv 模块的简便之处我们不需要再对文件内容调用方法进行去掉换号符，指定分割符操作了，使用 reader() 函数读入的结果是一个直接可以迭代的对象。

#### 使用 Pandas 库

前面提到的两种方法都需要显式地调用 open() 函数打开文件，然后使用工具进行读入处理。相比而言，使用流行库 Pandas 对 CSV 文件操作就更简单了。

```python
In [6]: import pandas as pd

In [7]: records = pd.read_csv('records.csv')

In [8]: records
Out[8]:
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班

In [9]: records.columns
Out[9]: Index(['姓名', '年龄', '班级'], dtype='object')

In [10]: records.index
Out[10]: RangeIndex(start=0, stop=2, step=1)
```

Pandas 库读入数据的强大之处在于不仅仅简化了读入代码，而且对读入的数据进行了良好的转换，自动将第一行识别为了列名，并设定了行索引。Pandas 读入的结果是一个 DataFrame 对象，针对它的一些基础操作方法本书已经在第 8 章进行了详细介绍，这里不再赘述。

### 11.1.2 CSV 变体

通过上一小节我们知道了 CSV 文件是通过英文逗号进行文字域的分隔，所以有时候我们需要处理 CSV 的变体并不奇怪，其中最常见的 CSV 变体是 TSV，即制表符分隔文件。在数据处理时，读者碰到的大部分 txt 文本文件其实就是 TSV 文件。制表符可以通过我们键盘上的 Tab 键键入，但在程序中我们使用 \t 指定它。另外有的文本会采用空格分隔数据，其他的情况相对而言则更少见了。

既然有这么多 CSV 的变体，我们如何导入它们呢，总不可能为每一种变体编写一个函数吧？正确的做法是使用默认参数。

下面是具体的思路和做法：

* 如果是自己编写函数，应当创建合理的默认参数，以处理常见的一些情况。
* 如果是使用他人编写的模块，首先应当查阅函数文档，而不是马上求助他人或者垂头丧气。一般而言，模块的开发者都会为函数的一些常见情况创建相应的参数，阅读函数文档是非常好的习惯。如果函数的确没有参数，而且自己又没有开发的能力，再去网络上搜索资料或者专业论坛提问。

假设我们需要处理 3 种 CSV 格式文件：英文逗号分隔、制表符分隔以及空格分隔，它们的文件名分别为 records.csv、records.tsv 以及 records.txt。我们接下来看看如何通过自己创建函数导入以及使用 Pandas 库进行导入。

records.csv 内容：

```
姓名,年龄,班级
周某某,9,3班
王某某,10,6班
```

records.tsv 内容：

```
姓名	年龄	班级
周某某	9	3班
王某某	10	6班
```

records.txt 内容：

```
姓名 年龄 班级
周某某 9 3班
王某某 10 6班
```

#### 创建 CSV 导入函数

为了处理不同的分隔符，我们为要创建的函数指定一个 sep 参数（seperator 的简写）。另外，前面我们发现使用字符串方法处理和 csv 模块处理的结构是类似的，我们不妨也设定一个参数 method 用来控制使用哪种方法解析文本。

```python
def read_csv(file_path, sep=',', method='default'):
    """导入 CSV 及其变体文本"""
    res = []
    with open(file_path, "r", encoding='utf-8') as f:
        # 这里我们直接指定了 encoding 为 utf-8
        # 实际上为了处理更广泛的编码类型，
        # 读者可以将其改写为函数的一个参数
        # 其他选项也可以这样做
        if method == "default":
            for line in f.readlines():
                res.append(line.strip().split(sep))
        elif method == "csv":
            print("Using csv module...")
            import csv
            csv_reader = csv.reader(f, delimiter=sep)
            for row in csv_reader:
                res.append(row)
        else:
            raise ValueError('不支持的导入方法！')
    return res
```

上面的 read_csv() 函数中我们通过不同的 method 调用不同的导入方法，通过查阅 csv 模块的文档（请读者自行查阅），我们可以找到 reader() 函数的 delimiter 参数可以指定分隔符。下面让我们来试试我们函数的威力吧！

我们先看看默认方法的结果，读者需要先运行上面创建的函数再运行下面的测试代码。

```python
In [11]: read_csv('records.csv')
Out[11]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]

In [12]: read_csv('records.tsv', sep='\t')
Out[12]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]

In [13]: read_csv('records.txt', sep=' ')
Out[13]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]
```

三种情况读入的数据完全一致！我们再看看使用 csv 模块导入的结果如何。

```python
In [14]: read_csv('records.csv', method='csv')
Using csv module...
Out[14]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]

In [15]: read_csv('records.tsv', sep='\t', method='csv')
Using csv module...
Out[15]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]

In [16]: read_csv('records.txt', sep=' ', method='csv')
Using csv module...
Out[16]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]
```

结果也是完全一致。可见，上面的函数虽然简单，但它完全实现了我们所需要的功能。实际上，更复杂的函数也是这样一步一步添加选项完成的。


#### 使用 Pandas 导入

使用 Pandas 就不需要自己创建函数了，因为 Pandas 库提供的 read_csv() 函数本身支持 sep 参数，所以通过指定该选项我们就能够读入不同的 CSV 及变体格式数据。

```python
In [17]: import pandas as pd
In [18]: pd.read_csv('records.csv')
Out[18]: 
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班
In [19]: pd.read_csv('records.tsv', sep='\t')
Out[19]:
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班

In [20]: pd.read_csv('records.txt', sep=' ')
Out[20]:
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班
```

从上面的代码调用来看，我们创建的 read_csv() 和 Pandas 库提供的函数是没有差别的。利用前面章节学习的知识，我们也可以修改函数，让结果都保持一致。

```python
def read_csv2(file_path, sep=',', method='default'):
    """导入 CSV 及其变体文本"""
    res = []
    with open(file_path, "r", encoding='utf-8') as f:
        if method == "default":
            for line in f.readlines():
                res.append(line.strip().split(sep))
        elif method == "csv":
            print("Using csv module...")
            import csv
            csv_reader = csv.reader(f, delimiter=sep)
            for row in csv_reader:
                res.append(row)
        else:
            raise ValueError('不支持的导入方法！')
    import pandas as pd
    # 将结果转换为 DataFrame
    res = pd.DataFrame(res[1:], columns=res[0])
    return res
```

运行上述函数并进行测试。

```python
In [21]: read_csv2('records.tsv', sep='\t', method='csv')
Using csv module...
Out[21]: 
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班
```

读者不妨试试修改要读入的文件和函数选项看看函数是否都能够正常工作。

#### 导出 CSV

将处理后得到的结构化数据导出为 CSV 文件是保存数据的最佳方式，方便分享和再次分析。导出或者粘贴为 Excel 表格是非常不推荐的方式，Excel 会自动对输入文本进行分析和转换，虽然大部分时候这种方式简化了我们的操作，但有时候却会得到意料之外的结果，特别是在要求数据严谨的科学领域。例如，在 Excel 表格中键入 MARCH1，它是一个基因的名字，紧接着键入回车后它会被 Excel 自动转换为日期 3 月 1 号！有一篇科学研究报道称，生物医学文献中 Excel 保存的数据中，有 20% 左右的表格都出现了问题，这极大了影响了科学研究的可重复性，而且这种错误很难发现，因而会影响所有使用包含错误数据的研究。

将数据保存为 CSV 文件其实是导入 CSV 文件的逆操作。因此我们这里也可以提出相应的两种办法：一是结合使用 open() 和 print() 函数将数据按分隔符输出到文件；而是直接调用 Pandas 提供的 to_csv() 方法。

先读入测试数据：

```python
In [3]: rds1 = read_csv('records.csv')
In [4]: rds2 = pd.read_csv('records.csv')
In [5]: rds1
Out[5]: [['姓名', '年龄', '班级'], ['周某某', '9', '3班'], ['王某某', '10', '6班']]
In [6]: rds2
Out[6]: 
    姓名  年龄  班级
0  周某某   9  3班
1  王某某  10  6班
```

如果只是简单地将数据以 CSV 格式打印到屏幕，我们可以使用下面的命令：

```python
In [13]: for row in rds1:
    ...:     print(','.join(row))
    ...: 
姓名,年龄,班级
周某某,9,3班
王某某,10,6班
```

接下来是如何将数据打印输出到文件中，我们先看一下 print() 函数说明：

```python
In [12]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.    
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method
```

可以看到，print() 函数支持参数 file 用于设定文件流，默认是系统标准输出。因此，我们可以联合 open() 函数打开一个文件 test1.csv 并进行写入：

```python
In [16]: with open('test1.csv', 'w', encoding='utf-8') as f:
    ...:     for row in rds1:
    ...:         print(','.join(row), file=f)
```

使用系统命令查看文件内容是否正确：

```python
In [17]: !cat test1.csv
姓名,年龄,班级
周某某,9,3班
王某某,10,6班
```

这样我们就确定将数据成功导出到 CSV 文件中了。

相比而言，直接使用 Pandas 的 to_csv() 方法就可以完成上面的操作：

```python
In [18]: rds2.to_csv('test2.csv')

In [19]: !cat test2.csv
,姓名,年龄,班级
0,周某某,9,3班
1,王某某,10,6班
```

由此可见，无论数据读写，Pandas 提供的工具更加简便直观。

### 11.1.3 Excel 文件

尽管本书不推荐读者使用 Excel 处理和保存数据，但是因为微软系统和 Office 办公套件的流行我们总会遇见并且必须面对 Excel 文件的处理。在 Python 中，我们无法通过直接使用 open() 函数或标准模块来导入 Excel 数据，但有很多工具包提供了该功能，比较知名的有 Pandas、openpyxl、xlrd、xlutils 以及 pyexcel。

#### 检查数据

Excel 本身是微软提供的一款非常强大的数据分析软件，我们可以对 Excel 的单元格进行非常多的操作，包括设定格式、插入函数命令等。一旦我们在 Excel 中对数据进行了额外操作，我们使用 Python 进行导入时就需要额外小心，因为跟数据无关的额外信息破坏了数据的规律性，增加了文件的复杂性，所以 Python 在解析时非常容易出错。

既然是使用 Python 处理数据，那么读者提供的 Excel 数据应当尽量是规整的，具体可以参考以下几条要求进行检查：

- 表格的第一行应当是列名
- 所有的单元格尽量避免出现空格，特别是行名和列名。读者可以使用其他符号，如下划线、分号、短横杠等进行替代
- 名字尽量简短易懂
- 确保缺失值都使用 NA 进行标注

我们知道，Excel 文件一般是以 xls 或 xlsx 作为文件拓展名。除了它们，Excel 是支持保存为其他格式的，推荐将数据导出为 CSV 文件后用前面介绍过的方法导入。

#### 准备工作

在前面执行导入操作时，我们默认 IPython Shell 或 Jupyter Notebook 是在要导入文件的同一目录下启动的，此时 Python 的工作路径与文件目录一致，我们在为导入函数传入文件路径参数时只需要指定文件名即可。但更为实际的情况可能是执行的脚本、Notebook 没有和要操作的数据文件位于同一路径，一个解决办法是通过绝对路径或相对路径的方式指定文件路径，另一个办法是在 Python 程序中切换工作目录。

假设 records.csv 文件有以下路径层级：C 盘中有 data 文件夹（目录），data 下有文件 records.csv，而我们在 C 盘下启动了 Jupyter Notebook 或 IPython Shell。那么 Python 如何访问 records.csv 文件路径呢？

```
C:
├─data
   └─records.csv
```

绝对路径是以根目录为起始的路径，Windows 系统一般以盘符开始，如 C:；而 macOS 和 Linux 系统则以 / 开始。相对路径是指以当前路径为参考的路径。以 C: 为当前路径，文件 records.csv 的绝对路径和相对路径给出如下：

```python
# 绝对路径
C:/data/records.csv
# 相对路径
data/records.csv
```

另外，我们可以通过 os 模块提供的 chdir() 函数在 Python 脚本内部切换工作目录。常见操作如下：

```python
# 导入 os
import os

# 获取当前工作目录，cwd 为 current working directory 首字母缩写
cwd = os.getcwd()
cwd
# 或者使用魔术命令 pwd
pwd

# 更改工作目录
os.chdir("/path/to/your/data-folder")
# 或者使用魔术命令 cd
cd /path/to/your/data-folder

# 列出当前目录的所有文件和子目录
os.listdir('.')
```

#### 使用 Pandas 读写 Excel

前面我们向读者介绍了 Pandas 可以非常方便地导入 CSV 文本数据，这里将了解如何使用 Pandas 读写 Excel 文件。一个 Excel 可以存储多张表格，因此读入 Excel 的操作大有不同。

这里使用事先已经创建好的 Excel 文件 data.xlsx 作为示例数据，它包含了两个数据集，分别存储在两个表格中。

我们首先查看下当前的工作目录，并将其切换到数据对应的目录中。

```python
In [2]: import os
In [3]: os.getcwd()  # 获取当前工作目录 
Out[3]: 'C:\\Shixiang\\pybook'
In [4]: os.listdir('files/chapter11')  # 列出目录下的文件及子目录
Out[4]: 
['data.xlsx',
 'lung.csv',
 'mtcars.csv',
 'records.csv',
 'records.tsv',
 'records.txt',
 'test1.csv',
 'test2.csv']

In [5]: cd files  # 切换工作目录
C:\Shixiang\pybook\files
In [6]: os.getcwd()  # 获取当前工作目录
Out[6]: 'C:\\Shixiang\\pybook\\files'
In [7]: pwd
Out[7]: 'C:\\Shixiang\\pybook\\files'

In [8]: os.chdir('chapter11')  # 将工作目录切换为数据所在目录
In [9]: pwd
Out[9]: 'C:\\Shixiang\\pybook\\files\\chapter11'
```

上面代码分别演示了使用 os 模块的函数和 IPython 魔术命令进行工作目录的获取和切换，下面开始进行数据的读入。

```python
In [10]: import pandas as pd
In [11]: file = 'data.xlsx'
In [12]: xl = pd.ExcelFile(file)
In [13]: # 打印表格名字
In [14]: print(xl.sheet_names)
['mtcars', 'lung']
```

我们的确可以看到 data.xlsx 文件中存在两张表名分别为 mtcars 和 lung 的表格，下面我们将这 2 个数据集解析出来。

```python
In [15]: mtcars = xl.parse('mtcars')
In [16]: mtcars.head()  # 只查看头几行
Out[16]: 
    mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
0  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
2  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
3  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
4  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2

In [17]: lung = xl.parse('lung')
In [18]: lung.head()
Out[18]: 
   inst  time  status  age  ...  ph.karno  pat.karno  meal.cal  wt.loss    
0   3.0   306       2   74  ...      90.0      100.0    1175.0      NaN    
1   3.0   455       2   68  ...      90.0       90.0    1225.0     15.0    
2   3.0  1010       1   56  ...      90.0       90.0       NaN     15.0    
3   5.0   210       2   57  ...      90.0       60.0    1150.0     11.0    
4   1.0   883       2   60  ...     100.0       90.0       NaN      0.0    

[5 rows x 10 columns]
```

然后我们就可以根据前面学习过的 Pandas 知识操作它们了。

现在我们假设已经分析好了数据，接下来想要把结果导出为 Excel 文件，怎么做呢？使用 Pandas 的 to_excel() 函数就可以完成。

```python
In [21]: lung.to_excel('~/测试导出.xlsx')
```

如果读者也运行了上面这个命令，快去打开家目录下的“测试导出.xlsx”文件看看成功导出没吧。

该函数支持非常多的选项：

```python
In [22]: lung.to_excel?
Signature:
lung.to_excel(
    excel_writer,       
    sheet_name='Sheet1',
    na_rep='',
    float_format=None,  
    columns=None,       
    header=True,        
    index=True,
    index_label=None, 
    startrow=0,       
    startcol=0,       
    engine=None,      
    merge_cells=True, 
    encoding=None,    
    inf_rep='inf',    
    verbose=True,     
    freeze_panes=None,
)
Docstring:
Write object to an Excel sheet.
...
```

例如，默认的表名是 Sheet1，我们可以通过以下代码进行修改为 lung：

```python
In [23]: lung.to_excel('~/测试导出.xlsx', sheet_name='lung')
```

### 11.1.4 pickle 文件

上面介绍的 CSV 文件和 Excel 文件都可以通过外部程序进行修改，这可能与某些安全程序的目的可能相悖，有时也不利于分析的可重复性。特别是 CSV 和 Excel 等文件类型都无法保存 Python 特有的数据结构，例如类。为此，Python 提供了一个标准模块 pickle 实现对一个 Python 对象结构的二进制序列化和反序列化：通过 pickle 模块的序列化操作我们能够将 Python 程序中运行的对象信息保存到文件中去，永久存储；通过pickle 模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

pickle 文件与 CSV 这种文本文件相比有几点本质的不同：

- pickle 文件是二进制格式的
- pickle 文件无法通过文本编辑器直观阅读
- CSV 文件在 Python 系统外广泛使用，而 pickle 文件是 Python 专有的
- pickle 文件可以保存 Python 大量的数据类型

pickle 文件的读取和保存通过 pickle 模块的 load() 和 dump() 函数实现，下面简单举例说明。

```python
In [1]: import pickle
In [2]: data = {'a':[1,2,3], 'b':['yes','no']}
In [3]: with open('data.pkl', 'wb') as f:
   ...:     pickle.dump(data, f)
```

这里我们首先创建了一个字典 data，然后使用 open() 函数并以二进制写入的方式创建了文件 data.pkl，pkl 是 pickle 文件特有的拓展名，在 with 语句内部，我们使用 dump() 函数将数据写入，保证了 data.pkl 文件无论如何都会正常关闭。

此处使用 pickle 文件的好处是显而易见的，这个数据并不是很好用 CSV 格式表示。另外，如果考虑使用纯文本保存，我们需要调用 for 循环，而这种情况下数据如果更复杂点就会难以还原了。

导入 pickle 文件操作类似，不过我们需要把 open() 的模式设定为二进制写入 'rb'，另外是调用 load() 函数而非 dump()。

```python
In [4]: with open('data.pkl', 'rb') as file:
   ...:     data_restore = pickle.load(file)
   ...: 

In [5]: print(data_restore)
{'a': [1, 2, 3], 'b': ['yes', 'no']}
```

### 11.1.5 SAS 与 Stata 文件

作为数据分析从业者，我们可能没有使用过 SAS 和 Stata，但肯定对它们的大名有所耳闻。SAS 是 Statistical Analysis System 的缩写，是由美国北卡罗来纳州立大学 1966 年开发的统计分析软件。经过多年来的完善和发展，SAS 在国际上已被誉为统计分析的标准软件，在各个领域得到广泛应用，尤其是商业分析以及生物统计学。Stata 则是由 Statistics 和 data 这两个词各取一部分拼接而成（与 Pandas 一词的来源相似），是一套提供其使用者数据分析、数据管理以及绘制专业图表的完整及整合性统计软件，主要用于学术研究，尤其是社会科学领域。

SAS 和 Stata 作为专业的统计分析软件，它们都有自己独有的数据存储方式。SAS 目前主要使用 sas7bdat 作为文件拓展名，而 Stata 使用 dta 作为文件拓展名。

sas7bdat 文件的导入需要提前安装好 sas7bdat 包。安装之后，我们通过 SAS7BDAT() 函数打开数据集文件，并调用 to_data_frame() 方法可以将文件导入为一个 Pandas 的 DataFrame 对象。

```python
import pandas as pd
from sas7bdat import SAS7BDAT

# 此处 xxxx 应修改为实际文件名
with SAS7BDAT('xxxx.sas7bdat') as file:
    df_sas = file.to_data_frame()
```

而 dta 文件可以直接通过 Pandas 库提供的 read_stata() 函数导入。

```python
import pandas as pd
# 此处 xxxx 应修改为实际文件名
data = pd.read_stata('xxxx.dta')
```

#### 11.1.6 HDF5 文件

```python
import h5py
filename = 'data.hdf5'
data = h5py.File(filename, 'r')
print(type(data))

for key in data.keys():
    print(key)

print(type(data['meta']))

for key in data['meta'].keys():
    print(key)

print(data['meta']['Description'].value, data['meta']['Detector'].value)
```

#### 11.1.7 MATLAB 文件

scipy.io.loadmat() - read
scipy.io.savemat() - write

```python
import scipy.io
filename = 'xxx.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))

print(type(mat['x']))

# keys - MATLAB variable names
# values - objects assigned to variables
```

#### 11.1.8 json 文件

#### 11.1.9 yml 文件

## 11.3 网页数据

XML 与 HTML 的关系简单解析

## 11.4 数据库数据

读写SQL
