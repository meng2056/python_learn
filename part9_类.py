##9.1创建和使用类
###9.2.3 修改属性的值
#01.直接修改属性的值
class Car:
    def __init__(self,name,make,model):
        self.name = name
        self.make = make
        self.model = model
        self.year = 0 

    def read(self):
        print(f"车的年龄是{self.year}")
    
car = Car('aodi','bmw','auto')
car.read()
car.year = 9  #通过实例访问，直接修改属性的值
car.read()

#02.使用方法修改属性的值
"""
class Car:
    --snip--
    def update_year(self,new_value):
        self.year = new_value

car = Car('aodi','bmw','auto')
car.update_year(10) ###通过方法传递参数
"""
#03.使用方法让属性的值递增

##test 9.5
class User:
    def __init__(self,login_atte):
        self.login_atte = login_atte

    def increment_login_atte(self):
        self.login_atte += 1
    
    def reset_login_atte(self):
        self.login_atte = 0

user = User(10)
user.increment_login_atte()
print(user.login_atte)
user.increment_login_atte()
print(user.login_atte)
user.reset_login_atte()
print(user.login_atte)

##9.3 继承
###9.3.1 子类的 __init__()方法
"""在既有类的基础上编写新类，通常要调用父类的__init__()方法。这将初始化在父类的__init__()
方法中定义的所有属性，从而让子类也可以使用这些属性。"""

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

###9.3.2 给子类定义属性和方法

###9.3.3 重写父类中的方法

###9.3.4 将实例用作属性
class Car:
    pass

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    
    def descript_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()  #将实例用作属性
    
my_leaf = ElectricCar('bmw','leaf',2024)
my_leaf.battery.descript_battery() #可以直接访问

##9.4 导入类
###9.4.1 导入单个类

##9.6 类的编程风格
"""
1.类名应采用驼峰命名法，即将类名中的每个单词的首字母大写，不使用下划线。
2.实例化和模块名都采用全小写格式，并在单词之间加下划线。
3.每个类定义后面都应该紧跟一个docstring。
4.可以使用空行来组织代码，但不宜过多了。类中使用一个空行来分隔方法，在模块中，可以使用俩个
空行分隔类。
5.当需要同时导入标准库的模块和自定义的模块时，先导入标准库的模块，空一行，再导入自定义的模块

"""
