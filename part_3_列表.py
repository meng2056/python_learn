#3.1.1 访问列表元素
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print(bikes[0])
print(bikes[-1])
print(f"I would like to own a {bikes[0].title()}.")

#test 3.1
names = ['Allan', 'James', 'Jimmy']
print(f"{names[0]} is my friend.")
print(f"Hello, {names[1]}")

#3.2.1 修改列表元素
bikes = ['honda', 'yamaha', 'suzuki']
bikes[0] = 'ducati'
print(bikes)

#3.2.2 列表元素-使用append在列表末尾添加一个元素
bikes.append('ducati') #使用append在列表末尾添加一个元素
print(bikes)

bikes.insert(1, 'bmw') #在列表指定位置添加元素
print(bikes)

del bikes[0]  #删除列表元素
print(bikes)

popped_bike = bikes.pop() #删除列表末尾元素，并返回该元素,也可以使用pop()删除列表中任意位置的元素，在()中指定索引
print(bikes)
print(popped_bike)

bikes.remove('yamaha') #删除列表中指定值的元素，删除的元素值必须唯一
print(bikes)

##test 3.2
names = ['Allan', 'James', 'Jimmy']
print(f"我邀请的嘉宾有:{names[0]},{names[1]},{names[2]}")
print(f"{names[2]}无法赴约")
names[2] = 'Tom'
print(f"我邀请的嘉宾有:{names[0]},{names[1]},{names[2]}")
names.insert(0, 'Lucy')
names.insert(3, 'Mike')
names.append('Lily')
print(f"我邀请的嘉宾有:{names[0]},{names[1]},{names[2]},{names[3]},{names[4]},{names[5]}")
names.pop()
print(f"我邀请的嘉宾有:{names[0]},{names[1]},{names[2]},{names[3]},{names[4]}")
names.remove('Mike')
del names[1]
print(names)

#3.3 管理列表
#使用sort()对列表进行永久排序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#使用sorted()对列表进行临时排序，不影响列表原始顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#使用reverse()对列表进行反转，列表元素位置会发生变化。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#使用len()获取列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#test 3.3
names = ['tianjin', 'beijing', 'shanghai', 'guangzhou', 'shenzhen']
print(names)
print(sorted(names))
print(names)
print(sorted(names, reverse=True))
print(names)
names.reverse()
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)