import seaborn as sns
In [1]: import pandas as pd
   ...: import numpy as np
   ...:
   ...: mtcars = pd.read_csv('files/chapter10/mtcars.csv')
In [2]: mtcars.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32 entries, 0 to 31
Data columns (total 11 columns):
mpg     32 non-null float64
cyl     32 non-null int64
disp    32 non-null float64
hp      32 non-null int64drat    32 non-null float64
wt      32 non-null float64
qsec    32 non-null float64
vs      32 non-null int64
am      32 non-null int64
gear    32 non-null int64
carb    32 non-null int64
dtypes: float64(5), int64(6)
memory usage: 2.9 KB
In [3]: mtcars.describe()
# Out[3]:
             mpg        cyl        disp  ...         am       gear     carb
count  32.000000  32.000000   32.000000  ...  32.000000  32.000000  32.0000
mean   20.090625   6.187500  230.721875  ...   0.406250   3.687500   2.8125
std     6.026948   1.785922  123.938694  ...   0.498991   0.737804   1.6152
min    10.400000   4.000000   71.100000  ...   0.000000   3.000000   1.0000
25%    15.425000   4.000000  120.825000  ...   0.000000   3.000000   2.0000
50%    19.200000   6.000000  196.300000  ...   0.000000   4.000000   2.0000
75%    22.800000   8.000000  326.000000  ...   1.000000   4.000000   4.0000
max    33.900000   8.000000  472.000000  ...   1.000000   5.000000   8.0000

[8 rows x 11 columns]
In [4]: import seaborn as sns
In [5]: # 注意在 Jupyter Notebook 中使用 %matplotlib inline
   ...: %matplotlib
Using matplotlib backend: agg
In [6]: sns.pairplot(mtcars.iloc[:, 2:7])
In [7]: sns.pairplot(mtcars.loc[:, ['wt', 'mpg']])
In [8]: sns.pairplot(mtcars.loc[:, ['wt', 'mpg', 'cyl']], hue='cyl')
In [9]: sns.set_style('dark')
In [10]: sns.pairplot(mtcars.loc[:, ['wt', 'mpg', 'cyl']], hue='cyl')
In [11]: sns.set_style('dark')
In [12]: sns.set_palette('colorblind')
In [13]: sns.pairplot(mtcars.loc[:, ['wt', 'mpg', 'cyl']],
    ...: hue='cyl')
In [14]: sns.set_style('whitegrid')
In [15]: sns.pairplot(mtcars,
    ...: hue='cyl',
    ...: vars=['wt', 'mpg', 'cyl'])
In [16]: sns.set_style('white')
In [17]: sns.pairplot(mtcars,
    ...:    hue='cyl',
    ...:    x_vars=['wt', 'mpg'],
    ...:    y_vars=['hp', 'disp'])
In [18]: sns.set_style('ticks')
In [19]: sns.set_palette('dark')
In [20]: sns.pairplot(mtcars,
    ...:    kind='reg',
    ...:    x_vars=['wt', 'mpg'],
    ...:    y_vars=['hp', 'disp'])
In [21]: sns.set_palette('bright')
In [22]: sns.pairplot(mtcars.loc[:, ['wt', 'mpg', 'hp']],
    ...:    kind='reg', diag_kind='kde')
In [23]: sns.barplot(x='cyl', y='mpg', data=mtcars)
In [24]: sns.barplot(x='cyl', y='mpg', hue='vs',
    ...:    data=mtcars)
In [25]: sns.countplot(x='cyl', data=mtcars)
In [26]: sns.pointplot(x='cyl',
    ...:               y='wt',
    ...:               hue='vs',
    ...:               markers=['^', 'o'],
    ...:               linestyles=['-', '--'],
    ...:               data=mtcars)
In [27]: sns.boxplot(x='cyl',
    ...:             y='wt',
    ...:             hue='vs',
    ...:             data=mtcars)
In [28]: sns.violinplot(x='cyl',
    ...:                y='wt',
    ...:                hue='vs',
    ...:                data=mtcars)
In [29]: sns.jointplot(x='mpg', y='wt',
    ...:               data=mtcars,
    ...:               kind='kde')
In [30]: sns.jointplot(x='mpg', y='wt',
    ...:               data=mtcars,
    ...:               kind='reg')
In [31]: from plotnine import *
In [32]: from plotnine.data import mtcars
In [33]: (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
    ...: + geom_point()
    ...: + stat_smooth(method='lm')
    ...: + facet_wrap('~gear'))
In [34]: mtcars.head()
# Out[34]:
    mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
0  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
2  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
3  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
4  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2
In [35]: (ggplot(mtcars, aes(x='wt', y='mpg'))
    ...: + geom_point())
In [36]: ggplot(mtcars, aes(x='wt', y='mpg'))
In [37]: ggplot(mtcars, aes(x='wt', y='mpg')) + geom_point()
In [38]: ggplot(mtcars, aes(x='wt', y='mpg')) + geom_line()
In [39]: (ggplot(mtcars, aes(x='wt', y='mpg'))
    ...: + geom_smooth(method="lm"))
In [40]: (ggplot(mtcars, aes(x='wt', y='mpg'))
    ...: + geom_smooth(method="lm")
    ...: + geom_point())
In [41]: (ggplot(mtcars, aes(x='wt', y='mpg'))
    ...: + geom_smooth(method="lm", color='red')
    ...: + geom_point(color='blue'))
In [42]: (ggplot(mtcars, aes(x='wt', y='mpg'))
    ...: + geom_smooth(method="lm", color="red")
    ...: + geom_point(color="blue")
    ...: + labs(title="Automobie Data", x="Weight", y="Miles Per Gallon"))
In [43]: (ggplot(mtcars, aes(x='hp', y='mpg',
    ...: shape='factor(cyl)', color='factor(cyl)')) +
    ...: geom_point(size=3) +
    ...: facet_grid('am~vs') +
    ...: labs(title="Automobile Data by Engine Type",
    ...:      x="Horsepower", y="Miles Per Gallon"))
In [44]: (ggplot(mtcars, aes(x='hp', y='mpg',
    ...: shape='factor(cyl)', color='cyl')) +
    ...: geom_point(size=3) +
    ...: facet_grid('am~vs') +
    ...: labs(title="Automobile Data by Engine Type",
    ...:      x="Horsepower", y="Miles Per Gallon"))
In [45]: (ggplot(mtcars, aes(x='factor(cyl)', y='mpg'))
    ...: + geom_boxplot(fill='cornflowerblue', color='black', notch=True)
    ...: + geom_point(position='jitter', color='blue', alpha=0.5)
    ...: + geom_rug(sides='l', color='black'))
In [46]: from bokeh.io import output_notebook, show
In [47]: from bokeh.plotting import figure
In [48]: output_notebook()
Loading BokehJS ...
In [49]: # 步骤1：使用 figure() 创建图形对象
    ...: # 并指定图形的宽高
    ...: p = figure(plot_width=400, plot_height=400)
    ...: # 步骤2：添加图形元素
    ...: # 这里绘制点并指定点的一些属性
    ...: # 包括大小、颜色和透明度
    ...: p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5],
    ...:     size=15, line_color="navy",
    ...:     fill_color="orange", fill_alpha=0.5)
    ...: # 步骤3：展示图形
    ...: show(p)
In [50]: p = figure(plot_width=400, plot_height=400)
    ...: p.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5],
    ...:      size=15, color="firebrick", fill_alpha=0.5)
    ...: show(p)
In [51]: p = figure(plot_width=400, plot_height=400)
    ...: p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5],
    ...:      line_width=2)
    ...: show(p)
In [52]: # 构建数据
    ...: x = [1, 2, 3, 4, 5]
    ...: y = [6, 7, 8, 7, 3]
    ...: # 步骤1：
    ...: p = figure(plot_width=400, plot_height=400)
    ...: # 步骤2：
    ...: p.line(x, y, line_width=2)
    ...: p.circle(x, y, fill_color="white", size=8)
    ...: # 步骤3：
    ...: show(p)
In [53]: # 构建数据
    ...: x = [1, 2, 3, 4, 5]
    ...: y = [6, 7, 8, 7, 3]
    ...: # 绘制图形 1
    ...: p1 = figure(plot_width=150, plot_height=150)
    ...: p1.circle(x, y,
    ...:      size=5, line_color="navy",
    ...:      fill_color="orange", fill_alpha=0.5)
    ...: # 绘制图形 2
    ...: p2 = figure(plot_width=150, plot_height=150)
    ...: p2.square(x, y,
    ...:      size=5, color="firebrick", fill_alpha=0.5)
    ...: # 绘制图形 3
    ...: p3 = figure(plot_width=150, plot_height=150)
    ...: p3.line(x, y, line_width=2)
In [54]: from bokeh.layouts import row, column
    ...: # 水平排列
    ...: show(row(p1, p2, p3))
In [55]: # 垂直排列
    ...: show(column(p1, p2, p3))
In [56]: from bokeh.layouts import gridplot
    ...: p = gridplot([[p1, p2], [p3, None]], toolbar_location=None)
    ...: show(p)
