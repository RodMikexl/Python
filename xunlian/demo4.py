# -*- codeing = utf -*-
# @Time :3/02/2023 1:06 pm
# @Author : Weihong
# @File : demo4.py
# @Software : PyCharm

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,10,3): #从0开始到10结束 步进值为3 每次加3
    print(i)
'''

'''
for i in range(-10, -100, -30):
    print(i)
'''

'''
name = "chengdu"
for x in name:
   # print(x)
   #print(x, end="")
    print(x,end="\t")
'''

'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])

#输出为
#0 aa
#1 bb
#2 cc
#3 dd
'''

'''
i=0
while i<5:
    print("这是第%d次循环"%(i+1))
    print("i=%d"%i)
    i +=1 #i=i+1
'''

'''
1-100求和
n=100
sum=0
counter = 1

while counter<= n:
    sum = sum + counter
    counter +=1

print("1到%d的和是:%d"%(n,sum))

#用for的形式
sum = 0
for x in range(1,101):
    sum = sum+x
else:
  print("1到%d的和是:%d"%(x,sum))

'''


# count = 0
# while count<5:
#     print(count,"小于5")
#     count = count + 1
# else:
#     print(count,"大于或者等于5")

# i = 0
# while i<10:
#     i = i + 1
#     print("-"*30)
#     if i == 5 :
#         # break #break 结束整个while循环
#         continue #contiue 结束本次循环
#     print(i)

# i=1
# j=1
# for i in range (1,10):
#     for j in range(1, i + 1):
#         print("%d*%d=%d"%(i,j,i*j),end=" ")
#     print("")
#

'''
错误例子
i = 1
j = 1
while i < 10 :
    while j < i + 1 :
        print("%d*%d=%d"%(i,j,i*j),end = " ")
        print("")
'''

#正确例子
# i = 1
# j = 1
# while i < 10:
#     while j < i + 1:
#         print("%d*%d=%d" % (i, j, i * j), end=" ")
#         j += 1
#     print("")
#     j = 1
#     i += 1






