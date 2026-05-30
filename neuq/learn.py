import sys
# sys.path.append('C:/Users/admin/Desktop/my_models/')
import random           # 标准库
import datetime
import calendar
import os

import my_model as mm   # 第三方库，引入 my_model 中的所有元素

courses = ['Math', 'English', 'Art', 'CompSic']
random_course = random.choice(courses)
print(random_course)

print(mm.test)

index = mm.find_index(courses, 'Art')
print(index)

# from my_model import find_index, test
# courses = ['Math', 'English', 'Art', 'CompSic']
# index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)

print(datetime.datetime.now())
print(calendar.isleap(2026))
print(os.getcwd())
print(os.__file__)

# import 一个库，Python 根据 sys.path 中路径搜索这个库，sys.path 中包括当前目录、标准库、Pycharm 安装的插件...
# 如果 import 一个第三方库（不在本目录下）, 可以添加 sys.path;
# sys.path.append('C:/Users/admin/Desktop/my_models/') 或者 在 windows 的环境变量 中新建一条 PATHONPATH


