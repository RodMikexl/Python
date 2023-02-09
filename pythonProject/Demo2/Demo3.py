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
info = {"name":"RockMIke","age":"18"}

#字典的访问
print(info["name"])
print(info["age"])

#访问不存在的键
#print(info["gender"]) #直接访问会报错

#print(info.get("gender")) #使用get方法，没有找到对应的键，默认返回none

print(info.get("age","20"))   #找到则使用默认值
print(info.get("gender","m"))  #可以设定没找到的默认值


