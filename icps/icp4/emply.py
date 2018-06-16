#create a class named Employee

class Employee:
    employee_empCount = 0#give the employee  count as 0
    totalsal = 0#total count as well

    #initialize the attributes
    def __init__(self, name, family, department, salary):
        self.name = name
        self.family = family
        self.department = department
        self.salary = salary
        Employee.totalsal += salary
        Employee.employee_empCount  += 1


    def fixed_salary(self):#defined a function to take salary of the employee
        return self.salary

class Full_time_employee(Employee):#created another class named full time employee calling the constructor of the main class
    def __init__(self, name, family, department, salary):
        super().__init__(name, family, department, salary)#super class is defined cause to inherit from the parent class


    def full_time_employee_avg_sal(self):#defined a function to take the avg salary

        avg_salary = Employee.totalsal / Employee.employee_empCount
        print (avg_salary)

    def details(self):#this function takes the details of the user
        print(self.name, self.family,self.department,self.salary)

    def cal_Employees(self):#this function takes the count of the employee
        print(Employee.employee_empCount)

emp1 = Full_time_employee("John","SE","AI", 20000)
emp2 = Full_time_employee("sid", "AM","HR",5000)

print("Average salary of employee 1 is: ", emp1.full_time_employee_avg_sal())
print("Average salary of employee 2 is: ", emp2.full_time_employee_avg_sal())
print("Total number of employees in an organization: ", emp1.employee_empCount)


emp1.details()#calling emp1 with object
emp2.details()#calling emp2 with object
emp1.employee_empCount#gives the employee count

