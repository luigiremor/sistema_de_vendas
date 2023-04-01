class Employee:

    def __init__(self, name, password, is_admin=False) -> None:
        self.name = name
        self._password = password
        self._is_admin = is_admin

    def authenticate(self, name, password):
        return self.name == name and self._password == password