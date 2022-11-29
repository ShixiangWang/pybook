In [1]: import numpy as np
In [2]: a = np.arange(9)
In [3]: a
# Out[3]: array([0, 1, 2, 3, 4, 5, 6, 7, 8])
In [4]: b = np.arange(9).reshape((3, 3))
In [5]: b
# Out[5]:
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
In [6]: import pandas as pd
In [7]: pd.RangeIndex(10)
# Out[7]: RangeIndex(start=0, stop=10, step=1)
In [8]: a_series = pd.Series([5, 7, 9])
In [9]: a_series.index
# Out[9]: RangeIndex(start=0, stop=3, step=1)
In [10]: a_series = pd.Series([5, 7, 9], index = ['user1', 'user2', 'user3'])
In [11]: a_series
# Out[11]:
user1    5
user2    7
user3    9
dtype: int64
In [12]: a_series = pd.Series([5, 7, 9], index = ['user1', 'user2', 'user3'], name='credit_score')
In [13]: a_series
# Out[13]:
user1    5
user2    7
user3    9
Name: credit_score, dtype: int64
In [14]: df = pd.DataFrame([[5, 166], [7, 178], [9, 160]],
    ...: index=['student1', 'student2', 'student3'], columns=['score', 'height'])
In [15]: df
# Out[15]:
          score  height
student1      5     166
student2      7     178
student3      9     160
In [16]: pd.Series(['a', 'a', 'b', 'c', 'b'], dtype='category')
# Out[16]:
0    a
1    a
2    b
3    c
4    b
dtype: category
Categories (3, object): [a, b, c]
In [17]: pd.Series(['a', 'a', 'b', 'c', 'b'])
# Out[17]:
0    a
1    a
2    b
3    c
4    b
dtype: object
In [2]: pd.Categorical(['a', 'a', 'b', 'c', 'b'])
# Out[2]:
[a, a, b, c, b]
Categories (3, object): [a, b, c]
pd.Categorical(
    values,
    categories=None,
    ordered=None,
    dtype=None,
    fastpath=False,
)
In [6]: pd.Categorical(['a', 'a', 'b', 'c', 'b'], categories=['a', 'c'])
# Out[6]:
[a, a, NaN, c, NaN]
Categories (2, object): [a, c]

In [7]: pd.Categorical(['a', 'a', 'b', 'c', 'b'], ordered=True)
# Out[7]:
[a, a, b, c, b]
Categories (3, object): [a < b < c]
In [9]: cts = pd.Categorical(['a', 'a', 'b', 'c', 'b'], ordered=True)
In [10]: cts.describe()
# Out[10]:
            counts  freqs
categories
a                2    0.4
b                2    0.4
c                1    0.2
In [11]: cts.categories
# Out[11]: Index(['a', 'b', 'c'], dtype='object')
In [12]: cts.ordered
# Out[12]: True
In [13]: cts_new = cts.copy()
In [14]: cts_new.categories = ['aa', 'bb', 'cc']
In [15]: cts
# Out[15]:
[a, a, b, c, b]
Categories (3, object): [a < b < c]
In [16]: cts_new
# Out[16]:
[aa, aa, bb, cc, bb]
Categories (3, object): [aa < bb < cc]
In [17]: cts_new.add_categories(['ff'])
# Out[17]:
[aa, aa, bb, cc, bb]
Categories (4, object): [aa < bb < cc < ff]
In [19]: cts_new.remove_categories("bb")
# Out[19]:
[aa, aa, NaN, cc, NaN]
Categories (2, object): [aa < cc]
In [23]: cts
# Out[23]:
[a, a, b, c, b]
Categories (3, object): [a < b < c]

In [24]: cts2 = pd.Categorical(['b', 'c', 'a', 'a'], ordered=True)
In [25]: cts > cts2
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-25-d954cff14835> in <module>
----> 1 cts > cts2

~/miniconda3/lib/python3.7/site-packages/pandas/core/arrays/categorical.py in f(self, other)
    113                 other_codes = other._codes
    114
--> 115             mask = (self._codes == -1) | (other_codes == -1)
    116             f = getattr(self._codes, op)
    117             ret = f(other_codes)

ValueError: operands could not be broadcast together with shapes (5,) (4,)
In [26]: cts2 = pd.Categorical(['b', 'c', 'a', 'a', 'a'], ordered=True)
In [27]: cts > cts2
# Out[27]: array([False, False,  True,  True,  True])
In [28]: cts > 'b'
# Out[28]: array([False, False, False,  True, False])
In [32]: import time
In [33]: time.time()
# Out[33]: 1576340722.0232272
In [34]: time.localtime(time.time())
# Out[34]: time.struct_time(tm_year=2019, tm_mon=12, tm_mday=15, tm_hour=10, tm_min=6, tm_sec=45, tm_wday=6, tm_yda
y=349, tm_isdst=0)
In [36]: time.asctime(time.localtime(time.time()))
# Out[36]: 'Sun Dec 15 10:09:29 2019'
In [37]: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# Out[37]: '2019-12-15 10:28:23'
In [39]: now = datetime.datetime.now()  # 当前本地时间
In [40]: now
# Out[40]: datetime.datetime(2019, 12, 15, 10, 34, 54, 516482)
In [41]: utc = datetime.datetime.utcnow()  # 当前世界标准时
In [42]: utc
# Out[42]: datetime.datetime(2019, 12, 15, 2, 35, 18, 609633)
In [45]: now.timestamp()  # 当前时间戳
# Out[45]: 1576377294.516482
In [46]: now.strftime("%Y-%m-%d %H:%M:%S")
# Out[46]: '2019-12-15 10:34:54'
In [47]: now2 = datetime.datetime.now()
In [48]: now2 - now
# Out[48]: datetime.timedelta(seconds=486, microseconds=231216)
In [49]: td = now2 - now
In [52]: td.seconds
# Out[52]: 486
In [55]: pd.datetime.now()
# Out[55]: datetime.datetime(2019, 12, 15, 10, 47, 58, 642985)
In [56]: pd.date_range('20190101', periods=7)
# Out[56]:
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
In [58]: pd.date_range('20190101', periods=7, freq='M')
# Out[58]:
DatetimeIndex(['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30',
               '2019-05-31', '2019-06-30', '2019-07-31'],
              dtype='datetime64[ns]', freq='M')

In [59]: pd.bdate_range('20190101', periods=7)
# Out[59]:
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-07', '2019-01-08', '2019-01-09'],
              dtype='datetime64[ns]', freq='B')
In [60]: pd.Timedelta('1 days 2 hours 3 minutes 4 seconds')
# Out[60]: Timedelta('1 days 02:03:04')
In [61]: pd.Timedelta(10, unit='h')
# Out[61]: Timedelta('0 days 10:00:00')
In [64]: pd.Timedelta(days=10)
# Out[64]: Timedelta('10 days 00:00:00')
In [65]: pd.Timedelta(hours=10)
# Out[65]: Timedelta('0 days 10:00:00')
In [66]: pd.Timedelta(minutes=10)
# Out[66]: Timedelta('0 days 00:10:00')
In [67]: pd.date_range('20190101', periods=7)
# Out[67]:
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
In [68]: pd.date_range('20190101', periods=7) + pd.Timedelta(hours=10)
# Out[68]:
DatetimeIndex(['2019-01-01 10:00:00', '2019-01-02 10:00:00',
               '2019-01-03 10:00:00', '2019-01-04 10:00:00',
               '2019-01-05 10:00:00', '2019-01-06 10:00:00',
               '2019-01-07 10:00:00'],
              dtype='datetime64[ns]', freq='D')
In [69]: pd.date_range('20190101', periods=7) - pd.Timedelta(hours=10)
# Out[69]:
DatetimeIndex(['2018-12-31 14:00:00', '2019-01-01 14:00:00',
               '2019-01-02 14:00:00', '2019-01-03 14:00:00',
               '2019-01-04 14:00:00', '2019-01-05 14:00:00',
               '2019-01-06 14:00:00'],
              dtype='datetime64[ns]', freq='D')
In [74]: s = pd.Series(['a', 'b', 'c'])
In [75]: df = df = {'姓名': ['小明','小王','小张'], '语文':[80,85,90], '数学':[99,88,86]}
In [76]: df = pd.DataFrame(df)
In [77]: s
# Out[77]:
0    a
1    b
2    c
dtype: object
In [78]: df
# Out[78]:
   姓名  语文  数学
0  小明  80  99
1  小王  85  88
2  小张  90  86
In [80]: for i in s:
    ...:     print(i)
    ...:
a
b
c
In [81]: for i in df:
    ...:     print(i)
    ...:
姓名
语文
数学
In [82]: for i in s.index:
    ...:     print(i)
    ...:
0
1
2
In [84]: for key, value in df.iteritems():
    ...:     print(key, value)
    ...:
姓名 0    小明
1    小王
2    小张
Name: 姓名, dtype: object
语文 0    80
1    85
2    90
Name: 语文, dtype: int64
数学 0    99
1    88
2    86
Name: 数学, dtype: int64
In [85]: for key, value in df.iteritems():
    ...:     print(type(value))
    ...:
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
In [87]: for key, value in df.iterrows():
    ...:     print(key, value)
    ...:
0 姓名    小明
语文    80
数学    99
Name: 0, dtype: object
1 姓名    小王
语文    85
数学    88
Name: 1, dtype: object
2 姓名    小张
语文    90
数学    86
Name: 2, dtype: object
In [88]: for row, value in df.iterrows():
    ...:     print(type(value))
    ...:
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
In [89]: for key, value in df.itertuples():
    ...:     print(key, value)
    ...:
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-89-6b42ad46ae68> in <module>
----> 1 for key, value in df.itertuples():
      2     print(key, value)
      3

ValueError: too many values to unpack (expected 2)

In [90]: for value in df.itertuples():
    ...:     print(value)
    ...:
Pandas(Index=0, 姓名='小明', 语文=80, 数学=99)
Pandas(Index=1, 姓名='小王', 语文=85, 数学=88)
Pandas(Index=2, 姓名='小张', 语文=90, 数学=86)

In [91]: for value in df.itertuples():
    ...:     print(type(value))
    ...:
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>
In [92]: for value in df.itertuples():
    ...:     print(tuple(value))
    ...:
(0, '小明', 80, 99)
(1, '小王', 85, 88)
(2, '小张', 90, 86)
In [97]: def timer(e1, e2):
    ...:     return(e1*e2)
    ...:
In [98]: df1 = pd.DataFrame(6*np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
In [99]: df1
# Out[99]:
        col1      col2       col3
0  -2.327459  4.391074   8.796776
1   3.736191  2.711543 -11.112365
2  -5.686908 -0.246942  -0.692201
3   4.060646  9.178073   1.355170
4  10.171053 -3.417467   0.447833
5  -7.363384 -0.176782  -6.391243
In [100]: df1.pipe(timer, 10)
# Out[100]:
         col1       col2        col3
0  -23.274593  43.910736   87.967759
1   37.361914  27.115432 -111.123654
2  -56.869085  -2.469423   -6.922007
3   40.606458  91.780725   13.551700
4  101.710534 -34.174668    4.478325
5  -73.633838  -1.767825  -63.912430
In [103]: df1.pipe(timer, pd.DataFrame(6*np.random.randn(6, 3), columns=['col1', 'col2', 'col3']))
# Out[103]:
        col1        col2       col3
0   5.756520  -26.905602  21.285264
1  20.548535  -10.953445 -99.671865
2  -2.653793    1.188218   2.159359
3  15.746131  225.602231  13.177158
4  95.979467   -1.891072   0.294889
5  14.734334    0.651522  27.829243
In [104]: df1 * 10
# Out[104]:
         col1       col2        col3
0  -23.274593  43.910736   87.967759
1   37.361914  27.115432 -111.123654
2  -56.869085  -2.469423   -6.922007
3   40.606458  91.780725   13.551700
4  101.710534 -34.174668    4.478325
5  -73.633838  -1.767825  -63.912430
In [105]: df1 * df1
# Out[105]:
         col1       col2        col3
0    5.417067  19.281527   77.383267
1   13.959126   7.352467  123.484665
2   32.340928   0.060981    0.479142
3   16.488844  84.237015    1.836486
4  103.450327  11.679079    0.200554
5   54.219421   0.031252   40.847987
In [114]: df1.apply(timer, axis=0, e2=10)
# Out[114]:
         col1       col2        col3
0  -23.274593  43.910736   87.967759
1   37.361914  27.115432 -111.123654
2  -56.869085  -2.469423   -6.922007
3   40.606458  91.780725   13.551700
4  101.710534 -34.174668    4.478325
5  -73.633838  -1.767825  -63.912430
In [123]: df1.iloc[:,2].apply(timer, e2=10)
# Out[123]:
0     87.967759
1   -111.123654
2     -6.922007
3     13.551700
4      4.478325
5    -63.912430
Name: col3, dtype: float64

In [124]: df1.iloc[2,].apply(timer, e2=10)
# Out[124]:
col1   -56.869085
col2    -2.469423
col3    -6.922007
Name: 2, dtype: float64
In [125]: df1.applymap(lambda x: 10 * x)
# Out[125]:
         col1       col2        col3
0  -23.274593  43.910736   87.967759
1   37.361914  27.115432 -111.123654
2  -56.869085  -2.469423   -6.922007
3   40.606458  91.780725   13.551700
4  101.710534 -34.174668    4.478325
5  -73.633838  -1.767825  -63.912430
In [126]: df1.applymap(lambda x: x ** 2 if x < 0 else x + 10)
# Out[126]:
        col1       col2        col3
0   5.417067  14.391074   18.796776
1  13.736191  12.711543  123.484665
2  32.340928   0.060981    0.479142
3  14.060646  19.178073   11.355170
4  20.171053  11.679079   10.447833
5  54.219421   0.031252   40.847987
In [127]: sample_data = pd.Series(['Mike', 'Shixiang', np.nan, '012345', 'HAPPY', 'hurry'])
In [128]: sample_data
# Out[128]:
0        Mike
1    Shixiang
2         NaN
3      012345
4       HAPPY
5       hurry
dtype: object
In [129]: sample_data.str.lower()
# Out[129]:
0        mike
1    shixiang
2         NaN
3      012345
4       happy
5       hurry
dtype: object
In [130]: sample_data.str.upper()
# Out[130]:
0        MIKE
1    SHIXIANG
2         NaN
3      012345
4       HAPPY
5       HURRY
dtype: object
In [131]: sample_data.str.len()
# Out[131]:
0    4.0
1    8.0
2    NaN
3    6.0
4    5.0
5    5.0
dtype: float64
In [132]: sample_data.str.replace('H', 'YY')
# Out[132]:
0        Mike
1    Shixiang
2         NaN
3      012345
4      YYAPPY
5       hurry
dtype: object
In [133]: sample_data.str.count('a')
# Out[133]:
0    0.0
1    1.0
2    NaN
3    0.0
4    0.0
5    0.0
dtype: float64
In [134]: sample_data.str.swapcase()
# Out[134]:
0        mIKE
1    sHIXIANG
2         NaN
3      012345
4       happy
5       HURRY
dtype: object
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                               'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
In [136]: df
# Out[136]:
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0

In [137]: df.groupby(['Animal']).mean()
# Out[137]:
        Max Speed
Animal
Falcon      375.0
Parrot       25.0
In [138]: df = pd.DataFrame(np.random.randn(4, 4), index = ['user1', 'user2', 'user3', 'user4'], columns=['c
     ...: ol1', 'col2', 'col3', 'col4'])
In [139]: df
# Out[139]:
           col1      col2      col3      col4
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
In [141]: df = df.reindex(['user0', 'user1', 'user2', 'user3', 'user4', 'user5'])
In [142]: df
# Out[142]:
           col1      col2      col3      col4
user0       NaN       NaN       NaN       NaN
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
user5       NaN       NaN       NaN       NaN
In [143]: df.isnull()
# Out[143]:
        col1   col2   col3   col4
user0   True   True   True   True
user1  False  False  False  False
user2  False  False  False  False
user3  False  False  False  False
user4  False  False  False  False
user5   True   True   True   True

In [144]: df.col1.isnull()
# Out[144]:
user0     True
user1    False
user2    False
user3    False
user4    False
user5     True
Name: col1, dtype: bool
In [145]: df.sum()
# Out[145]:
col1   -0.788979
col2    2.810636
col3   -0.609939
col4   -5.659715
dtype: float64

In [146]: pd.Series([np.nan, np.nan]).sum()
# Out[146]: 0.0

In [147]: pd.Series([np.nan, np.nan]).mean()
# Out[147]: nan
In [148]: df.fillna(0)
# Out[148]:
           col1      col2      col3      col4
user0  0.000000  0.000000  0.000000  0.000000
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
user5  0.000000  0.000000  0.000000  0.000000
In [150]: df.fillna(method='pad')   # 向前填充
# Out[150]:
           col1      col2      col3      col4
user0       NaN       NaN       NaN       NaN
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
user5 -1.042709  1.022162 -0.686548 -1.497647

In [151]: df.fillna(method='backfill')  # 向后填充
# Out[151]:
           col1      col2      col3      col4
user0  0.368869  1.021476 -0.771651 -1.908077
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
user5       NaN       NaN       NaN       NaN
In [152]: df.dropna()
# Out[152]:
           col1      col2      col3      col4
user1  0.368869  1.021476 -0.771651 -1.908077
user2  0.023887  0.799769 -0.230265 -0.800586
user3 -0.139025 -0.032772  1.078525 -1.453405
user4 -1.042709  1.022162 -0.686548 -1.497647
In [153]: df.dropna(axis=1)
# Out[153]:
Empty DataFrame
Columns: []
Index: [user0, user1, user2, user3, user4, user5]
pd.merge(
    left,
    right,
    how='inner',
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=False,
    suffixes=('_x', '_y'),
    copy=True,
    indicator=False,
    validate=None,
)
In [155]: stories = pd.DataFrame({'story_id':[1,2,3], 'title':['lions', 'tigers', 'bears']})

In [156]: data = pd.DataFrame({'subject':[1,2,1,2], 'story_id':[1,2,5,6], 'rating':[6.7, 7.8, 3.2, 9.0]})

In [157]: stories
# Out[157]:
   story_id   title
0         1   lions
1         2  tigers
2         3   bears

In [158]: data
# Out[158]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
In [159]: pd.merge(stories, data, how='left', on='story_id')
# Out[159]:
   story_id   title  subject  rating
0         1   lions      1.0     6.7
1         2  tigers      2.0     7.8
2         3   bears      NaN     NaN
In [160]: pd.merge(stories, data, how='right', on='story_id')
# Out[160]:
   story_id   title  subject  rating
0         1   lions        1     6.7
1         2  tigers        2     7.8
2         5     NaN        1     3.2
3         6     NaN        2     9.0

In [161]: pd.merge(data, stories, how='left', on='story_id')
# Out[161]:
   subject  story_id  rating   title
0        1         1     6.7   lions
1        2         2     7.8  tigers
2        1         5     3.2     NaN
3        2         6     9.0     NaN
In [162]: pd.merge(stories, data, how='outer', on='story_id')
# Out[162]:
   story_id   title  subject  rating
0         1   lions      1.0     6.7
1         2  tigers      2.0     7.8
2         3   bears      NaN     NaN
3         5     NaN      1.0     3.2
4         6     NaN      2.0     9.0
In [163]: pd.merge(stories, data, how='inner', on='story_id')
# Out[163]:
   story_id   title  subject  rating
0         1   lions        1     6.7
1         2  tigers        2     7.8
In [168]: data2 = pd.merge(stories, data, how='inner', on='story_id')

In [169]: data
# Out[169]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0

In [170]: pd.merge(data2, data, how='inner', on=['story_id', 'subject'])
# Out[170]:
   story_id   title  subject  rating_x  rating_y
0         1   lions        1       6.7       6.7
1         2  tigers        2       7.8       7.8
In [171]: data = pd.DataFrame({'subject':[1,2,1,2], 'story_id':[1,2,5,6], 'rating':[6.7, 7.8, 3.2, 9.0]})
In [172]: data2 = pd.DataFrame({'subject':[1,2], 'story_id':[3, 4], 'rating':[5, 9.7]})

In [173]: data
# Out[173]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0

In [174]: data2
# Out[174]:
   subject  story_id  rating
0        1         3     5.0
1        2         4     9.7
In [175]: pd.concat([data, data2])
# Out[175]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
0        1         3     5.0
1        2         4     9.7
In [176]: pd.concat([data, data2], keys=['data', 'data2'])
# Out[176]:
         subject  story_id  rating
data  0        1         1     6.7
      1        2         2     7.8
      2        1         5     3.2
      3        2         6     9.0
data2 0        1         3     5.0
      1        2         4     9.7
In [177]: pd.concat([data, data2], keys=['data', 'data2'], ignore_index=True)
# Out[177]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
4        1         3     5.0
5        2         4     9.7

In [178]: pd.concat([data, data2],  ignore_index=True)
# Out[178]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
4        1         3     5.0
5        2         4     9.7
In [180]: pd.concat([data, data2],  axis=1)
# Out[180]:
   subject  story_id  rating  subject  story_id  rating
0        1         1     6.7      1.0       3.0     5.0
1        2         2     7.8      2.0       4.0     9.7
2        1         5     3.2      NaN       NaN     NaN
3        2         6     9.0      NaN       NaN     NaN
In [181]: pd.concat([data, data2],  ignore_index=True, axis=1)
# Out[181]:
   0  1    2    3    4    5
0  1  1  6.7  1.0  3.0  5.0
1  2  2  7.8  2.0  4.0  9.7
2  1  5  3.2  NaN  NaN  NaN
3  2  6  9.0  NaN  NaN  NaN
In [182]: data.append(data2)
# Out[182]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
0        1         3     5.0
1        2         4     9.7
In [185]: data.append(pd.Series({'subject':1, 'story_id':10, 'rating':7}, name=6))
# Out[185]:
   subject  story_id  rating
0        1         1     6.7
1        2         2     7.8
2        1         5     3.2
3        2         6     9.0
6        1        10     7.0
In [187]: mtcars = pd.read_csv('files/chapter10/mtcars.csv')
In [188]: mtcars.describe()
# Out[188]:
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

In [189]: mtcars.shape
# Out[189]: (32, 11)
In [193]: df = mtcars.loc[:, ['cyl', 'mpg']]
In [194]: df.head()
# Out[194]:
   cyl   mpg
0    6  21.0
1    6  21.0
2    4  22.8
3    6  21.4
4    8  18.7
In [195]: %matplotlib inline
In [196]: df.plot()
df.plot(kind='bar')
df.plot(kind='barh')
df.plot(kind='bar', stacked=True)
df2 = df.copy()
df2.index = ['car '+str(i) for i in np.arange(32) + 1]
df2.plot(kind='bar', stacked=True)
df.plot(kind='hist')
df.plot(kind='hist', bins=20)
df.hist(bins=20)
df.plot(kind='box')
# 为了优化显示效果，我们进行了 3 项自定义：
# 去掉网格线
# 旋转 x 轴标签
# 增大字体
df.boxplot(by='cyl', grid=False, rot=45, fontsize=15)
df.plot(kind='area')
df.plot(kind='scatter', x='cyl', y='mpg')
df.cyl.plot(kind='pie')
df.head(5).plot(kind='pie', subplots=True)
