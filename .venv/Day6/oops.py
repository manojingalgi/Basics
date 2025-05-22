# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print("aditya",name)
#
# mc1 = MyClass()
# mc1.display("  Manoj")
#
#
# class Myclass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,num):
#         return (self,num)
#
# mc1= Myclass()
# mc1.m1()
# pp = mc1.m2(10,20)
# print(pp)


class Emp:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal


    def display(self):
        print(self.eid,self.ename,self.sal)

emp1 = Emp(1,"abhi",sal=10000)
emp1.display()  #1 abhi 10000

emp2 = Emp(2,"manu",234567)
emp2.display()  #2 manu 234567