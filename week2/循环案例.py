"""
需求:根据输入的用户名密码执行登录操作，具体要求如下:

1. 正确的用户名和密码为admin/777888 、zhangsan/123456、taoge/888666

2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录

3.输入的用户名和密码不能为空!

4.登录成功:输出"登录成功，进入B站首页~"

5.登录失败:输出"用户名或密码错误，请重新输入!"

关键词:
break:只能出现在循环中,表示结束,跳出循环的含义(break跳出循环时,while后面的else代码不会执行)
continue:只能出现在循环中,表示结束本次循环,进入下一次循环
"""

# while True:
#     # 1.接收输入的用户名和密码
#     username=input("请输入正确的用户名:")
#     password=input("请输入正确的密码:")
#
#     # 2.校验:输入的用户名和密码不能为空
#     if username == ""or password=="":
#         print("输入的用户名和密码不能为空")
#         continue#结束当前循环,直接进入下一轮循环
#
#     # 3.判断用户名和密码的正确性
#     if username == "admin" and password == "777888":
#         print("登陆成功")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功")
#         break
#     else:
#         print("用户名和密码错误")

"""
需求:用户名密码登录，正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666,

5次登录机会，输入错误五次，不允许再操作了。
"""
# i=0
# while i<6:
#     usernamne=input("用户名:")
#     password=input("密码:")
#
#     if usernamne=="" or password=="":
#         print("不能为空")
#         continue
#
#     if usernamne=="admin" and password=="666888":
#             print("登录成功")
#             break
#     elif usernamne=="zhangsan" and password=="123456":
#             print("登录成功")
#             break
#     elif usernamne=="taoge" and password=="888666":
#             print("登录成功")
#             break
#     else:
#         print("登录失败")
#         i+=1
#         if i==5:
#             print("你输入错误五次，不允许再操作了")
#             break

"""
案例:猜数字
1.系统随机生成一个随机数

2.用户根据提示猜数字，并将所猜的数字输入系统

3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字

4.如果猜对，系统自动退出，游戏结束
"""
import random
random_num=random.randint(1,100)#生成随机数

while True:
    num=int(input("请输入一个数字:"))

    if num>random_num:
        print("你输入的数字太大了")
    elif num<random_num:
        print("你输入的数字太小了")
    else:
        print("你猜对了")
        break



