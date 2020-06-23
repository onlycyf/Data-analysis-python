import pandas as pd
import numpy as np

a = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list('wxyz'))
# print(a)

d1 = {'name': ["xiaoming", 'xiaozhang'], 'age': [20, 32], 'tel': [10086, 10001]}
b1 = pd.DataFrame(d1)
# print(b1)

d2 = [{'name': 'xiaoming', 'age': 12, 'tel': 10086},
      {'name': 'xiaogang', 'age': 20, 'tel': 10001},
      {'name': 'xiaoxiao'}]
b2 = pd.DataFrame(d2)
# print(b2)

"""
pandas取行和列的方法
- []中写数组，表示取行，对行进行操作
- []写字符串,表示取列，对列进行操作
"""
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
print(t3)

print(t3.loc["a", 'w'])
print(t3.iloc[1:, 2:])

