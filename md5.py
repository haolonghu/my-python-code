# coding=gbk
import hashlib
str = input("请输入需要加密的字符：")
str1=input("请再次输入：")
if(str==str1):
	hl = hashlib.md5()
	hl.update(str.encode(encoding='utf-8'))
	print('Befor：' + str)
	print('After ：' + hl.hexdigest())
else:
	print("两次输入不一致，请重新输入!")
input()