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

