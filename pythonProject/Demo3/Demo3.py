# -*- codeing = utf -*-
# @Time :10/02/2023 1:50 pm
# @Author : Weihong
# @File : Demo3.py
# @Software : PyCharm

#异常报错
# print("------test----1-----")
#
# f = open("123.txt", "r")      #用只读模式打开了一个不存在的文件，报错
#
# print("------test----2-----") #这局代码不会被执行


#捕获异常
'''
try:
    print("------test----1-----")

    f = open("123.txt","r")

    print("------test----2-----")

except IOError:   #文件没找到，属于IO异常（输入输出异常)
    pass          #捕获异常后，执行代码
'''

'''
try:
    print(num)
# except IOError: #异常类型想要捕获，需要相同类型
except NameError:
    print("产生错误")
'''

'''
try:
    print("------test----1-----")
    f = open("test1.txt","r")
    print("------test----2-----")
    f.close()
    print(num)
except (NameError,IOError): #将所有可能产生的异常类型，都放在括号里面
    print("产生错误")
'''

#或许错误描述
'''
try:
    print("------test----1-----")
    f = open("123.txt","r")
    print("------test----2-----")
    f.close()
    
    print(num)
except (NameError,IOError)as result: #将所有可能产生的异常类型，都放在括号里面
    print("产生错误")
    print(result)
'''

#捕获所有的异常
'''
try:
    print("------test----1-----")
    f = open("test1.txt", "r")
    print("------test----2-----")
    f.close()

    print(num)
except Exception as result:  #Exception可以显示所有的异常
    print("产生错误")
    print(result)
'''

#try 。。。。。 finally 嵌套




