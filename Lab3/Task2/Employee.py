class Employee :
  def __init__ (self, id , name , birhtYear , salaryRate) :
    self.id = id
    self.name = name
    self.birhtYear = birhtYear
    self.salaryRate = salaryRate
  def __str__ (self) :
    return f"id : {self.id} , name : {self.name} , birhtYear : {self.birhtYear} , salaryRate : {self.salaryRate}"