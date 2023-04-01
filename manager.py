from employee import Employee


class Manager(Employee):

    def __init__(self, name, password) -> None:
        super().__init__(name, password)
        self._is_admin = True