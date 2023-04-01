from random import randint
from employee import Employee

class Cashier(Employee):
    def __init__(self) -> None:
        super().__init__()
        self._matricula = self._generate_matricula()

    def _generate_matricula(self):
        return randint(1, 100)
