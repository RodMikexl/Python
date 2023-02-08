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

#删减的方法 【del】 【pop】
'''
movieName = ["movie1", "movie2","movie3","movie4","movie2"]
print("---删除前，movie列表的数据---")
for name in movieName:
    print(name)

#del movieName[2]  #在指定位置删除一个元素
#movieName.pop()   #弹出末尾最后一个元素
movieName.remove("movie2") # #删除指定内容的元素 当出现2个时，则只会删除第一个

print("---删除后，movie列表的数据---")
for name in movieName:
    print(name)
'''

#改 【】
'''
namelist = ["Mike","Mkiex","Rock"]
print("---增加前，名单列表的数据---")
for name in namelist:
    print(name)

namelist[1] = "红" #修改指定下表元素内容

print("---增加后，名单列表的数据---")
for name in namelist:
    print(name)
'''

#查： 【in  .  not  in】
'''
namelist = ["Mike","Mkiex","Rock"]

findName = input("请输入要查找的人名:")

if findName in namelist:
    print("在名单中找到相同的名字")
else:
    print("没有找到")
'''

mylist = ["a","b","c","a","b"]

'''
print(mylist.index("a", 1, 4)) #查找范围 可以用来查找指定对应下标的元素， 找到并返回对应的下标位置

print(mylist.index("a", 1, 3))  #范围区间 左闭右开 [1,3）
                                #找不到会报错
'''

'''
print(mylist.count("c"))   #统计某个元素出席几次
'''

#排序和反转
'''
a = [1,4,2,3]
print(a)
a.reverse()     #将列表所有元素反转
print(a)
a.sort()       #升序
print(a)
a.sort(reverse=True)  #降序
print(a)
'''


# schoolName=[[],[],[]]    #有3个元素的空列表，每个元素都有给空列表
'''
schoolName= [["school1","school2"],["school3","school4","school5"],["school6","school7"]]

# print(schoolName[1][2])  #二维数组

for j in range(len(schoolName)):
    for i in range (len(schoolName[j])):
        print(schoolName[j][i])    #打印所有的元素列表
'''

#八个老师随机分配3个办公室
'''
import random
offices = [[],[],[]]

name= ["A","B","C","D","E","F","G","H"]

for name in name:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数:%d"%(i,len(office)))
    i = i + 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
'''

products=[["iphone",6888],["Macpro",14800],["小米6",2499],["Book",60],["Nike",699]]

i=0
print("-----商品列表-----")
for i in range(len(products)):
    print(i,products[i][0],products[i][1],end="\n")
    i=i+1

id=[]
money=[]

print("你想选择那件商品:")
