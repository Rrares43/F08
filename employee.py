class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgrCount = 0
    
    def __init__(self, name, salary, department = "F08"):
        super().__init__(name, salary)
        self._department = f"F08_{department}"
        Manager.mgrCount += 1
        
    def display_employee(self):
        X = int(len("Raducanu"))
        
        if X % 3 == 0:
            print(f"The manager is called:{self.name}")
        elif X % 3 == 1:
            print(f"The manager makes: {self.salary} dollars")
        elif X % 3 == 2:
            print(f"This is the manager of the {self._department} department")
        else:
            print("Nuh uh")
            
def main():
    Y = float(len("Rares Aurelian"))
    final_y = int(Y/3)
    angajati_manageri = []
    angajat_normal = Employee("Lenghel", "2800")
    
    for i in range(final_y):
        nume = input("Name:")
        salariu = int(input("Salary:"))
        departament = input("Departament:")
        manajer = Manager(nume, salariu, departament)
        angajati_manageri.append(manajer)
        
    for employee in angajati_manageri:
        employee.display_employee()
    
    angajat_normal.display_emp_count()
    angajati_manageri[0].display_emp_count()

   
if __name__ == "__main__":
    main()          

        
        
        
        