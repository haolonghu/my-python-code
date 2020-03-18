import sys
print("参数的个数是",len(sys.argv))
for i in range(len(sys.argv)):
     print('sys.argv[%d]='%i+sys.argv[i])
