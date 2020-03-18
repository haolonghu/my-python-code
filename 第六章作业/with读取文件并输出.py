import sys
filename=sys.argv[1]
line_no=0
with open(filename,'r',encoding="utf-8") as f:
	for line in f:
		line_no+=1
		print(line_no,":",line)
f.close   
