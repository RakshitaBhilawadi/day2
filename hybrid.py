class Person:
  def __init__(self,name):
    self.name=name
  def display_person(self):
    print("Person name is:",self.name)

class Student(Person):
  def __init__(self,student_id,name):
    Person.__init__(self,name)
    self.student_id=student_id
  def display_student(self):
     print("ID:",self.student_id)

class SportsPlayer(Person):
  def __init__(self,sport_name, name):
    Person.__init__(self,name)
    self.sport_name=sport_name
  def display_sports_player(self):
    print("Sport:",self.sport_name)

class CollegeStudent(Student, SportsPlayer):
    def __init__(self,name,student_id,sports_name,college_name,):
      SportsPlayer.__init__(self,sports_name,name)
      Student.__init__(self,student_id,name)
      self.college_name = college_name
    def display_college_student(self):
      print("College:", self.college_name)
      
AI= CollegeStudent("Rak", "22AD047", "cricket", "MITT")
AI.display_college_student()
AI.display_sports_player()
AI.display_student()
AI.display_person()
