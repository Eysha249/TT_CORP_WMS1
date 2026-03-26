import datetime
from Domain.Projectstatus import ProjectStatus

class Project:
    def __init__(self, name, description, status:ProjectStatus):
        self.name = name   
        self.desription = description
        self.status = status
        self.createdAt = datetime.datetime.now
        
