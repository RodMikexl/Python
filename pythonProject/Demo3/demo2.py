# -*- codeing = utf -*-
# @Time :10/02/2023 12:12 pm
# @Author : Weihong
# @File : demo2.py
# @Software : PyCharm

'''
f = open("test.txt","w") #文件打开，“w"写 文件不存在则新建文件

f.write("Hello world, I am here!") #将字符串写人文件中

f.close() #关闭文件
'''


# read方式，读取指定的字符，开始时定位在文件夹的头部，没执行一次则向后移动字符数
'''
f = open("test.txt","r")

content = f.read(5)  #读取

print(content)

content = f.read(10)

print(content)

f.close()
'''

#打印使用内容并且隔行
'''
f = open("test.txt","r")
content = f.readlines()

#print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i= i+1

f.close()
'''

'''
f = open("test.txt","r")
content = f.readline() #读一行
print("1:%s"%content,end="") #end不用空一行在写

content = f.readline()
print("2:%s"%content)

f.close()
'''

#文件重新命名
import os

os.rename("test.txt","test1.txt")
