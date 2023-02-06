# -*- codeing = utf -*-
# @Time :4/02/2023 6:17 pm
# @Author : Weihong
# @File : Demo1.py
# @Software : PyCharm

'''
word = '字符串'
sentence = "这是个句子"
paragraph = """
            这是一个段落
            组成几行话
"""

print(word)
print(sentence)
print(paragraph)
'''

'''
# my_str = "I'm a student"
my_str = 'I\'am a student' # I'am a student
print(my_str)
'''

'''
#转义字符
my_str = "jack said \"he is a student\""
print(my_str)
'''

str = "chengdu"

'''
print(str)
print(str[0])
print(str[0:5]) #cheng 第1个到第6 [起始位置:偏移位置]
print(str[1:7:2]) #hnd 切片


print(str[:5]) #cheng
print(str[5:]) #du

print(str*3)

print("hello\nchengdu") #使用斜杠实现转义
print(r"hello\nchengdu") #前面加r和“\”前面加\可以不转义
 '''

#详细见字符串的常见操作
capitalizestr = str.capitalize()
print(capitalizestr) #将第一个字符串转换为大小写
