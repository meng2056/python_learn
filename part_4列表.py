#使用  for 循环遍历列表
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    print(car.title())

#4.3 创建数值列表
##4.3.1 使用 range() 函数
for value in range(1,5):
    print(value)

##4.3.2 使用 range() 创建数字列表，list() 函数将range() 创建的数字列表转换成列表。
numbers = list(range(1,6))
print(numbers)# [1, 2, 3, 4, 5]

#range(2,11,3) 从2开始，每次增加3，直到11; 3 为步长

squares = []
for value in range(2,11,2):
    squares.append(value**2)
print(squares)

###4.3.4 列表推导式
sequares = [value**2 for value in range(1,11,2)]
print(sequares)

##test 4.3-4.9
numbers = [num for num in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = list(range(1,21,2))
for i in numbers:
    print(i)

numbers = [num for num in range(3,31) if num % 3 == 0]
for i in numbers:
    print(i)

numbers = list(num**3 for num in range(1,11))
for i in numbers:
    print(i)

##4.4 列表的切片
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:3])# [1, 2, 3]
print(numbers[3:])# [4, 5, 6, 7, 8, 9, 10]
print(numbers[:5])# [1, 2, 3, 4, 5]
print(numbers[-3:])# [8, 9, 10]

###4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #复制列表
print(my_foods)
print(friend_foods)

##4.5 元组
"""列表中的值是可变的。元组的值是不可变的。元组的索引和遍历与列表一样。"""
###4.5.1 定义元组， 使用圆括号()
dimensions = (200, 50) #即使只有一个元素也需要加,
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions: #遍历元组
    print(dimension)

##4.6 设置代码格式-PEP 8
"""PEP 8是Python的官方风格指南。"""
#1. 每级缩进都使用四个空格。
#2. 每行不超过80个字符。建议注释行不超过72个字符。
#3.程序的不同部分使用空行隔开。

