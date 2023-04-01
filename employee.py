class Employee:

    def __init__(self) -> None:
        self.name = None
        self._password = None

    def create(self, name, password):
        self.name = name
        self._password = password
        return "Usuário criado com sucesso!"

    def authenticate(self, name, password):
        return self.name == name and self._password == password