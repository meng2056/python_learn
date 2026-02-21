#2.3.1 使用方法修改字符串的大小写。
message = "hello world!"
print(message.title())
print(message.upper())
print(message.lower())

##方法是python可对数据执行的操作。每个方法后面都跟着一对括号，用来补充信息。

#2.3.2 在字符串中使用变量
first_name = "eda"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}!")

##要在字符串中插入变量的值，要在引号（"）外加上字母f。

#2.3.3使用制表符（\t）或换行符（\n）来添加空白。
print("language:\n\tpython.\n\tC.\n\tJavaScript")

#2.3.4 删除空白
favorite_language = " python "
print(favorite_language.strip())
print(favorite_language.rstrip())
print(favorite_language.lstrip())

##lstrip()、rstrip()、strip()方法分别删除字符串开头的空白、结尾的空白、两端的空白。

#删除前缀
base_url = "https://www.baidu.com"
print(base_url.removeprefix("https://"))

#test 2.3
name = "eric"
lesson = "Python"
print(f"Hello {name},would you like to learn some {lesson}")
print(name.title(),name.upper(),name.lower())
message = "Albert Esinstein once said, 'A person who never made a mistake never  " \
"tried anything new.'"
print(message)

name = "\tAllan\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

file_name = "file.txt"
print(file_name.removeprefix("file."))
print(file_name.removesuffix(".txt"))

#2.4 数
##2.4.5 同时给多个变量赋值
a,b,c = 1,2,3
print(a,b,c)

#2.4.6 创建常量
PI = 3.14

##常量要使用全大写字母。指程序中不会改变的值。

##test 2.4
print(5+4)
print(10-2)
print(2*4)
print(16/2)

VALUE = 5
print(f"我最喜欢的数字：{VALUE}")

# 2.6 Python 之禅
import this