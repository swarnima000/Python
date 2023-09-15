#wap to create a class student and input marks of 5 subjects
#find average and percentage in disp() function 

class student:
  def input_val(self):
    eng=int(input())
    phy=int(input())
    chem=int(input())
    math=int(input())
    com=int(input())

    self.eng=eng
    self.phy=phy
    self.chem=chem
    self.math=math
    self.com=com
  
  def result(self):
    avg=(self.eng+self.phy+self.math+self.chem+self.com)//5
    print("Average is: ",avg)

    prcnt=((self.eng+self.phy+self.math+self.chem+self.com)*1/5)
    print("Percentage is: ",prcnt)
  
stu1=student()
stu1.input_val()
stu1.result()