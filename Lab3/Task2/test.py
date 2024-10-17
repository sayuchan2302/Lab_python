from Lab3.Task2.Department import Department
from Lab3.Task2.Employee import Employee

employee1 = Employee(1, "John Doe", 1990, 50000)
employee2 = Employee(2, "Jane Smith", 1985, 60000)
employee3 = Employee(3, "Robert Jones", 1995, 55000)
employee4 = Employee(4, "Mary Williams", 1980, 70000)
employee5 = Employee(5, "Michael Brown", 1992, 65000)
ems = [employee1, employee2, employee3, employee4, employee5]
department1 = Department("thinhsuy", ems)
print (department1.countEmployees (1990))
print (department1.findOldestEmployee())
print (department1.statByBirthYear())