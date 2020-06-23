import numpy as np


# print(t1)
def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 当前一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # 选中当前为nan的位置，把值赋值为不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")

    t1[1, 2:] = np.nan

    t1 = fill_ndarray(t1)
    print(t1)