class Person:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def say_hi(self):
          print(str.format("hi,I am {0},age:{1}",self.name,self.age))
class Student(Person):
     def __init__(self,name,age,stu_id):
          Person.__init__(self,name,age)
          self.stu_id=stu_id
     def say_hi(self):
          Person.say_hi(self)
          print('I am a student,my id is %s'%self.stu_id)
p1=Person('zwq',23)
p1.say_hi()
p2=Student('hhl',19,'2018050576')
p2.say_hi()
