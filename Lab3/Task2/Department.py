class Department :
  def __init__ (self, name , employees) :
    self.name = name
    self.employees = employees

  def countEmployees (self , year) :
    count = 0
    for e in self.employees :
      if e.birhtYear == year :
        count += 1
    return count
  def findOldestEmployee (self) :
    oldestEmployee = self.employees[0]
    for e in self.employees :
      if e.birhtYear < oldestEmployee.birhtYear :
        oldestEmployee = e
    return oldestEmployee
  def statByBirthYear (self) :
    dict = {}
    for e in self.employees :
      if e.birhtYear in dict :
        dict[e.birhtYear] += 1
      else :
        dict[e.birhtYear] = 1
    return dict