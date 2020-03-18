def add(a,b):
     return a+b
def sub(a,b):
     return a-b
def mul(a,b):
     return a*b
def div(a,b):
     return a/b
def squ(a,b):
     return a**b
#测试代码
def main():
     print('123+100=',add(123,100))
     print('123-100=',sub(123,100))
     print('123*100=',mul(123,100))
     print('123/100=',div(123,100))
     print('2**10=',squ(2,10))
if __name__=='__main__':
     main()
