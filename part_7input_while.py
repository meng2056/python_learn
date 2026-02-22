###7.1.1 input()函数
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

###7.1.2 使用int()来获取数值输入
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")

###7.1.3 求模运算符 %-将两数相除并返回余数
number = input("input a number,and i will tell you it's even or odd.")
number = int(number)
if number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

##7.2 while 循环
prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True # 控制循环的flag
while active:
    message = input(prompt)
    if message == 'quit':
       #active = False
       break
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

"""break 不在执行余下的代码并退出整个循环。continue 跳过当前循环的剩余代码并继续下一次循环。"""

##test 7.4-7.7
#7.4
prompt = "\n请输入pizza配料："
prompt += "\n输入q退出："
while True:
    message = input(prompt)
    if message == 'q':
        break
    else:
        print("添加配料：" + message)
    
#7.5
age = input("请输入你的年龄：")
age = int(age)
while True:
    if age < 3:
        print('免费')
        break
    elif age < 12:
        print('10dolls')
        break
    else:
        print('15 dollars')
        break

##7.3 while 循环处理列表和字典
"""for循环中不能修改列表，要想在遍历列表的同时修改它，可以使用while循环。"""

###7.3.1在列表中移动元素
list_1 = ['a','b','c','d']
list_2 = []
while list_1:
    current = list_1.pop()
    print(current)
    list_2.append(current)

for i in list_2:
    print(i)


