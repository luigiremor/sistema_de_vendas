from random import randint
from employee import Employee

class Cashier(Employee):
    def __init__(self, name, password) -> None:
        super().__init__(name, password)
        self._matricula = self._generate_matricula()

    def _generate_matricula(self):
        return randint(1, 100)
