from Domain.user import User

class ProjectMember:
    def __init__(self, user: User, project):
        self.user = user
        self.project = project