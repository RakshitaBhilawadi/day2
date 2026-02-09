class Student:
  college_name = "MITT College"
  def __init__(self,name,roll_no):
    self.name=name
    self.roll_no=roll_no

  @classmethod
  def change_college(cls,new_name):
    cls.college_name=new_name

  @staticmethod
  def is_pass(marks):
    if marks>=35:
      return "Pass"
    else:
      return "Fail"
    
  def display(self):
    print("Name:",self.name)
    print("Roll_no:",self.roll_no)
    print("College:", Student.college_name)
    

s=Student("Rakshita","AD047")
s.display()
Student.change_college("Swapnodaya")
s.display()
print("Result:", Student.is_pass(89))
