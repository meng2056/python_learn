###8.1.2 实参和形参
def user_greet(user_name):
    """显示简单的问候语"""
    print(f"hello,{user_name.title()}")

user_greet('jesse')
"""调用user_greet()时，将实参'jesse'赋给形参'user_name'."""

###8.2 传递参数
###8.2.1 位置实参
"""基于实参的位置去关联函数中定义的形参"""
def pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"my {animal_type}'s name is {pet_name.title()}.")

pet('dog','willie')

###8.2.2 关键字实参
def pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"my {animal_type}'s name is {pet_name.title()}.")

pet(animal_type='dog',pet_name='willie')

###8.2.3 默认值
"""在编写函数时，可以给每个形参指定默认值，如果在调用函数中给形参提供了实参，Python将
使用指定的实参值，否则，将使用形参的默认值。"""
def pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"8.2.3\nmy {animal_type}'s name is {pet_name.title()}.")

pet('willie')
pet('harry','hamster')

##8.3返回值
###8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    dic_full_name = {'first_name': first_name, 'last_name': last_name}
    return f"{full_name.title()}\n{dic_full_name}"

musician = get_formatted_name('jimi','hendrix')
print(musician)

###8.3.4 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return f"{full_name.title()}"

while True:
    print("\ntell me your name:")
    print("enter 'q' at any time to quit")
    first_name = input("first_name:")
    if first_name == 'q':
        break
    last_name = input("last_name:")
    if last_name == 'q':
        break
    full_name = get_formatted_name(first_name, last_name)
    print(f"hello, {full_name}")
 

def make_album(artist_name, album_title, song_num=None):
    """返回一个字典，其中包含专辑的歌手和标题。"""
    if song_num:
        album = {'artist_name': artist_name, 'album_title': album_title, 'song_num': song_num}
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album

album = make_album('taylor swift', '1989')
print(album)
albums = make_album('taylor swift', '1989', 12)
print(albums)

##8.4 传递列表
def get_play(new,old):
    """打印列表中存储的元素"""
    while old:
        current = old.pop()
        new.append(current)
        print(f"{new}")

def show_play(new):
    """打印列表中存储的元素"""
    for new in new:
        print(f"{new}")

old = ['1','2','3']
new = []
get_play(new,old)
show_play(new)

##8.5 传递任意数量的实参
"""使用星号(*)来让函数接受任意数量的实参。"""
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(f"- {topping}")
    

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

###8.5.2 使用任意数量的关键字实参
"""使用**来让函数接受任意数量的关键字实参。"""
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的用户信息"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',)
print(user_profile)
"""**user_info的俩个星号让Python创建一个名为user_info的空字典。"""

##8.6 将函数存储在模块中
"""将函数存储在模块中，然后从模块中导入函数。"""
###8.6.1 导入整个模块
"""
在模块中定义的函数，然后从模块中导入整个模块。
在pizza.py中定义make_pizza()函数。在seal.py中 import pizza
"""
###8.6.2 导入特定的函数
"""
在模块中定义的函数，然后从模块中导入特定的函数。
在pizza.py中定义make_pizza()函数。在seal.py中 import pizza.make_pizza()
"""
###8.6.3 使用as 给函数指定别名
"""给导入的函数指定别名。例：from pizza import make_pizza as mp"""
###8.6.4 使用as 给模块指定别名
"""给导入的模块指定别名。例：import pizza as p"""
###8.6.5 导入模块中的所有函数
"""
from pizza import *
注意：如果导入模块中的函数与当前项目中的函数出现重名，会覆盖掉当前项目函数。
"""
##8.7 函数编写指南
"""
1.函数名应该使用小写，并使用下划线来分隔单词。
2.给形参指定默认值时，等号俩边不要有空格。例：def function_name(parameter_0, parameter_1='default value')
3.函数调用时，在等号俩边也不要有空格。例：function_name(value_0, value_1='value')
4.PEP 8建议代码行长度不超过79个字符，如果形参过多，可在函数定义中输入左括号后按回车键，并在下一行连按俩次Tap键，
从而将形参列表与只缩进一层的函数体区分开。
def fun_name(
        parameter_0,
        parameter_1,
):
    function_body...
"""