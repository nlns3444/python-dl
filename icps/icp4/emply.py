#create a class named Employee

class Employee:
    employee_empCount = 0
    totalsal = 0

    #initialize the attributes
    def __init__(self, name, family, department, salary):
        self.name = name
        self.family = family
        self.department = department
        self.salary = salary
        Employee.totalsal += salary
        Employee.employee_empCount  += 1


    def fixed_salary(self):
        return self.salary

class Full_time_employee(Employee):
    def __init__(self, name, family, department, salary):
        super().__init__(name, family, department, salary)


    def full_time_employee_avg_sal(self):

        avg_salary = Employee.totalsal / Employee.employee_empCount
        print (avg_salary)

    def details(self):
        print(self.name, self.family,self.department,self.salary)

    def cal_Employees(self):
        print(Employee.employee_empCount)

emp1 = Full_time_employee("John","SE","AI", 20000)
emp2 = Full_time_employee("sid", "AM","HR",5000)

print("Average salary of employee 1 is: ", emp1.full_time_employee_avg_sal())
print("Average salary of employee 2 is: ", emp2.full_time_employee_avg_sal())
print("Total number of employees in an organization: ", emp1.employee_empCount)


emp1.details()
emp2.details()
emp1.employee_empCount

