#遍历输入的字符串
# msg=input("请输入需要遍历的字符串:")
# for s in msg:#s表示遍历出来的元素;msg表示需要遍历的字符串
#     print(f"元素:{s}")

#计算1-100之间所有的奇数之和
#第一种
# total=0
# i=1
# while i<=100:
#     if i%2==1:
#         total+=i
#      i+=1
# print(total)

#第二种
# total=0
# for i in range(1,101):
#     if i%2==1:
#         total+=i
# print(total)
#简化版
# for i in range(1,101,2):
#     total+=i

#计算100-500之间所有3的倍数的数字之和
# total=0
# i=100
#
# while i<=500:
#     if i%3==0:
#         total+=i
#     i+=1
# print(total)

"""
循环嵌套:根据输入的长方形的长度m,宽度n,打印一个长方形;

如下:是一个长度为4,宽度为3的长方形
****
****
****

print()语句自带换行效果
print(,end="")end""表示的是每一次输入以什么结束;默认\n,表示换行
"""
# m=int(input("长度m为:"))
# n=int(input("宽度n为:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end="")
#     print()

#案例:打印99乘法表
for i in range(1,10):#外层循环--控制行
    for j in range(1,i+1):#内层循环--控制列
        print(f"{j}×{i}={j*i}",end="\t")
    print()