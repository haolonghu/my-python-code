# coding=gbk
import hashlib
str = input("��������Ҫ���ܵ��ַ���")
str1=input("���ٴ����룺")
if(str==str1):
	hl = hashlib.md5()
	hl.update(str.encode(encoding='utf-8'))
	print('Befor��' + str)
	print('After ��' + hl.hexdigest())
else:
	print("�������벻һ�£�����������!")
input()