from ..homework import employee


class HourlyEmployee(employee.Employee):
    """Сотрудники с почасовой оплатой"""
    def __init__(self, kod, name, hours_worked, hours_rate):
        super().__init__(kod, name)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate

