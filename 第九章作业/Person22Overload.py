class Person22:
     def say_hi(self,name):
          print('你好，我叫',self.name)
     def say_hi(self,name,age):
          print(str.format("hi,{0},年龄{1}",name,age))

p=Person22()
p.say_hi('Lisa',22)
p.say_hi('Bob')
