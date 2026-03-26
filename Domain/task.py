from Domain.Taskstatus import Taskstatus

class task:
    def __init__(self, name, description, status: Taskstatus, estimatedhours, assignedTo):
        self.name = name
        self.description = description
        self.status = status
        self.estimatedhours = estimatedhours
        self.assignedTo = assignedTo
        