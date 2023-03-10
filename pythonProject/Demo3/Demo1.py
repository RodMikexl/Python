# -*- codeing = utf -*-
# @Time :10/02/2023 11:24 am
# @Author : Weihong
# @File : Demo1.py
# @Software : PyCharm

#函数的定义
'''
def printinfo():
    print("-------------")
    print("    Python   ")
    print("-------------")

#函数的调用

printinfo()
printinfo()
'''


#带参数的函数
'''
def add2Num(a,b):
    c = a + b
    print(c)
    

add2Num(11,22)
'''

#带返回值的函数
'''
def add2Num(a,b):
    return a+b  #通过return来返回运算结果

result = add2Num(11,22)
print(result)
#print(add2Num(11,22))
'''

#返回多个值的函数
'''
def divid(a,b):
    shang = a//b
    yushu = a%b
    return  shang,yushu     #多个返回值用都好分割

sh,yu = divid(5,2)   #需要使用躲过值来保存返回内容

print("商:%d， 余数:%d"%(sh,yu))
'''

#写一个打印一条横线的函数
'''
def printOneline():
    print("-"*30)

printOneline()
'''

#写一个打印多条横线的函数
'''
def printOneline():
    print("-"*30)

def printNumline(num):
    i = 0
    while i < num:
        printOneline()
        i = i+1

#printNumline(3)
printNumline(int(input("请输入你想打印的横线数:")))
'''

#求三给数的和
'''
def sum3Number(a,b,c):
    return a+b+c

result = sum3Number(1,2,3)
print(result)
'''

#完成三个数的平均值
'''
def sum3Number(a,b,c):
    return a + b + c

def average3Number(a,b,c):
    sumResult = sum3Number(10,20,30)
    aveResult = sumResult/3.0
    return  aveResult

result = average3Number(10,20,30)
print("平均值为:%d"%result)
'''

#全局变量和局部变量
'''
def test1():
    a = 300     #局部变量
    print("test1--------修改前: a = %d"%a)
    a = 100
    print("test1--------修改后: a = %d" % a)

def test2():
    a = 500     #不同函数
    print("test2-------- a = %d" % a)


test1()
test2()
'''

#全局变量
'''
a = 100 #全局变量

def test1():
    print(a)

def test2():
    print(a)   #调用全局变量

test1()
test2()
'''

#全局变量和局部变量的名字相同
'''
a = 100
def test1():    #局部变量优先于全局变量
    a = 300     #局部变量
    print("test1--------修改前: a = %d"%a)
    a = 200
    print("test1--------修改后: a = %d" % a)

def test2():
    print("test2-------- a = %d" % a)  #如果没有局部变量则默认使用全局变量


test1()
test2()
'''

#在函数中修改全局变量

a = 100
def test1():    #局部变量优先于全局变量
    global a      #声明全局变量在函数中的标识符
    print("test1--------修改前: a = %d"%a)
    a = 200
    print("test1--------修改后: a = %d" % a)

def test2():
    print("test2-------- a = %d" % a)  #如果没有局部变量则默认使用全局变量
    #test2-------- a = 200

test1()
test2()


