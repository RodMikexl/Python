# -*- codeing = utf -*-
# @Time :9/02/2023 10:34 am
# @Author : Weihong
# @File : Demo3.py
# @Software : PyCharm

#列表是[ ]，元组是（），集合是{}
#元组的创建
'''
tup1 = () #创建空的元组
print(type(tup1))

# tup2 = (50) #<class 'int'>
# tup2 = (50,)   #数字后面加给“,”则变成元组<class 'tuple'>
tup2 = (50,60,70)
print(type(tup2)) <class 'tuple'>
'''

'''
tup1=("abc","def",2000,2000,333,444)

print(tup1[0])
print(tup1[-1])  #最后一个元素
print(tup1[1:5]) #('def', 2000, 2000, 333)不包含5
'''


#增加  (链接）
'''
tup1 = (12,34,56)
tup2 = ("abc","xyz")

tup = tup1+tup2
print(tup)  
#输出(12, 34, 56, 'abc', 'xyz')
'''

#删减
'''
tup1 = (12,34,56)
print(tup1)
del tup1  #删除整个元组变量
print("删后：")
print(tup1)
'''

#更改  -不能修改
# tup1 = (12,34,56)
#
# tup1[0] = 100  #报错，不允许修改

#查询
'''
tup1=("abc","def",2000,2000,333,444)

print(tup1[0])
print(tup1[-1])  #最后一个元素
print(tup1[1:5]) #('def', 2000, 2000, 333)不包含5
'''

#字典的定义
# info = {"name":"RockMIke","age":"18"}

#字典的访问
'''
print(info["name"])
print(info["age"])

#访问不存在的键
#print(info["gender"]) #直接访问会报错

#print(info.get("gender")) #使用get方法，没有找到对应的键，默认返回none

print(info.get("age","20"))   #找到则使用默认值而不会变
print(info.get("gender","man"))  #可以设定没找到的默认值
'''

#增加
'''
info = {"name":"RockMIke","age":"18"}
newID = input("请输入新的学号:")
info["id"] = newID

print(info["id"])
'''

#删减
#[del]
'''
info = {"name":"RockMIke","age":"18"}
print("删除前: %s"%info["name"])

del info["name"]

# print("删除后: %s"%info["name"]) #删除了指定位置后，在访问会报错
'''

'''
info = {"name":"RockMIke","age":"18"}
print("删除前: %s"%info)

del info
print("删除前: %s"%info)  #删除字典后会报错
'''

#[clear]

'''
info = {"name":"RockMIke","age":"18"}
print("清空前: %s"%info)
info.clear()
print("清空后: %s"%info)
'''

#修改
'''
info = {"name":"RockMIke","age":"18"}

info["age"] = 20

print(info["age"])
'''


#查询  遍历

info = {"id":1,"name":"RockMIke","age":18}
'''
print(info.keys())   #得到所有的键（列表形式)
print(info.values())    #得到所有的值（列表形式)

print(info.items())     #得到所有的项（列表形式)
'''
#遍历所有的键
'''
for key in info.keys():
    print(key)
'''

#遍历所有的值
'''
for value in info.values():
    print(value)
'''

#遍历所有的键值对
'''
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

#使用枚举函数，同时拿到列表中的下表和元素内容
mylist=["a","b","c","d"]

for i,x in enumerate(mylist):
    print(i+1,x)

