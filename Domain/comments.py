import datetime 
from Domain.Project import Project
from Domain.task import Task
class comments:
    def __init__(self, user,value:str,project:Project = null,task:Task = null):
        self.user = user
        self.value = value
        self.createdAt = datetime.datetime.now
        self.project = project
        self.task = task