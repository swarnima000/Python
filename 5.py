# class A:
#   def __init__(self,name):
#     self.name=name
#   def display(self):
#     print("Welcome",self.name)
# class B(A):
#   def show(self):
#     print("Hello",self.name)
# obj=B("Tamya")
# obj.display()




class A:
  def __init__(self,name):
    self.name=name
  def display(self):
    print("Welcome",self.name)
class B(A):
  def __init__(self):
    print("Constructor in Class B")
  def show(self):
    print("Hello",self.name)
obj=B("Tamya")
obj.display()
obj.show()

