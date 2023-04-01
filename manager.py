from employee import Employee


class Manager(Employee):

    def __init__(self) -> None:
        super().__init__()
        self._is_admin = True