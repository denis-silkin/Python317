

class PayrollSystem:
    def calculate(self, employees):
        print('Расчет заработной платы')
        print('=' * 50)
        for employee in employees:
            print(f'Заработная плата: {employee.kod} - {employee.name}')
            print(f'- Проверить Сумму: {employee.calculate_payroll()}')
            print()
