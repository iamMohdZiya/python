
# # # # # # # class student:
# # # # # # #      def  __init__(self,name,mark1,mark2,mark3):
# # # # # # #           self.name = name
# # # # # # #           self.marks = [mark1, mark2, mark3]
# # # # # # #           self.total = sum(self.marks)
# # # # # # #           student.avg(self)
# # # # # # #      def avg(self):
# # # # # # #             avg = self.total / len(self.marks)
# # # # # # #             print(f"{self.name} has average of {avg}")

# # # # # # # s1 = student("john", 90, 80, 70)
# # # # # # # s2 = student("jane", 85, 75, 95)
# # # # # # # # s1.avg()
# # # # # # # # s2.avg()
        



# # # # # # class Car:
# # # # # #     def __init__(self,acc,clh,brk):
# # # # # #         self.acc= acc
# # # # # #         self.clh = clh
# # # # # #         self.brk= brk

# # # # # #     def start(self):
# # # # # #         self.acc= True
# # # # # #         self.clh = True
# # # # # #         self.brk= False
# # # # # #         print("Car is Started...")
# # # # # #     def stop(self):
# # # # # #         self.acc= False
# # # # # #         self.clh = True
# # # # # #         self.brk= True
# # # # # #         print("Car is stopped...")

# # # # # # car = Car(True,True,False)
# # # # # # car.start()
# # # # # # car.stop()
# # # # # # make a setter and getter method for private variables in class

# # # # class profile:
# # # #     def __init__(self):
# # # #         # self.__id= id #private
# # # #         # self.__password= password #private
# # # #         pass
# # # #     def getData(self):
# # # #         self.__display()
# # # #     def setData(self,id,password):
# # # #         self.__id= id
# # # #         self.__password= password
# # # #     def __display(self):
# # # #         print(f"your id is {self.__id} and password is this {self.__password}")

# # # # p = profile()
# # # # p.setData("123","123")
# # # # p.getData()
# # # # p.setData("999","999")
# # # # # p.getData()
# # # # class Account:
# # # #     def __init__(self,acc,bal,password):
# # # #         self.__acc = acc
# # # #         self.bal= bal
# # # #         self.__password= password
# # # #     def debit(self,amount):
# # # #         if ( amount < self.bal ):
# # # #             self.bal=self.bal-amount
# # # #         else:
# # # #             print("Insufficient Balance") 
# # # #     def credit(self,amount):
# # # #         self.bal=self.bal+amount
# # # #     def display(self):
# # # #         print(f"your balance is {self.bal}")

# # # # a = Account(9999,100,"123")
# # # # a.display()
# # # # a.credit(10)
# # # # a.display()
# # # # a.debit(1000)
# # # # a.display()

# # # # make a add function to add imaginary and normal numbers
# # # class Complex:  
# # #     def __init__(self, real, imag):
# # #         self.real = real
# # #         self.imag = imag

# # #     def display(self):
# # #         print(f"{self.imag}i + {self.real}")
# # #     def add(self , c2 ):
# # #         newImag = self.imag + c2.imag
# # #         newReal= self.real + c2.real
# # #         return Complex(newImag , newReal)
# # #     def sub(self , c3):
# # #         newImag = self.imag - c3.imag
# # #         newReal= self.real - c3.real
# # #         return Complex(newImag , newReal)



# # # c = Complex(5,4)
# # # c.display()

# # # c2 = Complex(5,4)

# # # addition = c.add(c2)

# # # addition.display()

# # # subtraction =c.sub(c2)

# # # subtraction.display()



# # class Circle:
# #     def __init__(self,r):
# #         self.r = r
# #     def display(self):
# #         print(f"radius of circle = {self.r}")
# #     def area(self):
# #         area = 3.14 * (self.r)**2
# #         print(f"area of circle {area}")
# #     def perimeter(self):
# #         perimeter = 2 * 3.14 * (self.r)**2
# #         print(f"perimeter of circle {perimeter:.3F} ")
# # c = Circle(12)
# # c.display()
# # c.perimeter()
# # c.area()



# class emp:
#      def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary= salary 
#      def showDetails(self):
#           print(f"Your role is {self.role},your dept {self.dept} and salary {self.salary} " )

# # e = emp("developer","Technical",90_0000)
# # # e.getDetails()
# # e.showDetails()


# class Engineer(emp):
#     def __init__(self,name, age, role, dept, salary):
#         super().__init__(role , dept , salary)
#         # self.role = role
#         # self.dept = dept
#         # self.salary= salary 
#         self.age = age 
#         self.name = name 
#     def showDetails(self):
#           print(f"{self.name} and age = {self.age}" )
#           super().showDetails()

# e = Engineer("ziya",20,"Developer","IT",9000000)
# e.showDetails()






