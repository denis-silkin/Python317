from dz_python.homework import salary_employee
from dz_python.homework import commission
from dz_python.homework import payroll
from dz_python.homework import hourly

salary_employee = salary_employee.SalaryEmployee(1, 'Валерий Задорожный', 1500)
hourly_employee = hourly.HourlyEmployee(2, 'Илья Кромин', 40, 15)
commission_employee = commission.CommissionEmployee(3, 'Николай Хорольский', 1000, 250)
payroll_system = payroll.PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee
])

