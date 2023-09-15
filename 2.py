#WAP to find the sum of two numbers using class and object 

#class car:
#  def show(abhishek):
#    print("Hello User",abhishek)
#obj=car()
#obj.show()  

#class calc:
# def sum(self,a,b):
#    c=a+b
#    print("Hello User",c)

class calc:
  def input_val(self):
    a=int(input())
    b=int(input())
    self.a1=a
    self.b1=b
  def sum(self):
    c=self.a1+self.b1
    print("Hello User",c)

obj1=calc()
obj1.sum(12,34)  

obj2=calc()
obj2.sum(23,34)

obj=calc()
print(type(obj))
