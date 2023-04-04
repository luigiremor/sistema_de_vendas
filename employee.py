class Employee:

    def __init__(self, name, password, is_admin=False) -> None:
        self.name = name
        self._password = password
        self._is_admin = is_admin

    def get_name(self):
        return self.name
    
    def _get_password(self):
        return self._password
    
    def _get_is_admin(self):
        return self._is_admin
    
    def set_name(self, name):
        self.name = name

    def _set_password(self, password):
        self._password = password
    
    def _set_is_admin(self, is_admin):
        self._is_admin = is_admin

    def authenticate(self, name, password):
        return self.name == name and self._password == password
    
    def __str__(self) -> str:
        return f"Nome: {self.name} - Senha: {self._password} - Admin: {self._is_admin}"
