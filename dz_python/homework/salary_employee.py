from ..homework import employee


class SalaryEmployee(employee.Employee):
    """Административные работники имеют фиксированную оплату"""
    def __init__(self, kod, name, weekly_salary):
        super().__init__(kod, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
