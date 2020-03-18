class Stack:
     def __init__(self,size=10):
          self.stack=[]
     def push(self,obj):
          self.stack.append(obj)
     def pop(self):
          try:
               return self.stack.pop()
          except IndexError as e:
               print("Stack is Empty")
     def __str__(self):
          return str(self.stack)
     
def main():
     stack=Stack()
     print("1~10入栈:")
     for i in range(1,11):
          stack.push(i)
          print(stack)
     print("1~10出栈:")
     for i in range(1,11):
          stack.pop()
          print(stack)
     stack.pop()
     
if __name__=='__main__':main()
