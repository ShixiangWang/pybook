print('你好啊，世界！)
# print('你好啊，世界')! # 错误写法
3 + 2             # 加法
3 / 2             # 浮点数除法
3 // 2            # 整除
3 * 2             # 乘法
3 ** 2            # 指数（幂）
3 % 2             # 求余
abs(a)            # 绝对值
1 + 1
# Out[3]: 2

1 - 1
# Out[4]: 0

1 * 1
# Out[5]: 1

1 / 1
# Out[6]: 1.0
70 / 1.82 ** 2
# Out[11]: 21.132713440405748
70 / 1.82 ** 2  # 计算我的 BMI
# Out[12]: 21.132713440405748
# 计算我的 BMI
70 / 1.82 ** 2
# Out[14]: 21.132713440405748
# 计算我的 BMI  70 / 1.82 ** 2
计算我的 BMI 指数 70 / 1.82 ** 2
#   File "<ipython-input-16-b7d966d13e1f>", line 1
#     计算我的 BMI 指数 70 / 1.82 ** 2
#                  ^
# SyntaxError: invalid syntax
# 与朋友比较 BMI 指数
70 / 1.82 ** 2
# Out[10]: 21.132713440405748

 48 / 1.64 ** 2
# Out[11]: 17.846519928613922

70 / 1.82 ** 2 - 48 / 1.64 ** 2
# Out[12]: 3.2861935117918257
height = 1.82

weight = 70
print(height)
# Out[15]: 1.82

print(weight)
# Out[16]: 70

height
# Out[17]: 1.82

weight
# Out[18]: 70
myBMI = 70 / 1.82 ** 2      # 我的 BMI
friendBMI = 48 / 1.64 ** 2  # 朋友的 BMI
myBMI - friendBMI           # 我与朋友的 BMI 值的差异
# Out[21]: 3.2861935117918257
__myName = "ShixiangWang"

my-name = "ShixiangWang"  # 错误的表示方法
'What's your name?'  # 错误的表示方法
#   File "<ipython-input-26-dff8324f3597>", line 1
#     'What's your name?'  # 错误的表示方法
#           ^
# SyntaxError: invalid syntax

'What\'s your name?'  # 使用转义\对字符串中的英文单引号进行转义
# Out[27]: "What's your name?"
"What\'s your name?"  # 将英文单引号嵌入英文双引号中
# Out[28]: "What's your name?"
"This is the first sentence.\
This is the second sentence."
"Newlines are indicated by \n"
# Out[35]: 'Newlines are indicated by \n'

r"Newlines are indicated by \n"
# Out[36]: 'Newlines are indicated by \\n'

print(r"Newlines are indicated by \n")
# Out[37]: Newlines are indicated by \n

print("Newlines are indicated by \n")
# Out[38]: Newlines are indicated by
# 此处输出一个空行
type1 = 1
type2 = 1.0
type3 = "1"
type4 = True
type(type1)
# Out[49]: int
type(type2)
# Out[50]: float
type(type3)
# Out[51]: str
type(type4)
# Out[52]: bool
'1' + '1'
# Out[2]: '11'
'1' - '1'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-3f89fba82f3e> in <module>()
# ----> 1 '1' - '1'

# TypeError: unsupported operand type(s) for -: 'str' and 'str'
type('1')
# Out[8]: str

type(int('1'))
# Out[9]: int
"我的语文和数学成绩之和是 " + 199
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-17fa10d93550> in <module>()
# ----> 1 "我的语文和数学成绩之和是 " + 199

# TypeError: must be str, not int

"我的语文和数学成绩之和是 " + str(199)
# Out[11]: '我的语文和数学成绩之和是 199'
9 + 2 # 加
9 - 2 # 减
9 * 2 # 乘
9 / 2 # 除（浮点输出）
9 //2 # 整除
9 % 2 # 求余
9 **2 # 幂
'这是一个' + '字符串' # 字符串连接
'这是一个字符串' * 5  # 字符串重复
5 == 4  # 等于
5 > 4   # 大于
5 < 4   # 小于
5 != 4  # 不等于
5 >= 4  # 大于或等于
5 <= 4  # 小于或等于
True and True   # 逻辑“与”
True or False   # 逻辑“或”
not False       # 逻辑“非”
