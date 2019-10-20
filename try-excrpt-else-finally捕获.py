#coding:utf-8
try:
	file=open("hhl.txt","w")
	file.write("123456")
	#f1=open("2.txt","r")
except IOError:
	print("Error")
else:
	print("Finish!")
finally:
	file.close()