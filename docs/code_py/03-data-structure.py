vowels = ['a', 'e', 'i', 'o', 'u']
vowels
# Out[2]: ['a', 'e', 'i', 'o', 'u']
array_init = []
array_init
# Out[4]: []
vowels[2]
# Out[5]: 'i'
rectangle = ['长方形1', 20, [4, 5], '长方形2', 16, [4, 4]]
rectangle
# Out[8]: ['长方形1', 20, [4, 5], '长方形2', 16, [4, 4]]
len(rectangle)
# Out[9]: 6
rectangle[6]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-10-6e16763c0048> in <module>()
# ----> 1 rectangle[6]

# IndexError: list index out of range
aseq = "atggctaggc"
list(aseq)
# Out[18]: ['a', 't', 'g', 'g', 'c', 't', 'a', 'g', 'g', 'c']
odd_numbers = [1, 3, 5, 7, 8]
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers = [1, 3, 5, 7, 8]
odd_numbers[4] = 9
odd_numbers
# Out[15]: [1, 3, 5, 7, 9]
odd_numbers[-1]
# Out[16]: 9
print(odd_numbers[0])
print(odd_numbers[1])
print(odd_numbers[2])
print(odd_numbers[3])
print(odd_numbers[4])
for i in odd_numbers:
  print(i)

# 1
# 3
# 5
# 7
# 9
nested_list = ['记录', 3, ['小明', '小红', '小蓝'], [2.30, 2.41, 2.33]]
for i in nested_list:
  print(i)
# 记录
# 3
# ['小明', '小红', '小蓝']
# [2.3, 2.41, 2.33]
a * 5
# Out[33]: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
letters7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
you_want = letters7[0:4]
you_want
# Out[38]: ['a', 'b', 'c', 'd']
letters7[0:4:1]
# Out[39]: ['a', 'b', 'c', 'd']
letters7[:4]
# Out[40]: ['a', 'b', 'c', 'd']
letters7[:7]
# Out[41]: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters7[4:]
# Out[42]: ['e', 'f', 'g']
letters7[-1]
# Out[43]: 'g'
letters7[-1:]
# Out[44]: ['g']
letters7[::1]
# Out[45]: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters7[::2]
# Out[46]: ['a', 'c', 'e', 'g']
letters7[::-1]
# Out[47]: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
letters7[::-2]
# Out[48]: ['g', 'e', 'c', 'a']
letters7[0:2] = ['h', 'i']
letters7
# Out[50]: ['h', 'i', 'c', 'd', 'e', 'f', 'g']
letters7[0:2] = ['a']
letters7
# Out[52]: ['a', 'c', 'd', 'e', 'f', 'g']
letters7[0:1] = ['a', 'b']
letters7
# Out[54]: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters7[0:2] = 'h'
letters7
# Out[56]: ['h', 'c', 'd', 'e', 'f', 'g']
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example_list.append(11)
example_list
# Out[61]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

example_list.insert(2, 12)
example_list
# Out[63]: [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
example_list.extend([13,14])
example_list
# Out[65]: [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
example_list.pop()
# Out[67]: 14
example_list.pop(2)
# Out[68]: 12
example_list.remove(13)
example_list
# Out[70]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
del example_list[10]
example_list
# Out[72]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example_list.clear()
example_list
# Out[74]: []
a = [3, 1, 2, 5, 4, 6]
a.sort()
a
# Out[80]: [1, 2, 3, 4, 5, 6]
nums = [-1, 34, 0.2, -4, 309]
nums_desc = sorted(nums, reverse=True)
nums
# Out[83]: [-1, 34, 0.2, -4, 309]
nums_desc
# Out[84]: [309, 34, 0.2, -1, -4]
nums
# Out[90]: [1, 2, 2, 2, 3, 3, 4, 5]
nums.reverse()
nums
# Out[92]: [5, 4, 3, 3, 2, 2, 2, 1]
min(nums)
# Out[85]: -4
max(nums)
# Out[86]: 309
nums = [1, 2, 2, 2, 3, 3, 4, 5]
nums.count(2)
# Out[88]: 3
nums.count(3)
# Out[89]: 2
sum(nums)
# Out[93]: 22
4 in example_list
# Out[76]: False
3 in example_list
# Out[77]: True
conditions = [True, False, True]
all(conditions)
# Out[95]: False
any(conditions)
# Out[96]: True
a = [1, 2, 3, 4]

a == [1, 2, 3, 5]
# Out[98]: False
a == [1, 3, 2, 4]
# Out[99]: False
a == [1, 2, 3, 4]
# Out[100]: True
s = 'interactive Python'
t = list(s)
t
# Out[103]:
['i',
 'n',
 't',
 'e',
 'r',
 'a',
 'c',
 't',
 'i',
 'v',
 'e',
 ' ',
 'P',
 'y',
 't',
 'h',
 'o',
 'n']
s.split()
# Out[104]: ['interactive', 'Python']
s = 'interactive-Python'
s.split('-')
# Out[107]: ['interactive', 'Python']
t = ['我','是', '谁', '？']
''.join(t)
# Out[109]: '我是谁？'
a = 'banana'
b = 'banana'
a is b
# Out[6]: True
id(a)
# Out[10]: 1691582590008
id(b)
# Out[11]: 1691582590008
a = "orange"
b
# Out[13]: 'banana'
a = [1, 2, 3]
b = [1, 2, 3]

a is b
# Out[16]: False

id(a)
# Out[17]: 1691581888264
id(b)
# Out[18]: 1691582794120
b = a

a is b
# Out[20]: True

id(b)
# Out[21]: 1691581888264
e = a

e
# Out[23]: [1, 2, 3]
a
# Out[24]: [1, 2, 3]

a[1] = 4
e
# Out[26]: [1, 4, 3]
a_tuple = (1, 2, 3)
a_list = [1, 2, 3]
another_tuple = 1,2,3
type(another_tuple)
# Out[7]: tuple
1
# Out[8]: 1

(1)
# Out[9]: 1

1,
# Out[10]: (1,)

(1,)
# Out[11]: (1,)
tuple("Python")
# Out[14]: ('P', 'y', 't', 'h', 'o', 'n')
tuple(["I", "am", ["learning", "Python"]])
# Out[15]: ('I', 'am', ['learning', 'Python'])
('a',) + ('b',)
# Out[16]: ('a', 'b')

('a',) * 3
# Out[17]: ('a', 'a', 'a')
pythonName = tuple("Python")
pythonName
# Out[19]: ('P', 'y', 't', 'h', 'o', 'n')

pythonName[0]
# Out[20]: 'P'
pythonName[0:3]
# Out[21]: ('P', 'y', 't')
pythonName[3:]
# Out[22]: ('h', 'o', 'n')
pythonName[0] = 'p'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-23-19ded1757eee> in <module>()
# ----> 1 pythonName[0] = 'p'

# TypeError: 'tuple' object does not support item assignment
newName = ('p',) + pythonName[1:]
newName
# Out[25]: ('p', 'y', 't', 'h', 'o', 'n')
weight = {'小红':65, '小明':45, '我':75}
weight
# Out[6]: {'小明': 45, '小红': 65, '我': 75}
weight['小明']
# Out[7]: 45
weight.keys()
# Out[8]: dict_keys(['小红', '小明', '我'])
weight.values()
# Out[9]: dict_values([65, 45, 75])
int_dict = {}
int_dict
# Out[11]: {}
rgb = [('red', 'ff0000'), ('green', '00ff00'), ('blue', '0000ff')]

dict(rgb)
# Out[14]: {'blue': '0000ff', 'green': '00ff00', 'red': 'ff0000'}
dict(red='ff0000',green='00ff00', blue='0000ff')
# Out[15]: {'blue': '0000ff', 'green': '00ff00', 'red': 'ff0000'}
rgb = {}

rgb['red'] = 'ff0000'
rgb['green'] = '00ff00'
rgb['blue'] = '0000ff'

rgb
# Out[20]: {'blue': '0000ff', 'green': '00ff00', 'red': 'ff0000'}
len(rgb)
# Out[21]: 3
rgb.pop()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-22-1654217e28c5> in <module>()
# ----> 1 rgb.pop()

# TypeError: pop expected at least 1 arguments, got 0

rgb.pop('blue')
# Out[23]: '0000ff'
rgb
# Out[24]: {'green': '00ff00', 'red': 'ff0000'}
del rgb
rgb
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-26-d412e57c3c38> in <module>()
# ----> 1 rgb

# NameError: name 'rgb' is not defined
rgb.get('red', '键不存在')
# Out[28]: 'ff0000'
rgb.get('yellow', '键不存在')
# Out[29]: '键不存在'
from collections import OrderedDict

OrderedDict(rgb)
# Out[33]: OrderedDict([('red', 'ff0000'), ('green', '00ff00'), ('blue', '0000ff')])

order_dict = OrderedDict()
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
order_dict
# Out[39]: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
a_set = {1, 2, 3, 4, 5, 5, 4}
a_set
# Out[41]: {1, 2, 3, 4, 5}
a_set = {}
a_set.add(1)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-43-2a4eeb394ac5> in <module>()
# ----> 1 a_set.add(1)

# AttributeError: 'dict' object has no attribute 'add'
a_set = set()
a_set.add(1)
a_set
# Out[46]: {1}
a_set = set([1, 2, 3, 4, 5])
b_set = set([4, 5, 6, 7, 8])
a_set
# Out[49]: {1, 2, 3, 4, 5}
b_set
# Out[50]: {4, 5, 6, 7, 8}

a_set.union(b_set)
# Out[51]: {1, 2, 3, 4, 5, 6, 7, 8}
a_set.intersection(b_set)
# Out[52]: {4, 5}
a_set.difference(b_set)
# Out[53]: {1, 2, 3}
fs = frozenset(['a', 'b'])
fs
# Out[2]: frozenset({'a', 'b'})

fs.remove('a')
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-3-b55f44b7e2c9> in <module>()
# ----> 1 fs.remove('a')

# AttributeError: 'frozenset' object has no attribute 'remove'

fs.add('c')
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-4-34531eab3bc0> in <module>()
# ----> 1 fs.add('c')

# AttributeError: 'frozenset' object has no attribute 'add'
