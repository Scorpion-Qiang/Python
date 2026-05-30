import numpy as np
# 基础语法
def fun():
    a = 1
    s = "秦皇岛"
    b = True
    n = None
    print(a)

    score = 85
    if score > 90:
        print("优秀")
    else:
        print("合格")

    while a > 0:
        print("山海关")
        a -= 1

    for i in range(9):
        print(i)

    fruits = ["apple", "banana", "cherry"]
    for f in fruits:
        print(f)

# 字符串
def fun2():
    name = "Scorpion"
    age = 24
    print(f"{name} is {age} years old")

    string = "Hello, Neuq"
    print(string[0:5])
    print(string[6:])
    print(string[::-1])

#数据结构
def fun3():
    list = ["I", 250, "东秦", True]
    print(list.append(804))
    list[0] = "Cui"
    print(list[0])
    print("东秦" in list)

    nums = [1, 2, 3, 4, 5, 6]
    squares = [n * n for n in nums]

    arr = [n for n in nums if n % 2 == 0]

    print("列表打印: ")
    for val in arr:
        print(val)

    dict = {"name" : "neu", 1 : 2, 0 : "nice"}
    print(dict["name"])
    print(map.get(6, "无"))
    dict["city"] = "Beijing"

    for k, v in map.items():
        print(f"{k}: {v}")

    set = {1, 2, 3}
    print(set)


# 函数
def great(name, cnt):
    return f"Hello, {name}"
def greet(city: str, location: str = "HeBei"):
    return f"Hello, {city} in {location}"

# 文件读写
def readandwrite():
    # with open("word", "w") as f:
    #     f.write("qust")

    with open("word", "r") as f:
        s = f.read()
        print(s)


def twoSum(self, nums, target):
    dict = {}
    ret = []
    n = len(nums)
    for i in range(n):
        val = nums[i]
        if dict.__contains__(target - val):
            ret.append(dict[target - val])
            ret.append(i)
        dict[val] = i
    return ret

#类
class Animal:
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def speak(self):
        return f"{self.id} is {self.type}"

# numpy

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
             [3, 4, 5]])

print(a.shape)
print(b.shape)

zeros = np.zeros((3, 4))
ones = np.ones((3, 4))

x = np.array([6, 7, 8])
y = np.array([9, 8, 7])

print(x + y)
print(x * y)
print(x ** 2)
print(x * 10)

print(np.mean(a))
print(a[0])
print(a[2 : 3])
print(a[a > 1])


# if __name__ == "__main__":
