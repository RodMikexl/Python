# -*- codeing = utf -*-
# @Time :3/02/2023 12:13 pm
# @Author : Weihong
# @File : demo3.py
# @Software : PyCharm

'''
#非0时为ture,0或false为false
#if True:
if 11:
    print("true")
    print("Answer") #同一程序必须要同一缩进
else:
    print("false")
print("end")
'''
'''
score =67

if score>=90:
    print("this grade 是 A")
elif score >= 80 and score < 90 :
    print("this grade 是 B")
elif score >= 70 and score < 80 :
    print("this grade 是 C")
elif score >= 60 and score < 70 :
    print("this grade 是 D")
#else:  #2个都可以
elif score >= 0 and score < 60 :
    print("this garde 是 E ")
'''

'''
xingBie =1 #1代表男，0代表女
denShen =1 #1代表单，0代表双

if xingBie ==1 :
    print("男")
    if denShen ==1:
        print("单")
    else:
        print("你崩三单")
else:
    print("女")
    print("...")
'''
'''
#引入库 随机数
import random  #随机数

x = random.randint(0,10) #随机生产0到10之间的数字
print(x)
'''

#剪刀石头布游戏
import  random

x = random.randint(0,2)
a = int(input("你的输入为：剪刀（0），石头（1），布（2）\n" ))

if a == x :
    print("平局")
else :
    if x == 0:
        print("随机数是剪刀（0）")
        if a ==2:
            print("你输掉了")
        elif a ==1:
            print("你赢了")
    if x == 1:
        print("随机数是石头（1）")
        if a == 2:
            print("你赢了")
        elif a == 0:
            print("你输掉了")
    if x == 2:
        print("随机数是布（2）")
        if a == 0:
            print("你赢了")
        elif a == 1:
            print("你输掉了")

