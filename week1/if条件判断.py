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
year=int(input("输入年份:"))
if (year%100 !=0 and year%4 ==0) or (year%400 ==0):
    print("是闰年")
else:
    print("是平年")