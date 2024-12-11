import pytest
import employee

@pytest.fixture(autouse=True)
def reset():
    employee.Employee.empCount = 0

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
    emp1 = employee.Manager("Dana", "4900", "Stocare")
    empdoi = employee.Manager("Erd", "0", "Caritate")
    assert employee.Employee.empCount == 2
    