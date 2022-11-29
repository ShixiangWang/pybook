In [1]: import numpy as np

In [2]: np_array = np.arange(10000000)

In [3]: py_array = list(range(10000000))

In [4]: %time for i in range(10): np_array * 2
CPU times: user 136 ms, sys: 300 ms, total: 436 ms
Wall time: 435 ms

In [5]: %time for i in range(10): [ x*2 for x in py_array ]
CPU times: user 6.04 s, sys: 1.66 s, total: 7.7 s
Wall time: 7.7 s
In [7]: np.array([1, 3, 5, 7])
# Out[7]: array([1, 3, 5, 7])
In [8]: np.array((2, 4, 6, 8))
# Out[8]: array([2, 4, 6, 8])

In [9]: np.array(2, 4, 6, 8)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-9-1ec14a5e9a23> in <module>()
----> 1 np.array(2, 4, 6, 8)

ValueError: only 2 non-keyword arguments accepted
In [10]: np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
# Out[10]:
array([[1, 3, 5, 7],
       [2, 4, 6, 8]])

In [11]: np.array([[1, 3, 5, 7], [2, 4, 6]])
# Out[11]: array([list([1, 3, 5, 7]), list([2, 4, 6])], dtype=object)
In [12]: arr1 = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
In [14]: arr1.ndim
# Out[14]: 2
In [15]: arr1.shape
# Out[15]: (2, 4)
In [16]: arr1.dtype
# Out[16]: dtype('int64')
In [17]: arr2 = np.array([[1.0, 3, 5, 7], [2, 4.0, 6, 8]])
In [18]: arr2.dtype
# Out[18]: dtype('float64')
In [19]: np.ones(5)
# Out[19]: array([1., 1., 1., 1., 1.])

In [20]: np.empty((2, 5))
# Out[20]:
array([[6.94152610e-310, 4.66070032e-310, 4.66070031e-310,
        6.94152610e-310, 7.35167805e+223],
       [5.40761401e-067, 1.39835953e-076, 7.01413727e-009,
        2.17150970e+214, 6.45967520e+270]])

In [21]: np.zeros((2,3,4))
# Out[21]:
array([[[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]],

       [[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]]])
Signature: np.ones(shape, dtype=None, order='C')
Docstring:
Return a new array of given shape and type, filled with ones.

Parameters
----------
shape : int or sequence of ints
    Shape of the new array, e.g., ``(2, 3)`` or ``2``.
dtype : data-type, optional
    The desired data-type for the array, e.g., `numpy.int8`.  Default is
    `numpy.float64`.
order : {'C', 'F'}, optional, default: C
    Whether to store multi-dimensional data in row-major
    (C-style) or column-major (Fortran-style) order in
    memory.

Returns
-------
out : ndarray
    Array of ones with the given shape, dtype, and order.

See Also
--------
ones_like : Return an array of ones with shape and type of input.
empty : Return a new uninitialized array.
zeros : Return a new array setting values to zero.
full : Return a new array of given shape filled with value.
In [24]: num_string = np.array(['1.0', '2', '3.45'], dtype = np.string_)

In [25]: num_string
# Out[25]: array([b'1.0', b'2', b'3.45'], dtype='|S4')
In [26]: num_string.astype(float)
# Out[26]: array([1.  , 2.  , 3.45])
In [28]: num_string.astype(float).astype(np.int32)
# Out[28]: array([1, 2, 3], dtype=int32)
In [29]: num_string.astype(float).astype(np.int64)
# Out[29]: array([1, 2, 3])
In [30]: arr = np.array([[2, 3., 4.], [4, 5.4, 6]])
In [31]: arr
# Out[31]:
array([[2. , 3. , 4. ],
       [4. , 5.4, 6. ]])

In [32]: arr * arr
# Out[32]:
array([[ 4.  ,  9.  , 16.  ],
       [16.  , 29.16, 36.  ]])

In [33]: arr ** 2
# Out[33]:
array([[ 4.  ,  9.  , 16.  ],
       [16.  , 29.16, 36.  ]])

In [34]: arr - arr
# Out[34]:
array([[0., 0., 0.],
       [0., 0., 0.]])

In [35]: arr / arr
# Out[35]:
array([[1., 1., 1.],
       [1., 1., 1.]])

In [36]: arr + arr
# Out[36]:
array([[ 4. ,  6. ,  8. ],
       [ 8. , 10.8, 12. ]])
In [37]: 1 + np.array([2, 3, 4])
# Out[37]: array([3, 4, 5])

In [38]: 1 - np.array([2, 3, 4])
# Out[38]: array([-1, -2, -3])
In [39]: np.array([1, 1, 1]) + np.array([2, 3, 4])
# Out[39]: array([3, 4, 5])
In [40]: np.array([1, 1]) + np.array([2, 3, 4])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-40-1fbcd8e2dd89> in <module>()
----> 1 np.array([1, 1]) + np.array([2, 3, 4])

ValueError: operands could not be broadcast together with shapes (2,) (3,)
In [43]: np.array([5, 1, 7, 2]) > np.array([2, 3, 4, 5])
# Out[43]: array([ True, False,  True, False])
In [7]: x = np.arange(-5, 2, 0.01)
In [8]: y = np.arange(-20, -10, 0.2)
In [9]: xspace, yspace = np.meshgrid(x, y)

In [10]: xspace
# Out[10]:
array([[-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99],
       [-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99],
       [-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99],
       ...,
       [-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99],
       [-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99],
       [-5.  , -4.99, -4.98, ...,  1.97,  1.98,  1.99]])
In [11]: yspace
# Out[11]:
array([[-20. , -20. , -20. , ..., -20. , -20. , -20. ],
       [-19.8, -19.8, -19.8, ..., -19.8, -19.8, -19.8],
       [-19.6, -19.6, -19.6, ..., -19.6, -19.6, -19.6],
       ...,
       [-10.6, -10.6, -10.6, ..., -10.6, -10.6, -10.6],
       [-10.4, -10.4, -10.4, ..., -10.4, -10.4, -10.4],
       [-10.2, -10.2, -10.2, ..., -10.2, -10.2, -10.2]])

In [12]: xspace + yspace ** 2
# Out[12]:
array([[395.  , 395.01, 395.02, ..., 401.97, 401.98, 401.99],
       [387.04, 387.05, 387.06, ..., 394.01, 394.02, 394.03],
       [379.16, 379.17, 379.18, ..., 386.13, 386.14, 386.15],
       ...,
       [107.36, 107.37, 107.38, ..., 114.33, 114.34, 114.35],
       [103.16, 103.17, 103.18, ..., 110.13, 110.14, 110.15],
       [ 99.04,  99.05,  99.06, ..., 106.01, 106.02, 106.03]])
In [13]: x = np.arange(-5, -2, 1)
In [16]: y = np.arange(-20, -15, 1)
In [17]: xspace, yspace = np.meshgrid(x, y)

In [18]: x
# Out[18]: array([-5, -4, -3])
In [19]: y
# Out[19]: array([-20, -19, -18, -17, -16])

In [20]: xspace
# Out[20]:
array([[-5, -4, -3],
       [-5, -4, -3],
       [-5, -4, -3],
       [-5, -4, -3],
       [-5, -4, -3]])
In [21]: yspace
# Out[21]:
array([[-20, -20, -20],
       [-19, -19, -19],
       [-18, -18, -18],
       [-17, -17, -17],
       [-16, -16, -16]])
In [44]: arr = np.arange(20)
In [45]: arr
# Out[45]:
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])

In [46]: arr[5]          # 单个值索引, 提取第 6 个元素
# Out[46]: 5
In [47]: arr[2:5]        # 范围索引，取第 3 个到第 5 个元素
# Out[47]: array([2, 3, 4])
In [48]: arr[2:5] = 10   # 将第 3 到第 5 到元素重新赋值为 10
In [49]: arr
# Out[49]:
array([ 0,  1, 10, 10, 10,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])

In [50]: arr[10:13] = [111, 222, 333]  # 将第 11、12、13 个元素分别赋值为 111、222、333
In [51]: arr
# Out[51]:
array([  0,   1,  10,  10,  10,   5,   6,   7,   8,   9, 111, 222, 333,
        13,  14,  15,  16,  17,  18,  19])
In [52]: ls = [i for i in range(10)]
In [53]: ls
# Out[53]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [54]: arr = np.arange(10)
In [55]: arr
# Out[55]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [56]: ls2 = ls[4:8]
In [57]: ls2
# Out[57]: [4, 5, 6, 7]

In [60]: arr2 = arr[4:8]
In [61]: arr2
# Out[61]: array([4, 5, 6, 7])
In [67]: ls2[0] = 100  # 修改列表第 1 个元素值为 100
In [68]: ls2
# Out[68]: [100, 5, 6, 7]
In [69]: ls
# Out[69]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [70]: arr2[0] = 100 # 修改 ndarray 第 1 个元素值为 100
In [71]: arr2
# Out[71]: array([100,   5,   6,   7])
In [72]: arr
# Out[72]: array([  0,   1,   2,   3, 100,   5,   6,   7,   8,   9])
In [1]: import numpy as np
In [2]: arr2d = np.array([[1, 2, 3], [4, 5, 6]])  # 初始化一个二维数组，即矩阵

In [3]: arr2d[0]      # 提取矩阵的第 1 行
# Out[3]: array([1, 2, 3])

In [4]: arr2d[:,0]    # 提取矩阵的第 1 列
# Out[4]: array([1, 4])

In [5]: arr2d[0, 0]   # 提取矩阵位于第 1 行第 1 列的元素
# Out[5]: 1

In [6]: arr2d[0:2, 0] # 提取矩阵第 1 列前两个元素
# Out[6]: array([1, 4])

In [7]: arr2d[0:2]    # 提取矩阵的前两行，这跟 arr2d[0:2, :] 结果是一致的
# Out[7]:
array([[1, 2, 3],
       [4, 5, 6]])

In [8]: arr2d[:2, 1:] = 0  # 矩阵前两行的第 2 列开始往右元素值全为 0

In [9]: arr2d
# Out[9]:
array([[1, 0, 0],
       [4, 0, 0]])

In [10]: arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])  # 创建一个简单的 3 维数组

In [11]: arr3d
# Out[11]:
array([[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]])

In [12]: arr3d[0]  # 这是沿着第 0 轴（第一个轴）切片的结果，注意与 arr3d 的区别，这里是一个 3x3 数组（矩阵）
# Out[12]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [13]: new_array = arr3d[0].copy()  # 创建矩阵新的拷贝

In [14]: new_array
# Out[14]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [15]: arr3d[0] = 42  # 对原始 3 维数组第 1 个子维度重新赋值

In [16]: arr3d          # 此处 42 进行了广播，矩阵全部元素都为 42
# Out[16]:
array([[[42, 42, 42],
        [42, 42, 42],
        [42, 42, 42]]])

In [17]: arr3d[0] = new_array  # 将存储在 new_array 的原始值重新赋值回去

In [18]: arr3d
# Out[18]:
array([[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]])
In [19]: arr3d > 5
# Out[19]:
array([[[False, False, False],
        [False, False,  True],
        [ True,  True,  True]]])
In [20]: subject = np.array(['chinese', 'math', 'chinese', 'english', 'history'])
In [21]: df = np.random.randn(5, 3)
In [22]: df
# Out[22]:
array([[ 0.50025766, -0.4625053 , -1.85743193],
       [ 0.63757593,  0.55624546, -1.7669166 ],
       [-0.18061614, -0.71896639, -0.26744936],
       [ 1.37094842, -0.21829646, -0.34926808],
       [-0.90192432, -0.2821726 ,  0.54411861]])
In [23]: subject == 'chinese'
# Out[23]: array([ True, False,  True, False, False])
In [24]: df[subject == 'chinese']
# Out[24]:
array([[ 0.50025766, -0.4625053 , -1.85743193],
       [-0.18061614, -0.71896639, -0.26744936]])
In [25]: df[subject == 'chinese', 1:] # 满足 chinese 对应行，去除第 1 列
# Out[25]:
array([[-0.4625053 , -1.85743193],
       [-0.71896639, -0.26744936]])

In [26]: df[subject == 'chinese', 2:] # 满足 chinese 对应行，去除第 1、2 列
# Out[26]:
array([[-1.85743193],
       [-0.26744936]])

In [27]: df[subject != 'chinese', 2:] # 不满足 chinese 对应行，去除第 1、2 列
# Out[27]:
array([[-1.7669166 ],
       [-0.34926808],
       [ 0.54411861]])
In [29]: df[~ (subject == 'chinese'), 2:] # 该代码行与上一个代码行结果一致
# Out[29]:
array([[-1.7669166 ],
       [-0.34926808],
       [ 0.54411861]])
In [31]: df[subject == "chinese" | subject == "math"]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-ec9c993564c8> in <module>()
----> 1 df[subject == "chinese" | subject == "math"]
In [33]: df[(subject == "chinese") | (subject == "math")]
# Out[33]:
array([[ 0.50025766, -0.4625053 , -1.85743193],
       [ 0.63757593,  0.55624546, -1.7669166 ],
       [-0.18061614, -0.71896639, -0.26744936]])
In [34]: df[df < 0] = 0
In [35]: df
# Out[35]:
array([[0.50025766, 0.        , 0.        ],
       [0.63757593, 0.55624546, 0.        ],
       [0.        , 0.        , 0.        ],
       [1.37094842, 0.        , 0.        ],
       [0.        , 0.        , 0.54411861]])
In [22]: arr_random = np.random.randn(4, 4)
In [23]: arr_random
# Out[23]:
array([[-1.48064102,  1.4408966 , -0.13313057,  1.09683071],
       [ 0.44698237,  0.01854261,  0.56719151, -1.03926198],
       [ 1.45070221,  0.04421898,  0.787423  , -1.28715644],
       [ 2.27759091, -0.06808282, -0.99294482, -0.39755302]])
In [24]: arr_random > 0
# Out[24]:
array([[False,  True, False,  True],
       [ True,  True,  True, False],
       [ True,  True,  True, False],
       [ True, False, False, False]])

In [25]: np.where(arr_random > 0, 1, 0)
# Out[25]:
array([[0, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 0],
       [1, 0, 0, 0]])
In [2]: import numpy as np
In [3]: arr = np.arange(12).reshape((3, 4))
In [4]: arr
# Out[4]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [5]: arr.T
# Out[5]:
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])

In [6]: arr.transpose()
# Out[6]:
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
In [10]: arr.shape
# Out[10]: (3, 4)
In [11]: np.dot(arr, arr.T)
# Out[11]:
array([[ 14,  38,  62],
       [ 38, 126, 214],
       [ 62, 214, 366]])
In [12]: arr = np.arange(24).reshape((2,3,4))
In [13]: arr
# Out[13]:
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])

In [14]: arr.transpose((1,0,2)) # 0表示第1轴、1表示第2轴、2表示第3轴
# Out[14]:
array([[[ 0,  1,  2,  3],
        [12, 13, 14, 15]],

       [[ 4,  5,  6,  7],
        [16, 17, 18, 19]],

       [[ 8,  9, 10, 11],
        [20, 21, 22, 23]]])
In [15]: arr.swapaxes(1, 2)
# Out[15]:
array([[[ 0,  4,  8],
        [ 1,  5,  9],
        [ 2,  6, 10],
        [ 3,  7, 11]],

       [[12, 16, 20],
        [13, 17, 21],
        [14, 18, 22],
        [15, 19, 23]]])

In [16]: arr.swapaxes(0, 1)
# Out[16]:
array([[[ 0,  1,  2,  3],
        [12, 13, 14, 15]],

       [[ 4,  5,  6,  7],
        [16, 17, 18, 19]],

       [[ 8,  9, 10, 11],
        [20, 21, 22, 23]]])
In [17]: arr = np.arange(10).reshape((2, 5))
In [18]: arr
# Out[18]:
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])

In [19]: np.sqrt(arr)
# Out[19]:
array([[0.        , 1.        , 1.41421356, 1.73205081, 2.        ],
       [2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ]])
In [20]: np.exp(arr)
# Out[20]:
array([[1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
        5.45981500e+01],
       [1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03,
        8.10308393e+03]])
In [21]: arr2 = np.random.randn(10).reshape((2,5))
In [22]: arr2
# Out[22]:
array([[-0.81547072,  0.02248639, -0.3004805 ,  1.53433534,  0.59514916],
       [ 1.60022692, -0.68780704,  0.79007821,  0.72034177, -1.33966745]])

In [23]: np.add(arr, arr2)      # 对应元素相加
# Out[23]:
array([[-0.81547072,  1.02248639,  1.6995195 ,  4.53433534,  4.59514916],
       [ 6.60022692,  5.31219296,  7.79007821,  8.72034177,  7.66033255]])
In [24]: np.maximum(arr, arr2)  # 返回对应元素较大的那个
# Out[24]:
array([[0., 1., 2., 3., 4.],
       [5., 6., 7., 8., 9.]])
In [25]: part1, part2 = np.modf(arr2)
In [26]: part1
# Out[26]:
array([[-0.81547072,  0.02248639, -0.3004805 ,  0.53433534,  0.59514916],
       [ 0.60022692, -0.68780704,  0.79007821,  0.72034177, -0.33966745]])
In [27]: part2
# Out[27]:
array([[-0.,  0., -0.,  1.,  0.],
       [ 1., -0.,  0.,  0., -1.]])
In [2]: import numpy as np
In [3]: arr = np.random.randn(5, 5)
In [4]: arr
# Out[4]:
array([[-0.51132191, -0.88525544, -1.10119999, -2.3272623 ,  0.24502215],
       [ 0.22767771, -0.43164608,  0.62262033, -1.68672377, -0.19473212],
       [-0.65820486, -1.62823718,  0.0798516 ,  0.1056899 , -0.45333499],
       [ 0.86035323,  1.79121647,  0.75648603,  0.56113024, -1.57487612],
       [ 0.90551266, -2.35820418,  0.34951423, -1.23775123, -0.62627856]])

In [5]: arr.mean()  # 求均值
# Out[5]: -0.36679816721832453
In [6]: arr.sum()   # 求和
# Out[6]: -9.169954180458113
In [7]: arr.var()   # 求方差
# Out[7]: 1.0772072348109176
In [8]: arr.std()   # 求标准差
# Out[8]: 1.037885944991509
In [9]: arr.mean(axis=0)   # 计算列的平均值
# Out[9]: array([ 0.16480337, -0.70242528,  0.14145444, -0.91698343, -0.52083993])
In [10]: arr.mean(axis=1)  # 计算行的平均值
# Out[10]: array([-0.9160035 , -0.29256078, -0.51084711,  0.47886197, -0.59344142])
In [11]: arr = np.arange(10)
In [12]: arr
# Out[12]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [13]: arr.cumsum()
# Out[13]: array([ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45])
In [2]: arr = np.random.randn(10)
In [3]: arr
# Out[3]:
array([-1.03434834, -0.1066477 , -0.18138105, -0.02874672,  0.37446326,
       -0.19669119,  0.00594903,  0.19048595,  0.14961745,  0.5749973 ])

In [4]: arr.sort()
In [5]: arr
# Out[5]:
array([-1.03434834, -0.19669119, -0.18138105, -0.1066477 , -0.02874672,
        0.00594903,  0.14961745,  0.19048595,  0.37446326,  0.5749973 ])
In [8]: arr = np.random.randn(3, 4)
In [9]: arr
# Out[9]:
array([[-1.36520054, -1.61647551, -1.19945064,  1.37181547],
       [-0.10126557, -0.39124394, -0.34307793, -0.8307224 ],
       [ 0.76972754,  1.10906676, -0.17070844,  0.06256465]])

In [10]: arr.sort(1) # 每行按升序排列
In [11]: arr
# Out[11]:
array([[-1.61647551, -1.36520054, -1.19945064,  1.37181547],
       [-0.8307224 , -0.39124394, -0.34307793, -0.10126557],
       [-0.17070844,  0.06256465,  0.76972754,  1.10906676]])
In [14]: arr_int = np.array([3, 4, 5, 8, 4, 3, 2, 1, 6, 10])
In [15]: arr_int
# Out[15]: array([ 3,  4,  5,  8,  4,  3,  2,  1,  6, 10])

In [16]: np.unique(arr_int)
# Out[16]: array([ 1,  2,  3,  4,  5,  6,  8, 10])
In [17]: sorted(set(arr_int))
# Out[17]: [1, 2, 3, 4, 5, 6, 8, 10]
In [18]: arr_int2 = np.array([1, 3, 22, 5, 6])  # 另外新建一个一维数组

In [19]: np.intersect1d(arr_int, arr_int2)  # 交集
# Out[19]: array([1, 3, 5, 6])
In [20]: np.union1d(arr_int, arr_int2)      # 并集
# Out[20]: array([ 1,  2,  3,  4,  5,  6,  8, 10, 22])
In [21]: np.setdiff1d(arr_int, arr_int2)    # 差集
# Out[21]: array([ 2,  4,  8, 10])

In [22]: x = np.array([[1, 2, 3], [4, 5, 6]])
In [23]: y = np.array([[3, 5, 6], [7, 8, 9]])
In [24]: x * y
# Out[24]:
array([[ 3, 10, 18],
       [28, 40, 54]])
In [25]: np.dot(x, y)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-25-c3a58f1d73f8> in <module>()
----> 1 np.dot(x, y)

ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
In [27]: np.dot(x, y)
# Out[27]:
array([[ 39,  46],
       [ 90, 109]])
In [28]: x.dot(y)
# Out[28]:
array([[ 39,  46],
       [ 90, 109]])

In [29]: x @ y
# Out[29]:
array([[ 39,  46],
       [ 90, 109]])
In [30]: np.random.normal(size=(5,5))
# Out[30]:
array([[ 0.03488939, -1.58459629, -1.46781029, -1.13217542, -1.06312407],
       [ 0.83678804,  1.21880709, -0.90811673, -1.71748912,  0.92877163],
       [-0.49898785, -0.17523296, -1.73258953, -0.47749123, -1.49576169],
       [ 0.15254935,  0.46308905,  0.1221845 , -2.15762674,  2.23510318],
       [-0.70557981,  0.96598878,  0.43192638, -0.2049251 ,  0.23281444]])
In [31]: np.random.randn(10)
# Out[31]:
array([-0.559106  ,  1.36880898, -0.24559224, -0.16668403,  2.42001793,
        0.39617551, -1.06446839,  1.02696512,  0.08217648,  1.07538155])
In [36]: np.random.randn(5,5)
# Out[36]:
array([[-0.77315232,  0.4786622 , -1.38927237, -0.20433972, -2.43830605],
       [ 0.34922348,  0.87849643,  1.5239394 , -0.73135812,  2.21068918],
       [ 0.12944191,  1.01207972, -0.57685143,  2.63207061, -0.74326986],
       [ 0.73286193,  0.42616076, -0.42334269, -0.98384705, -0.02632024],
       [-0.6184617 ,  0.40202667, -0.3722806 ,  0.16819083,  0.55132166]])
In [37]: np.random.seed(1234)
In [37]: r = np.random.RandomState(123456)
In [38]: r.randn(10)
# Out[38]:
array([ 0.4691123 , -0.28286334, -1.5090585 , -1.13563237,  1.21211203,
       -0.17321465,  0.11920871, -1.04423597, -0.86184896, -2.10456922])
In [2]: arr1 = np.random.randn(10)  # 创建一些数组
In [3]: arr2 = np.random.randn(10)
In [4]: arr_res =  arr1 + arr2      # 操作数组
In [5]: np.save('result', arr_res)  # 保存结果数组
In [6]: np.load('result.npy')
# Out[6]:
array([-1.62141731,  0.22330449,  0.52851935, -0.34489954,  0.00938235,
        3.27527395, -0.83738875,  0.45741888, -0.12050226, -0.90452199])
In [7]: np.load('result')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-7-f17638fbbc1f> in <module>()
----> 1 np.load('result')

~/anaconda3/lib/python3.7/site-packages/numpy/lib/npyio.py in load(file, mmap_mode, allow_pickle, fix_imports, encoding)
    382     own_fid = False
    383     if isinstance(file, basestring):
--> 384         fid = open(file, "rb")
    385         own_fid = True
    386     elif is_pathlib_path(file):

FileNotFoundError: [Errno 2] No such file or directory: 'result'
In [8]: np.savez('array_save.npz', input1=arr1, input2=arr2, result=arr_res)
In [9]: np.load('array_save.npz')
# Out[9]: <numpy.lib.npyio.NpzFile at 0x7f917c6caba8>
In [10]: arr_save =  np.load('array_save.npz')
In [11]: arr_save['input1']
# Out[11]:
array([-0.79417709,  0.57095314,  1.59839779, -0.96875458, -1.35098779,
        2.5673315 ,  0.64841217,  0.28681969,  0.26718872,  0.26876572])
In [12]: arr_save['input2']
# Out[12]:
array([-0.82724022, -0.34764864, -1.06987844,  0.62385504,  1.36037014,
        0.70794245, -1.48580092,  0.17059919, -0.38769099, -1.17328771])
In [13]: arr_save['result']
# Out[13]:
array([-1.62141731,  0.22330449,  0.52851935, -0.34489954,  0.00938235,
        3.27527395, -0.83738875,  0.45741888, -0.12050226, -0.90452199])
