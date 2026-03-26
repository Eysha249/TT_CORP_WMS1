from enum import Enum

class Role(Enum):   
    superadmin = 1
    user = 2


class User:
    def __init__(self,fullname, username, email, password, role: Role = Role.user):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.role = role



