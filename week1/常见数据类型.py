# num=114.1
# print(num)
#
# num=num+1
# print(num)

# base=20.7
# incr=50
# print(base+incr)
# print(base-incr)

#转义字符\' \" \n \t
# mg='it\'s very good'
# print(mg)
#
# mg1="it's very good"
# print(mg1)
#
# mg2="Hello 的意思是\"你好\""
# print(mg2)

# print("\t欢迎\n\t大家")#\n换行 \t缩进

# s1="你好""世界"
# print(s1)

# msg1="你好"
# msg2="世界"
# print("我说"+msg1+","+msg2)

#案例----str(int数字)--将int类型的数字转为字符串
# name="涛哥"
# age=18
# pro="软件工程"
# hobby="Python,java"
# print("大家好,我是"+name+",今年"+str(age)+"岁,学习的专业是"+pro+",爱好"+hobby)

#字符串格式化---1.%s占位符
# name="涛哥"
# age=18
# pro="软件工程"
# hobby="Python,java"
# print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s"%(name,age,pro,hobby))

#字符串格式化---2.f"{变量名/表达式}"---推荐方式
name="涛哥"
age=18
pro="软件工程"
hobby="Python,java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")