In [1]: import statistics as st # 标准库
   ...: import numpy as np
   ...: import pandas as pd
   ...: mtcars = pd.read_csv('files/chapter10/mtcars.csv')
In [2]: st.mean([1, 2, 3])  # 标准库计算
# Out[2]: 2
In [3]: np.mean([1, 2, 3])  # NumPy 库计算# Out[3]: 2.0
In [4]: pd.Series([1, 2, 3]).mean()  # Pandas 库计算
# Out[4]: 2.0
In [5]: def geo_mean(iterable):
   ...:     a = np.log(iterable)
   ...:     return np.exp(a.sum()/len(a))
In [6]: geo_mean([1, 2, 3])
# Out[6]: 1.8171205928321397
In [7]: from scipy.stats.mstats import gmean
   ...: gmean([1, 2, 3])
# Out[7]: 1.8171205928321397
In [8]: st.median([1, 2, 1000])
# Out[8]: 2
In [9]: np.median([1, 2, 1000])
# Out[9]: 2.0
In [10]: pd.Series([1, 2, 3, 1000]).median()
# Out[10]: 2.5
In [11]: pd.Series([1, 2, 2, 3, 3, 5]).mode()
# Out[11]:
0    2
1    3
dtype: int64
In [12]: a = [1, 2, 3, 1000]    ...: max(a) - min(a)
# Out[12]: 999
In [13]: pd.Series([1, 2, 3, 1]).var()
# Out[13]: 0.9166666666666666
In [14]: pd.Series([1, 2, 3, 1000]).var()
# Out[14]: 249001.66666666666
In [15]: pd.Series([1, 2, 3, 1]).std()
# Out[15]: 0.9574271077563381
In [16]: mtcars.describe()
# Out[16]:
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
In [17]: mtcars.wt.skew()
# Out[17]: 0.4659161067929868
In [18]: %matplotlib # Notebook 使用 %matplotlib inline
    ...: mtcars.wt.plot(kind='kde')
In [19]: mtcars.wt.kurtosis()
# Out[19]: 0.41659466963492564
In [20]: mtcars.cyl.kurtosis()
# Out[20]: -1.7627938970111958
In [21]: mtcars.cyl.plot(kind='kde')
In [22]: from scipy import stats
    ...: import matplotlib.pyplot as plt
    ...: mu = 0 # 均值
    ...: sigma = 1 # 标准差
    ...: x = np.arange(-5,5,0.1)
    ...: y = stats.norm.pdf(x,mu,sigma)  # 生成正态分布概率函数值
    ...: plt.plot(x, y)
    ...: plt.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))
    ...: plt.xlabel('x')
    ...: plt.ylabel('Probability density', fontsize=15)
    ...: plt.show()
In [23]: # 使用rvs()函数模拟一个二项随机变量
    ...: data = stats.binom.rvs(n=10,p=0.5,size=10)
    ...:
    ...: plt.hist(data, density=True)
    ...: plt.xlabel('x')
    ...: plt.ylabel('Probability density', fontsize=15)
    ...: plt.title('Binormal: n=10,$p$=0.5')
    ...: plt.show()
In [24]: data = stats.binom.rvs(n=10,p=0.5,size=1000)
    ...: plt.hist(data, density=True)
    ...: plt.xlabel('x')
    ...: plt.ylabel('Probability density', fontsize=15)
    ...: plt.title('Binormal: n=10,$p$=0.5')
    ...: plt.show()
In [25]: data = stats.bernoulli.rvs(p=0.6, size=10)
    ...: plt.hist(data)
    ...: plt.xlabel('x')
    ...: plt.ylabel('Frequency', fontsize=15)
    ...: plt.title('Bernouli: $p$=0.5')
    ...: plt.show()
In [26]: data = stats.expon.rvs(scale=2,size=1000) # scale参数表示λ的倒数
    ...: plt.hist(data, density=True, bins=20)
    ...: plt.xlabel('x')
    ...: plt.ylabel('Probability density', fontsize=15)
    ...: plt.title('Exponential: 1/$\lambda$=2')
    ...: plt.show()
In [27]: data = stats.poisson.rvs(mu=2,size=1000) # scale参数表示λ的倒数
    ...: plt.hist(data, density=True, bins=20)
    ...: plt.xlabel('x')
    ...: plt.ylabel('Probability density', fontsize=15)
    ...: plt.title('Poisson: $\lambda$=2')
    ...: plt.show()
In [28]: from scipy import stats
    ...: height = [1.75, 1.58, 1.71, 1.64, 1.55, 1.72, 1.62, 1.83, 1.63, 1.65]
    ...: print(stats.ttest_1samp(height, 1.60))
Ttest_1sampResult(statistic=2.550797248729806, pvalue=0.03115396848888224)
In [29]: quality_A = stats.norm.rvs(loc = 9,scale = 10,size = 500)
    ...: quality_B = stats.norm.rvs(loc = 7,scale = 10,size = 500)
    ...:
    ...: _ = plt.hist(quality_A, density=True, alpha=0.5)
    ...: _ = plt.hist(quality_B, density=True, color="red", alpha=0.5)
