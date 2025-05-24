#example1 single inheritance

# class A:
#     def m1(self):
#         print("this is method of class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is method of class B")
#
# b_obj = B()
# b_obj.m1( )
# b_obj.m2( )
#

#Example2 single inheritance
#
# class A:
#     x,y=10,20
#
#     def m1(self):
#         print(self.x,self.y)
#
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a, self.b)
#
# a_obj =B()
# a_obj.m1()
# a_obj.m2()


#Example3 MULTI LEVEL inheritance

# class A:
#     x,y=100,200
#     def m1(self):
#         print(self.x +self.y)
#
# class B(A):
#     a,b = 10,20
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):
#     i,j=15,25
#     def m3(self):
#         print(self.i + self.j)
#
# c_obj = C()
# c_obj.m1()
# c_obj.m2()
# c_obj.m3()
#
#
#
#Example4 Multpile inhritance
#
# class A:
#     def m1(self):
#         a,b =10,20
#         print("This is method m1 sum: ", a+b)
#
# class B:
#     def m2(self):
#         i,j = 15,20
#         print(i*j)
#
# class C(A,B):
#     def m3(self,x,y):
#         print("This is child method :",x+y)
#
# k_obj =A()
# k_obj.m1()
# l_obj =C()
# l_obj.m1()
# l_obj.m3(5,6)
# l_obj.m2()
