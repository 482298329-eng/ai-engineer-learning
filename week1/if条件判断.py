#案例:完成网站登录功能的实现
#正确的账号和密码
# ok_account="1888888"
# ok_password="777888"
# #1.接受输入
# account=input("请输入账号:")
# password=input("请输入密码:")
# #2.判断是否正确
# if account==ok_account and password==ok_password:
#     print("密码正确")
# #3.如果错误,则登录失败
# if account!=ok_account or password!=ok_password:
#     print("密码错误")

#案例:判断年份是闰年还是平年(非整百年且能被4整除;整百年必须被400整除)
# year=int(input("输入年份:"))
# if (year%100 !=0 and year%4 ==0) or (year%400 ==0):
#     print("是闰年")
# else:
#     print("是平年")

#案例:根据输入的用户名,密码进行登录系统
# username=input("请输入用户名:")
# password=input("请输入密码:")
#
# if username=="admin" and password=="777888":
#     print("登录成功")
# elif username =="root" and password=="123123":
#     print("登录成功")
# elif username =="zhangsan" and password=="234234":
#     print("登录成功")
# else:
#     print("登录失败")

"""
案例:三角形类型判断
1.构成三角形的条件:两边之和大于第三边
2.两边相等:等腰三角形,三个边相等:等边三角形,三个边都不相等:普通三角形
"""
# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
#
# if a+b>c and a+c>b and b+c>a:
#     if a == b and b == c :
#         print("是等边三角形")
#     elif a==b or a==c or b==c:
#         print("是等边三角形")
#     else:
#         print("是普通三角形")
# else:
#     print("不是三角形")

"""
电费计算
阶梯电价规则:
第一档:2880度以下,电费单价0.4883元/度
第二档:2880-4880度,电费单价0.5383元/度
第三档:4880度以上,电费单价0.7883元/度
"""
electricity=int(float("消费的电量:"))
if 0<electricity<2880:
    print("电费为:",electricity*0.4883)
elif 2880<electricity<4880:
    print("电费为:",electricity*0.5383)
elif 4880<electricity:
    print("电费为:",electricity*0.7883)
else:
    print("输入的电度数错误")