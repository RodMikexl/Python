# -*- codeing = utf -*-
# @Time :5/02/2023 6:08 pm
# @Author : Weihong
# @File : Demo2.py
# @Software : PyCharm

'''
#namelist = []    #定义一个空的列表

namelist = ["Mike","Mkiex","Rock"]

testlist = [1,"测试"]   #列表中可以存储混合类型

print(type(testlist[0]))
print(type(testlist[1]))

print(namelist[0])
print(namelist[1])
print(namelist[2])
'''

'''
namelist = ["Mike","Mkiex","Rock"]
for name in namelist:
    print(name)

# print(len(namelist)) #len()可以得到列表长度

length = len(namelist)

i = 0
while i<length:
    print(namelist[i])
    i = i+1
'''

#增加 【append】
'''
namelist = ["Mike","Mkiex","Rock"]

print("---增加前，名单列表的数据---")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的名字:")
namelist.append(nametemp)  #在末尾增加一个元素

print("---增加后，名单列表的数据---")
for name in namelist:
    print(name)
'''
'''
a = [1,2]
b = [3,4]
a.append(b) #将列表当作一个元素，加入列表a中
print(a)

a.extend(b) #将b列表的每个元素，追加到a列表中
print(a)
'''

'''
#增： [insert]
a = [0,1,2]
a.insert(1,3)   #第一个变量表示下标，第二个表示元素（对象）
print(a)      #输出为：[0, 3, 1, 2] 指定下表位置插入元素
'''

#删减的方法

