#打印十遍"你好"
# i=0
# while i<10:
#     print("你好")
#     i+=1
# else:
#     print("正常结束")

#计算1-100之间所有偶数之和
total=0#记录累加之和
i=1#循环开始数字

while i<=100:
    if i%2==0:
        total+=i
    i+=1
print(total)