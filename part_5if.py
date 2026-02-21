##5.2 条件测试
"""每条if 语句的核心都是一个值为True,False的表达式，这种表达式叫条件测试。
例如："==" "!= " "> " "< ">=" "<=" "and" "or" "not" "in" "not in" "is" "is not"
"""
# if-else 语句
# if-elif-else 语句

###5.4.2确定列表非空
cars = []
if cars:  # 列表非空
    for car in cars:
        print(car.title())
else:  # 列表为空
    print("We need to find some cars!")

"""对于数值0，空值None,'',"",[],(){},python 都会返回False"""