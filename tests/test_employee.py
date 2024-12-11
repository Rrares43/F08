import pytest
import employee

@pytest.fixture(autouse=True)
def reset():
    employee.Employee.empCount = 0 #asta am facut ca sa mi se reseteze countul la fiecare testare
    employee.Manager.mgrCount = 0

def test_display_employee():
    emp = employee.Manager("Andrei", "3500", "Vanzare")
    assert emp.name == "Andrei"
    assert emp.salary == "3500"
    assert emp._department == "F08_Vanzare"
    
    emp2 = employee.Manager("Super Mario", "10000", "Instalatii")
    assert emp2.name == "Super Mario"
    assert emp2.salary == "10000"
    assert emp2._department == "F08_Instalatii"

def test_emp_count():
    emp1 = employee.Employee("Dana", "4900")
    empdoi = employee.Employee("Erd", "4500")
    emptrei = employee.Employee("Gigel", "5400")
    assert employee.Employee.empCount == 3
    
    
def test_mgr_count():
    emp1 = employee.Manager("Shana", "4300", "Stocare")
    empdoi = employee.Manager("Radu", "4000", "Comenzi")
    assert employee.Manager.mgrCount == 2
    