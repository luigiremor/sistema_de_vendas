class Employee:

    def __init__(self, name, password) -> None:
        self.name = name
        self._password = password

    def authenticate(self, name, password):
        return self.name == name and self._password == password