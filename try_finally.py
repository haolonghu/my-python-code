try:
	f=open("test.txt","w")
	while True:
		s=str(input('请输入字符串，输入Q结束：'))
		if s.upper()=='Q':break
		f.write(s+'\n')
except KeyboardInterrupt:
	print('程序中端!(Ctrl+C)')
finally:
	f.close()