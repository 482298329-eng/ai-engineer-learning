#列表操作
#定义
# s=[56,90,88,"A",True]
# print(type(s))
# print(s[0])#正向索引从0开始
# print(s[-1])#反向索引从-1开始
# #修改
# s[1]="aaa"
# print(s)
# #删除
# del s[2]
# print(s)
# #遍历
# for item in s:
#     print(item)

#切片
# s=["a","b","c","d","e","f"]
# #切片操作是[开始索引:结束索引:步长]
# print(s[0:5:1])#可以简化
# print(type(s[0:5:1]))
# print(s[0:-1:])
# #列表的常用方法
# s.append(188)
# print(s)
# s.remove("a")
# print(s)
# s.insert(0,"s")
# print(s)
# e=s.pop(3)
# print(e)
# # s.sort()#排序,但数据类型不一样会运行错误
# # print(s)
# s.reverse()
# print(s)

#案例1:将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。
#定义一个列表
# num_list=[]
# #将用户输入的10个数字存入列表
# for i in range(10):
#     num=int(input("请输入一个有效的数字:"))
#     num_list.append(num)
#
# print("数字列表:",num_list)
# #排序
# num_list.sort()
# print("排序后的数字列表:",num_list)
# #输出案例要求,sum()求和,len()获取元素的个数
# print("最小值",num_list[0])
# print("最大值",num_list[-1])
# print("平均值",sum(num_list)/len(num_list))

"""
案例2:
合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
"""
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# #合并列表
# for num in num_list2:
#     num_list1.append(num)
#
# print("合并之后的列表",num_list1)
# #去重复记录
# new_list = []#去重之后的列表
# for num in num_list1:
#     #判断new_list中是否存在num元素
#     if num not in new_list:#判断元素是否存在于列表中,存在则True,不存在则False
#       new_list.append(num)
# print("最终列表:",new_list)

#简化版
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# #合并列表
# #解包:将列表这一类容器解开成一个一个独立元素
# #组包:将多个值合并到一个容器
# num_list=[*num_list1,*num_list2]
# print("合并之后的列表",num_list)
# #去重复记录
# new_list = []#去重之后的列表
# for num in num_list1:
#     #判断new_list中是否存在num元素
#     if num not in new_list:#判断元素是否存在于列表中,存在则True,不存在则False
#       new_list.append(num)
# print("最终列表:",new_list)

"""
案例3:
1.生成1-20的平方列表。-->rang(1,21)
2.从如下数学列表中提取所有偶数，并计算其平方，组成一个新的列表。
"""
#1.方式一
# num_list=[]
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
# #1.方式二:列表推导式-->[要插入的值 for i in 序列/列表]
# num_list2=[i**2 for i in range(1,20)]
# print(num_list2)

#2列表推导式-->[要插入的值 for i in 序列/列表 if 条件]
# num_list=[12,32,44,5,21,34,55,22]
# num_list=[i**2 for i in num_list if i%2==0]
# print(num_list)

#练习
"""
1.将如下多个列表合并为一个列表，并去重重复元素，排好序(升序)后输出到控制台。
#合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1=['M',A','C','E','F','G','H','L','N','I','J','K','0']
list2 = ['X','T','Y','E','F','G','Z']
list3 = ['w', 'A', 'S', 'D']
"""


"""
2.将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
#将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27,28,29, 30]
"""


"""
3.将如下列表中的正数提取出来，封装为一个新的列表。
#将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
"""