import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

c = np.array([6, 8, 9, 2], dtype= 'int32')

print(a)
print(b)

print(a.ndim)  # 维度

print(b.shape) # （行, 列）

print(a.dtype) # 数据类型   int64：一个数据占 64 个 bit 位（8个字节）
print(c.dtype)

print(a.itemsize) # 一个数据占多少 字节
print(c.itemsize)

print(a.nbytes)  # 整个列表占多少字节 3 * 8

print(a.size)  # 列表元素个数

d = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
              [9, 10, 11, 12, 13, 14, 15, 16],
              [17, 18, 19, 20, 21, 22, 23, 24]])
# 访问元素
print(d[1, 3])
print(d[-1, -2])

# 获取整行\整列
print(d[1, :])
print(d[:, -1])

# start: end: stepsize    [start, end) 中走 stepsize 步 取一个元素
print(d[0, 1: 6: 2])

# 修改元素
print('修改元素')
print(d)
# d[2, 3] = -20

# d[0, :] = 1    # 修改整行
# d[0, :] = [8, 7, 6, 5, 4, 3, 2, 1]

# d[:, 1] = [1, 1, 0]   # 修改整列

d[1:3, 1:4] = 1        # [1, 3) 行 [1, 4) 列, 修改
d[1:3, 1:4] = [[1, 2, 3], [4, 5, 6]]

print(d)


# 想象为一栋楼
f = np.array([[[1, 2, 3],
               [4, 5, 6]],

              [[7, 8, 9],
               [10, 11, 12]]])

print(f)
print(f[1, 0, 1])  # 从外向内 [层，行，列]
print(f[:, 0, :])
print(f[:, :, 1])

# 初始化
a = np.zeros((2, 3, 3))
b = np.zeros((2, 3, 3), 'int32')
print(a)
print(b)

a = np.ones((2, 3), dtype= 'int32')
print(a)

a = np.full((3, 3, 3), 99)
print(a)

a = np.full(b.shape, 66)
print(a)

# 随机矩阵
a = np.random.rand(3, 4, 5)   # （0, 1） 中的小数.
a = np.random.randint(0, 8, (3, 3, 3))  # [0, 8) 随机整数
print(a)

# 单位矩阵
a = np.identity(5, 'int32')
print(a)

# 重复
a = np.array([1, 2, 3])
rp = np.repeat(a, 3)    # 每个元素重复 3 次
rp = np.repeat(a, [2, 3, 6])   # 每个元素依次重复 2、3、6 次

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])
rp = np.repeat(a, 2)    # 一维数组
rp = np.repeat(a, 2, axis=1)  # axis=0/1, 每行/列重复
rp = np.repeat(a, [2, 1, 4, 2], axis=0)
rp = np.repeat(a, [3, 2, 4], axis=1)

a = np.array([
             [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10, 11, 12]],


             [[13, 14, 15],
              [16, 17, 18],
              [19, 20, 21],
              [22, 23, 24]],

             [[25, 26, 27],
              [28, 29, 30],
              [31, 32, 33],
              [34, 35, 36]]
              ])

rp = np.repeat(a, [1, 1, 2, 2], axis=1)  # axis=0/1/2 重复 层/行/列

print(rp)

#案例
output = np.ones((5, 5), 'int32')
zeros = np.zeros((3, 3), 'int32')
zeros[1, 1] = 9
output[1:-1, 1:-1] = zeros

print(output)
