# 第 10 章 数据导入

**本章内容提要**:

- CSV
- Excel
- JSON
- YAML
- SQLite

“三军未动，粮草先行”。数据是数据分析的起点，也是数据分析的核心之一。现实世界中的数据类型是多种多样的，有来自计算机本地存储的 Excel 文件、CSV 文件中的，也有来自网页数据，专用数据库中的，还有需要调用程序 API 获取的。本章将从实际数据处理常见的类型出发，讲解如何利用工具导入它们，为后续的数据分析和可视化提供源泉。

## 10.1 CSV 文件

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

### 10.1.1 使用字符串方法

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
/c/Shixiang/pybook/files/chapter10
```

### 10.1.2 使用 csv 标准模块

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

### 10.1.3 使用 Pandas 库

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

## 10.2 CSV 变体

通过上一节我们知道了 CSV 文件是通过英文逗号进行文字域的分隔，所以有时候我们需要处理 CSV 的变体并不奇怪，其中最常见的 CSV 变体是 TSV，即制表符分隔文件。在数据处理时，读者碰到的大部分 txt 文本文件其实就是 TSV 文件。制表符可以通过我们键盘上的 Tab 键键入，但在程序中我们使用 \t 指定它。另外有的文本会采用空格分隔数据，其他的情况相对而言则更少见了。

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

### 10.2.1 创建 CSV 导入函数

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


### 10.2.2 使用 Pandas 导入

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

### 10.2.3 导出 CSV

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

## 10.3 Excel 文件

尽管本书不推荐读者使用 Excel 处理和保存数据，但是因为微软系统和 Office 办公套件的流行我们总会遇见并且必须面对 Excel 文件的处理。在 Python 中，我们无法通过直接使用 open() 函数或标准模块来导入 Excel 数据，但有很多工具包提供了该功能，比较知名的有 Pandas、openpyxl、xlrd、xlutils 以及 pyexcel。

### 10.3.1 检查数据

Excel 本身是微软提供的一款非常强大的数据分析软件，我们可以对 Excel 的单元格进行非常多的操作，包括设定格式、插入函数命令等。一旦我们在 Excel 中对数据进行了额外操作，我们使用 Python 进行导入时就需要额外小心，因为跟数据无关的额外信息破坏了数据的规律性，增加了文件的复杂性，所以 Python 在解析时非常容易出错。

既然是使用 Python 处理数据，那么读者提供的 Excel 数据应当尽量是规整的，具体可以参考以下几条要求进行检查：

- 表格的第一行应当是列名
- 所有的单元格尽量避免出现空格，特别是行名和列名。读者可以使用其他符号，如下划线、分号、短横杠等进行替代
- 名字尽量简短易懂
- 确保缺失值都使用 NA 进行标注

我们知道，Excel 文件一般是以 xls 或 xlsx 作为文件拓展名。除了它们，Excel 是支持保存为其他格式的，推荐将数据导出为 CSV 文件后用前面介绍过的方法导入。

### 10.3.2 准备工作

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

### 10.3.3 使用 Pandas 读写 Excel

前面我们向读者介绍了 Pandas 可以非常方便地导入 CSV 文本数据，这里将了解如何使用 Pandas 读写 Excel 文件。一个 Excel 可以存储多张表格，因此读入 Excel 的操作大有不同。

这里使用事先已经创建好的 Excel 文件 data.xlsx 作为示例数据，它包含了两个数据集，分别存储在两个表格中。

我们首先查看下当前的工作目录，并将其切换到数据对应的目录中。

```python
In [2]: import os
In [3]: os.getcwd()  # 获取当前工作目录
Out[3]: 'C:\\Shixiang\\pybook'
In [4]: os.listdir('files/chapter10')  # 列出目录下的文件及子目录
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

In [8]: os.chdir('chapter10')  # 将工作目录切换为数据所在目录
In [9]: pwd
Out[9]: 'C:\\Shixiang\\pybook\\files\\chapter10'
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

## 10.4 pickle 文件

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

## 10.5 SAS 与 Stata 文件

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

## 10.6 HDF5 文件

HDF（Hierarchical Data Format）指一种为存储和处理大容量科学数据设计的文件格式及相应库文件。HDF 最早由美国国家超级计算应用中心 NCSA 开发，目前在非盈利组织 HDF 小组维护下继续发展。当前流行的版本是 HDF5。HDF5 拥有一系列的优异特性，使其特别适合进行大量科学数据的存储和操作，如它支持非常多的数据类型，灵活，通用，跨平台，可扩展，高效的 I/O 性能，支持几乎无限量的单文件存储等。它的官网地址为：https://support.hdfgroup.org/HDF5/。

在正式学习如何导入和操作 HDF5 文件之前，我们先来了解下它的主要特点。

一个 HDF5 文件是存储两类对象的容器，这两类对象分别为：

- dataset：类似数组的数据集合；
- group；结构类似目录的容器，其中可以包含一个或多个 dataset 及其它的 group。

一个 HDF5 文件从一个命名为 "/" 的 group 开始，所有的 dataset 和其它 group 都包含在此 group 下。当操作 HDF5 文件时，如果没有显式指定 group 的 dataset 都是默认指 "/" 下的 dataset。

HDF5 文件的 dataset 和 group 都可以拥有描述性的元数据，称作 attribute（属性）。

Python 中有一系列的工具可以操作和使用 HDF5 数据，其中最常用的是 h5py 和 PyTables。用 h5py 操作 HDF5 文件，我们可以像使用目录一样使用 group，像使用 NumPy 数组一样使用 dataset，像使用字典一样使用属性，非常方便和易用。

接下来具体介绍如何使用 h5py 进行导入时间序列数据，并进行简单的可视化。

```python
In [6]: import h5py
In [7]: import numpy as np
In [8]: import matplotlib.pyplot as plt
In [9]: filename = 'data.hdf5'
In [10]: data = h5py.File(filename, 'r')  # 读入 data.hdf5
In [11]: print(type(data))  # 查看对象类型
<class 'h5py._hl.files.File'>
In [12]: group = data['strain']  # 获取 HDF5 的 group
In [13]: # 检查 group 的键
In [13]: for key in group.keys():
    ...:     print(key)
    ...:
Strain
In [14]: # 获取数据集的值
In [14]: strain = data['strain']['Strain'].value
In [15]: # 设定采样数
    ...: s
    ...: num_samples = 10000
    ...:
    ...: # 设定时间向量
    ...: time = np.arange(0, 1, 1/num_samples)
In [16]: # 绘图
    ...: plt.plot(time, strain[:num_samples])
    ...: plt.xlabel('GPS Time (s)')
    ...: plt.ylabel('strain')
    ...: plt.show()
```

结果图形如图11-1所示。

![图10-1 HDF5 存储的时间序列数据可视化](images/chapter10/hdf5_time_series.png)

上述代码将 HDF5 文件导入为一个 h5py 类实例，该对象有自己一套操作方法，读者仅仅依靠上面这个简单的例子不足以掌握它们，如果读者比较感兴趣，请通过网络资料或其他参考书籍自行学习和练习。

## 10.7 MATLAB 文件

MATLAB 是 matrix 和 laboratory 两个词的组合，译作矩阵实验室。它是由美国 mathworks 公司发布的主要面对科学计算、可视化以及交互式程序设计的高科技计算环境。MATLAB 主要应用于科学计算、工程技术等领域，与工业界结合非常紧密，也是深度学习应用的主要平台之一。

MATLAB 所使用的数据格式以 mat 为文件拓展名，在 Python 中可以通过来自 scipy.io 模块中的 loadmat() 和 savemat() 函数进行读写。下面的代码片段提供了一个数据导入的操作范例。

```python
import scipy.io
filename = 'xxx.mat'
# 读入 mat 文件
mat = scipy.io.loadmat(filename)
print(type(mat))
# mat['x'] 中的 x 是
# MATLAB 文件中的变量 x，
# mat['x'] 是 变量 x 的值
print(type(mat['x']))
print(mat['x'])
```

不难理解，mat 文件中存储的变量名和相应值（来自 MATLAB）转换为了 Python 中的键值对形式。

## 10.8 json 文件

JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation），它是轻量级的文本数据交换格式，易于人阅读和编写。同时也易于机器解析和生成，并有效地提升网络传输效率。JSON 虽然使用 Javascript 语法来描述数据对象，但是它完全独立于编程语言和平台。目前非常多的动态（PHP、Python、R）编程语言都支持 JSON。

JSON 的语法规则如下：

- 数据在名称/值对中
- 数据由逗号分隔
- 大括号保存对象
- 中括号保存数组

下面给出一个对象示例：

```json
{ "名字": "Mike Wang" , "个人主页":"www.xxx.com" }
```

当存在多个数据时，则可以用数组表示。

```json
{
    "sites": [
        { "名字": "Mike Wang" , "个人主页":"www.xxx.com" },
        { "名字": "Mike Zhang" , "个人主页":"www.xx1.com" },
        { "名字": "Mike Li" , "个人主页":"www.xx2.com" }
        ]
    }
```

不难发现，这种结构在 Python 中就是列表和字典的嵌套，因此使用 Python 非常容易完成 JSON 的解析。Python 提供了一个标准模块 json 专门处理这项工作，其中 loads()、load() 函数用于将 JSON 结构解析为 Python 对象，dumps()、dump() 函数用于将 Python 对象解析为 JSON 结构。这里，带 s 结尾的函数的用处是处理非文本对象，而不带 s 结尾的函数用处是处理文件，请读者注意区分。

我们先通过一个简单的示例了解 loads() 和 dumps() 两个函数的用法。

```python
In [1]: import json
In [2]: json_data = '{ "名字": "Mike Wang" , "个人主页":"www.x
   ...: xx.com" }'
In [3]: json.loads(json_data)  # 解析 json 数据为字典
Out[3]: {'名字': 'Mike Wang', '个人主页': 'www.xxx.com'}
In [4]: data = json.loads(json_data)
In [5]: json.dumps(data)  # 将字典解析为 json 数据
Out[5]: '{"\\u540d\\u5b57": "Mike Wang", "\\u4e2a\\u4eba\\u4e3b\\u9875": "www.xxx.com"}'
```

Python 与 JSON 的对应关系如下表所示：

| Python 对象  | JSON 等价物  |
|---|---|
| 字典 | 对象 |
| 列表、元组| 数组|
| 字符串 | 字符串 |
| 数值 | 数值 |
| True | true |
| False | false |
| None | null |

下面是一些简单的测试：

```python
In [7]: json.dumps([1, 2, 3])
Out[7]: '[1, 2, 3]'
In [8]: json.dumps(True)
Out[8]: 'true'
In [9]: json.dumps(None)
Out[9]: 'null'
In [10]: json.dumps(('a', 'b', 'c'))
Out[10]: '["a", "b", "c"]'
```

load() 和 dump() 这两个函数的输入是文本对象，读者根据前面所学的知识可以推测使用下面的代码应该可以导入 JSON 文件。

```python
with open('xxx.json') as f:
  data = json.load(f)
```

现在我们试一试：

```python
In [12]: with open('files/chapter10/data.json', 'r', encoding=
    ...: 'utf-8') as f:
    ...:     data = json.load(f)
    ...:
In [13]: data
Out[13]:
{'sites': [{'名字': 'Mike Wang', '个人主页': 'www.xxx.com'},
  {'名字': 'Mike Zhang', '个人主页': 'www.xx1.com'},
  {'名字': 'Mike Li', '个人主页': 'www.xx2.com'}]}
```

用法的确是这样的。利用 dump() 函数和类似的操作，读者不妨试试将 Python 对象导出保存为 JSON 文件。

## 10.9 YAML 文件

YAML 是 "Yet Another Markup Language"（仍是一种标记语言）的缩写，它常见于配置文件，如 Markdown 文档的文件头元信息注释就常常采用 YAML 格式。YAML 可以简单表达清单、散列表，标量等数据形态。它使用空白符号缩进和大量依赖外观的特色，巧妙避开各种封闭符号，如：引号、各种括号等，这些符号在嵌套结构时会变得复杂而难以辨认，因而特别适合用来表达或编辑数据结构、各种配置文件、倾印调试内容、文件大纲。

下面是一个 YAML 格式的简单示例：

```yaml
a string: bla
another dict:
  foo: bar
  key: value
  the answer: 42
```

YAML 与 JSON 格式的关系很亲密，JSON 的语法是 YAML 1.2 版的子集，因此大部分的 JSON 文件都可以被 YAML 的剖析器剖析。虽然 YAML 也可以采用类似 JSON 的写法，不过 YAML 标准并不建议这样使用，除非这样编写能让文件可读性增加。

YAML 遵循以下规则：

- 使用英文井号进行注释标识，这与 Python 一致；
- 使用缩进表示层级关系，并只能使用空格缩进，不能使用制表符；
- 区分大小写；
- 缩进的空格数目不固定，只需要相同层级的元素左侧对齐；
- 文件中的字符串不需要使用引号标注，但若字符串包含有特殊字符则需用引号标注；

这里提醒读者注意第二点，因为 Python 是同时支持空格和制表符缩进的，只要在书写代码块时保持一致即可，而 YAML 不支持制表符缩进，这样如果我们工作时同时编辑和处理 Python 和 YAML 文件时稍不注意 YAML 可能会产生意想不到的语法错误。最好的解决办法是对代码编辑器设定将制表符转换为特定数目的空格符，一般是 4 个或者 2 个，这样我们就可以对所有文件使用制表符缩进了。具体的办法请读者自行搜索解决。

YAML 支持的数据结构如下：

- 对象：键值对的集合，类似 Python 中的字典；
- 数组：一组按序排列的值，简称 "序列或列表"。数组前加有 “-” 符号，符号与值之间需用空格分隔；
- 标量：单个的、不可再分的值，如：字符串、bool 值、整数、浮点数、时间、日期、null 等；
- None：空值，用 null 或 ~ 表示。

下面是常见标量的表示方式：

```yaml
字符串: name
特殊: "name\n"
数值: 3.14
布尔值: true
空值: null
空值2: ~
时间值: 2019-11-11t11:33:22.55-06:00
日期值: 2019-11-11
```

Python 提供了 yaml 模块以进行 YAML 文件的解析，使用方法和函数名都与 json 类似，即使用文件操作函数 open() 文件，使用 safe_load() 解析 YAML 文件（load() 函数也可以使用，但不安全），使用 dump() 保存 YAML 文件。

下面就 YAML 文件的导入举两个例子，导出与操作 JSON 文件一致，因而不再赘述。

第一个例子是将上面展示的标量表示方式保存到 YAML 文件 data1.yml 中（YAML 一般以 .yml 作为文件拓展名），我们使用 Python yaml 模块解析看看它们在 Python 的表现方式。

```python
In [1]: import yaml
In [2]: with open('files/chapter10/data1.yml', encoding='utf-8') as f:
    ...:     data = yaml.safe_load(f)
    ...:
In [3]: data
Out[3]:
{'字符串': 'name',
 '特殊': 'name\n',
 '数值': 3.14,
 '布尔值': True,
 '空值': None,
 '空值2': None,
 '时间值': datetime.datetime(2019, 11, 11, 17, 33, 22, 550000),
 '日期值': datetime.date(2019, 11, 11)}
```

结果显示是一个 Python 字典，每一行的内容都转换为了一个键值对。

我们再观察一个嵌套键值对和数组的结果。

```python
user1:
  type: user
  name: a
  password: 123
user2:
  type: user
  name: b
  password: 456
user3:
  type: group
  name:
    - aa
    - bb
    - cc
  password:
    - 123
    - 456
    - null
summary:
  - user1
  - user2
  - user3
```

上面我们虚构了一组简单地用户管理数据，用户 user1 和 user1 是个体用户，user3 是群组用户。

```python
In [12]: with open('files/chapter10/data2.yml', encoding='utf-8') as f:
    ...:     data = yaml.safe_load(f)
    ...:

In [13]: data
Out[13]:
{'user1': {'type': 'user', 'name': 'a', 'password': 123},
 'user2': {'type': 'user', 'name': 'b', 'password': 456},
 'user3': {'type': 'group',
  'name': ['aa', 'bb', 'cc'],
  'password': [123, 456, None]},
 'summary': ['user1', 'user2', 'user3']}
 ```

 读者不妨对比上一节介绍的 JSON 和本节介绍的 YAML，从视觉感官来看，虽然两者都比较容易看懂，YAML 的写法更加易读，而 JSON 的写法更加容易和 Python 解析后展示的结果直观对应起来。可能就是这种差异让出处相同、用处相同的两者在实际的应用方向上存在差异：JSON 常用于数据交换（机器解读），而 YAML 常用作配置文件（人类编辑）。

## 10.10 网页数据

网页数据的解析常与一个广泛流行的领域“爬虫”相关联。本书不会对涉及爬虫技术的解读，但有必要向读者简单介绍下网页数据格式和简单的处理办法。

我们目前所浏览的网页全部是一种叫作“超文本标记语言”（HyperText Markup Language），简称 HTML 的文件。超文本是一种组织信息的方式，它包括一系列标签．通过这些标签可以将网络上的文档格式统一，文字、图表与其他信息媒体相关联。这些相互关联的信息媒体可能在同一文本中，也可能是其他文件，或是地理位置相距遥远的某台计算机上的文件。

如果我们在本地浏览 HTML 文件，它就是一个简单的带有各种标签的文本，它必须在浏览器上运行和被浏览器解析才能观察到相应的网页效果。

下面是一个简单的 HTML 文件内容，它设定了一个网页的标题、内容标题和段落文字。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>一个网页</title>
</head>
<body>
    <h1>第一个标题</h1>
    <p>第一个段落。</p>
</body>
</html>
```

读者可以将它存储到一个以 .html 作为文件拓展名的文件中，然后用浏览器打开它查看网页的显示效果。

虽然内容比较短，但我们也可以轻易地从中发现 HTML 格式的规律，它使用的大部分标签都是以 \<tag> 的形式开始，以 \</tag> 的形式结束，它的标签作用一般由对应的英文所展示，所以也比较容易理解。

进一步，如果我们如果把这些标签想象为树的结构，可以得到以下的信息：

```
html
|__ head
|   |__ title: 一个网页
|
|__ body
    |__ h1: 第一个标题
    |__ p: 第一个段落
```

当然，我们上网浏览的网页都比这要复杂得多。互联网中，HTML 这种树结构中存储着巨量的信息，作为数据分析人员我们有时候不可避免要面对解析它们。

Python 标准模块 html.parser 提供一个简单的 HTML 解析器，这个模块定义了一个 HTMLParser 类，该类的实例用来接受 HTML 数据，并在标记开始、标记结束、文本、注释和其他元素标记出现的时候调用对应的方法。要实现具体的行为，我们需要使用 HTMLParser 的子类并重载其方法。

下面是一个来自 Python 官方文档的示例：

```python
In [1]: from html.parser import HTMLParser
   ...:
   ...: class MyHTMLParser(HTMLParser):
   ...:     def handle_starttag(self, tag, attrs):
   ...:         print("Encountered a start tag:", tag)
   ...:
   ...:     def handle_endtag(self, tag):
   ...:         print("Encountered an end tag :", tag)
   ...:
   ...:     def handle_data(self, data):
   ...:         print("Encountered some data  :", data)
   ...:
   ...: parser = MyHTMLParser()
   ...: parser.feed('<html><head><title>Test</title></head>'
   ...:             '<body><h1>Parse me!</h1></body></html>')
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html
```

接下来我们试着用这个解析器解析上面的 HTML 文件。

```python
In [2]: with open('files/chapter10/data.html', encoding='utf=8') as f:
   ...:    parser.feed(f.read())
   ...:
Encountered some data  :

Encountered a start tag: html
Encountered some data  :

Encountered a start tag: head
Encountered some data  :

Encountered a start tag: meta
Encountered some data  :

Encountered a start tag: title
Encountered some data  : 一个网页
Encountered an end tag : title
Encountered some data  :

Encountered an end tag : head
Encountered some data  :

Encountered a start tag: body
Encountered some data  :

Encountered a start tag: h1
Encountered some data  : 第一个标题
Encountered an end tag : h1
Encountered some data  :

Encountered a start tag: p
Encountered some data  : 第一个段落。
Encountered an end tag : p
Encountered some data  :

Encountered an end tag : body
Encountered some data  :

Encountered an end tag : html
Encountered some data  :
```

通过对上述程序增加判断语句，我们可以提取自己感兴趣的数据。不过对于 Python 初学者来说，我们有更好的选择，那就是大名鼎鼎的 BeautifulSoup 包。

例如，我们要提取上面 h1 标签存储的信息：

```python
In [3]: from bs4 import BeautifulSoup
In [4]: with open('files/chapter10/data.html', encoding='utf=8') as f:
   ...:    html_data = f.read()
In [5]: parsed_html = BeautifulSoup(html_data)  # 构建数据对象
In [6]: parsed_html.body.find('h1').text        # 查找 h1 并获取内容
Out[6]: '第一个标题'
```

爬虫技术和 BeautifulSoup 包的使用方法实在太过丰富，HTML 也是一门语言，因为一时难以详尽，本书都不宜进行过多介绍。感兴趣的读者请阅读官方网站 https://www.crummy.com/software/BeautifulSoup/ 和购买专业的爬虫技术书籍进行学习。

## 10.11 数据库数据

本章的最后一节本书对读写数据库进行简单的介绍。商业分析的工作者通常需要掌握数据库操作，而数据科学家们则比较少使用数据库。

J.Martin 给数据库下了一个比较完整的定义：

> 数据库是存储在一起的相关数据的集合，这些数据是结构化的，无有害的或不必要的冗余，并为多种应用服务；数据的存储独立于使用它的程序；对数据库插入新数据，修改和检索原有数据均能按一种公用的和可控制的方式进行。当某个系统中存在结构上完全分开的若干个数据库时，则该系统包含一个“数据库集合”。

使用数据库可以带来许多好处：如减少了数据的冗余度，从而大大地节省了数据的存储空间；实现数据资源的充分共享等等。

目前数据库可以分为两类：

- 关系型数据库 - 指采用了关系模型来组织数据的数据库。关系模型指的就是二维表格模型，而一个关系型数据库就是由二维表及其之间的联系所组成的一个数据组织。简单地说，它的数据格式就像含有多张紧密表格的 Excel 文件。当前主流的关系数据库有 Oracle，Microsoft SQL Server、MySQL、PostgreSQL、DB2、Microsoft Access、SQLite、Teradata、MariaDB、SAP 等；
- 非关系型数据库 - 指非关系型的，分布式的。非关系型数据库以键值对存储，且结构不固定，每一个元组可以有不一样的字段，每个元组可以根据需要增加一些自己的键值对，不局限于固定的结构，可以减少一些时间和空间的开销。其实就是本书在前面介绍过的 JSON 格式。非关系数据库的主要代表有 Redis、Amazon DynamoDB、Memcached、Microsoft Azure Cosmos DB。

关系型数据库都是需要通过 SQL 语句进行操作，SQL 是结构化查询语言（Structured Query Language）的缩写，它是一种具有特定用途的编程语言，用于存取数据以及查询、更新和管理关系数据库系统。因而关系型数据库通常被称为 SQL 数据库，而非关系型数据库则称为 NoSQL 数据库。SQL 的内容超出本书范围，请读者参考网络资料和专业书籍进行学习。

大部分的数据库都是由商业公司发布，体积都比较庞大，安装麻烦，而且有的需要收费。目前主流还是关系型数据库，下面选择 SQLite 进行学习。SQLite 是开源软件，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎，在世界上部署最为广泛。

在 Python 中使用 SQLite 需要 sqlite3 模块。下面的代码展示了如何创建（连接）数据库、创建游标、创建表格、对表格操作、提交修改、关闭数据库整个流程。所有的数据库都遵循相似的操作流程。

```python
# 导入模块
import sqlite3
# 连接数据库
connection = sqlite3.connect("data.db")
# 创建游标
crsr = connection.cursor()
# 对数据库使用 SQL 语句创建表格
sql_command = """CREATE TABLE emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""
# 执行 SQL 语句
crsr.execute(sql_command)
# 使用 SQL 语句在表格中插入数据
sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command)
# 再次插入数据
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command)
# 提交修改到数据库（如果不执行该操作，上面的修改将不会保存）
connection.commit()
# 关闭数据库连接
connection.close()
```

现在我们已经创建数据并存储在数据库中，当我们需要使用这些数据时，就可以连接数据库并获取数据，下面展示了数据获取的流程。

```python
# 导入模块
import sqlite3
# 连接 data 数据库
connection = sqlite3.connect("data.db")
# 创建游标
crsr = connection.cursor()
# 从表格 emp 中查询数据
crsr.execute("SELECT * FROM emp")
# 将数据存储到 ans 变量
ans= crsr.fetchall()
# 循环打印数据
for i in ans:
    print(i)
# 关闭数据库连接
connection.close()
```

不难看出，操作数据库有一个通用的模式：

- 导入需要的模块
- 连接数据库
- 创建游标对象
- 执行数据操作，主要是执行 SQL 语句
- 关闭数据库连接

## 10.12 章末小结

本章从最广泛使用的数据文件格式 CSV 出发，逐步介绍了常见数据格式的导入方法。CSV 和 Excel 数据的导入操作读者需要掌握的，而其他一些数据格式则需要读者根据自己的实际需求进行深入学习，本书所做的是初步的介绍和引导。网络数据和数据库数据的处理很复杂，本书的举例的较为简单，希望能够帮助读者对这些数据有所了解。数据分析涉及各行各业，不同的读者进行数据处理面对的数据格式，数据结构特点都可能有所不同，希望读者通过本章的学习能够学习到与自己领域相关数据的导入方式，并对 Python 的处理能力有更清晰的认识。

