import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

a = pd.date_range(start='20171230', end='20180131', freq='D')
b = pd.date_range(start='20171230', end='20180131', freq='10D')
c = pd.date_range(start='20171230', periods=10, freq='M')
print(a)
print(b)
print(c)

d = pd.to_datetime('2017*9*30', format='%Y*%m*%d')
print(d)
