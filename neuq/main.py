# 字符串
from numpy.ma.extras import average

message = 'Hello, world'

print("""Python是世界上最好的语言，
珠海是中国最好的城市，
计算机是世界上最好的学科！""")

print(message[0])
print(message[0 : 5])
print(message[:5])
print(len(message))

print(message.find('e'))
print(message.find('world'))
print(message.count('l'))
print(message.count('world'))
print(message.lower())
print(message.upper())

new_message = message.replace('world', 'universe')

greeting = 'welcome'
name = 'Jordon'
word = greeting + ', ' + name + ' to China'
new_word = '{}, {} to China'.format(greeting, name)
s_word = f'{greeting}, {name} to China'

print(word)
print(new_word)
print(s_word)

cnt = "100"
print(int(cnt))

num1 = 1
num2 = 6
print(num2 ** 2) # 幂运算
print(num2 / 4)
print(num2 // 4) # 向下取整
print(round(3.75, 1)) # 四舍五入

# 列表
courses = ['History', 'Math', 'Computer Science', 'Chinese']
new_courses = ['Art', 'English']

# 获取列表元素
print(courses[0])
print(courses[-1])

# 切片
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# 添加元素
courses.append('Chemistry')
courses.insert(1, 'Biology')

# courses.insert(1, new_courses)
courses.extend(new_courses)
print(courses)

# 删除
courses.remove('Math')
print(courses)

val = courses.pop()
print(val)
print(courses)

# 排序
courses.sort()       # 直接修改原列表
sort_courses = sorted(courses)         # 原列表不变，生成排序后的新列表
print(sort_courses)

nums = [3, 5, 6, 8, 9]
print(max(nums))
print(min(nums))
print(sum(nums))
print(average(nums))

#获取下标
print(courses)
print('Art' in courses)
print('Math' in courses)
print(courses.index('Chinese'))

# 遍历
print(courses)
for course in courses:
    print(course)

for i, course in enumerate(courses):
    print(i, course)

for i, course in enumerate(courses, start = 1):
    print(i, course)

# 列表转字符串
print(courses)
string = ' - '.join(courses)
print(string)

#反转
print(courses)
courses.reverse()
print(courses)

# 修改元素
courses[0] = 'materials'
print(courses)

# 集合 同 set, 元素无重复, 乱序
cs_courses = {'Math', 'Windows', 'English', 'MacOS'}
my_courses = {'Math', 'English', 'Metal'}

print(cs_courses.difference(my_courses))
print(cs_courses.intersection(my_courses))
print(cs_courses.symmetric_difference(my_courses))
print(cs_courses.union(my_courses))

# 创建空列表
empty_list1 = []
empty_list2 = list()

empty_set1 = {}   # 错误，和字典无法区分
empty_set2 = set()

# 字典
student = {'name': 'Cui', 'age': 24, 'course': ['Math', 'Chinese'], 2: 4}

# 获取 value
print(student)
print(student['course'])  # 如果不存在会报错
print(student.get('phone'))  #如果不存在就返回 None
print(student.get('phone', '12345'))  # 第二个参数放默认值

# 添加及修改
print(student)
student['address'] = 'NEU'
student['name'] = 'Scorpion'
print(student)

student.update({'phone': '12345', 'age': 100, 'name': 'Qiang'})   # 适用于同时添加或修改多个键值对
print(student)

# 删除
del student['address']

age = student.pop('age')
print(student)
print(age)

# 遍历
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(f'{key}: {value}')

# 条件语句
language = 'C++'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('no match')

# &&  and
# ||  or
# !   not

# False 的情况（除此以外，全为 True）
# None
# 0（任何数据类型）
# [] {} （空列表、空字典、空集合）

condition = ['Cui']
if condition:
    print('condition is true')
else:
    print('condition is false')

# == 比较内容
# is 比较地址
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
print(f'l1Id: {id(l1)};  l2Id: {id(l2)}')

# 循环和迭代
for i in range(10):   # [0, 10)
    print(i)

for i in range(2, 10):  # [2, 10)
    print(i)

s = 'abc'
for c in s:
    print(c)

x = 0
while x < 10:
    print(x)
    x += 1

# 函数
def hello_fun(greeting = 'Hello', name = 'Cui'):
    return '{}, {}'.format(greeting, name)

print(hello_fun())
print(hello_fun('Fuck', 'Yang'))


# *args 和 **kwargs 是约定好的，不能换成其他名称.
def fun1(*args):               # 放列表
    print(args)
fun1('NEU', 2026, [1, 2, 3])

def fun2(**kwargs):            # 放字典
    print(kwargs)
fun2(name= 'Cui', age= 24, address= 'NEUQ')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Math', 'Art', name= 'Cui', age= 10)

courses = ['Math', 'English', 'Metal']
info = {'name': 'Cui', 'age': 20}
student_info(courses, info)      # 将 [course, info] 看作 参数 args
student_info(*courses, **info)   # 解包

# 输入年份、月份，返回该月份有多少天
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_in_month(year, month):
    if month < 1 or month > 12:
        return 'Invalid month'
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(days_in_month(2026, 5))

