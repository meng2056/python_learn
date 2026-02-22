###6.2.7 使用get()来访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
"""get()方法在字典中有points键时返回对应的值，否则返回第二个参数指定的值。"""

##6.3 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
"""items()方法返回一个包含字典所有键值对的列表，列表中包含两个元素，第一个元素是键，第二个元素是键对应的值。"""

###6.3.2 遍历字典中的所有键 -keys()方法
love_numbers = {
    'jen': 10,
    'sarah': 7,
    'edward': 12,
    'phil': 8,
}
for name in love_numbers.keys():
    print(name.title())

for name in love_numbers:
    if name == 'jen':
        num = love_numbers[name]
        print(f"{name.title()}  favorite number is {num}!")

###6.3.3 按照特定的顺序遍历字典中的所有键
for name in sorted(love_numbers.keys()):
    num = love_numbers[name]
    print(f"{name.title()} favorite number is {num}!" )

###6.3.4 遍历字典中的所有值
for num in love_numbers.values():
    print(num)

#set()集合：集合中的每个元素都必须是独一无二的
languages = {'python', 'c', 'c++', 'java'} 
"""这是集合，也用{}定义，但是它没有键值对，集合中的元素是唯一的，集合中的元素是无序的"""

##6.4 嵌套
"""将多个字典存储在列表中、或将列表作为值存储在字典中，这叫嵌套。"""

###6.4.1 在列表中存储字典
alines = []

for alines_num in range(5):
    new_aline = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alines.append(new_aline)

print(type(alines))
print(len(alines))

for A in alines:
    if A['color'] == 'green':
        A['color'] = 'yellow'
        A['speed'] = 'medium'
        A['points'] = 10
    print(A)

###6.4.2  在字典中存储列表
pizza = {
    'crusts':['thick','thin','regular'],
    'toppings':['mushrooms', 'extra cheese'],
}

for crust,topping in pizza.items():
    print(f"you orederde a {crust}")
    for T in topping:
        print(f"\t{T}")

###6.4.3 在字典中存储字典
school = {
    'class1':{
        'name':'Allan',
        'age':18,
        'sex':'male',
        'grand':'1',
    },
    'class2':{
        'name':'Mike',
        'age':17,
        'sex':'male',
        'grand':'2',
    },
}

for class_name,class_info in school.items():
    print(f"{class_name}")
    for k,v in class_info.items():
        print(f"\t{k}:{v}")

##test 6.7-6.12
#6.7
peoples = [
    {'name':'Allan','age':18},
    {'school':'highschool', 'grade':'1'},
    {'sex':'male','location':'china'}
]
for people in peoples:
    for k,v in people.items():
        print(f"{k}:{v}")

#6.9
love_places = {
    "Allan":['上海','北京','杭州'],
    "jack":['深圳','广州','厦门'],
    "lily":['苏州','南京','合肥'],
}

for name,places in love_places.items():
    print(f"{name} 稀罕的地方有：")
    for place in places:
        print(f"\t{place}")

#6.11
cities = {
    '上海':{'country':'中国','population':'1000万','description':'中国魔都'},
    '北京':{'country':'中国','population':'1000万','description':'中国首都'},
    '广州':{'country':'中国','population':'1000万','description':'中国省份'},
}
for city,info in cities.items():
    print(f"{city}的详细信息有：")
    for k,v in info.items():
        print(f"\t{k}:{v}")
for city in cities.keys():
    print(city)
for info in cities.values():
    print(info)