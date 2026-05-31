import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

c = np.array([6, 8, 9, 2], dtype= 'int32')

print(a)
print(b)

print(a.ndim)  # 维度

print(b.shape) # （层, 行, 列）

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
d[2, 3] = -20

d[0, :] = 1    # 修改整行
d[0, :] = [8, 7, 6, 5, 4, 3, 2, 1]

d[:, 1] = [1, 1, 0]   # 修改整列

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

a = np.ones((2, 3), 'int32')
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

# 复制
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.copy()
b[0] = 0

print(a)
print(b)

# 数学运算
print(a)
print(b)
print(a + 2)
print(a * 2)
print(a ** 2)
print(a + b)
print(a * b)   # 对应元素相乘, 要求 a、b 的形状相同

print(np.sin(a))

# 线性代数
a = np.full((2, 3), 2)
b = np.ones((3, 4), 'int32')
c = np.matmul(a, b)     # 矩阵乘法  要求 a 的列数 = b 的行数


print(a)
print(b)
print(c)

a = np.identity(3, 'int32')
b = np.linalg.det(a)    # 求 行列式
print(b)

# 统计学
a = np.array([[[4, 5, 6],
               [1, 2, 3],
               [7, 8, 9]],

               [[1, 2, 3],
                [4, 5, 6],
                [1, 1, 1]]])

print(np.min(a))
print(np.min(a, axis= 0))  # axis= 0/1/2 分别是 消除层/行/列   即竖直方向/列/行元素取最小值, 变为 1 层/行/列

print(np.sum(a))
print(np.sum(a, axis= 2))

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = a.reshape((6, 1))
print(b)

# 堆叠
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.vstack((v1, v2, v1))   # 竖向叠加
print(v3)

v1 = np.ones((2, 3), 'int32')
v2 = np.zeros((2, 2), 'int32')
v3 = np.hstack((v1, v2))       # 横向叠加
print(v3)

a = np.genfromtxt('word', delimiter= ',', dtype= 'int32')
print(a)

b = a > 1
print(b)

b = a[a > 1]
print(b)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[[0, 5, 8]]
print(b)