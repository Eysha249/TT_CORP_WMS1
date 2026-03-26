import datetime 

class comments:
    def __init__(self, user, value:str,):
        self.user = user
        self.value = value
        self.createdAt = datetime.datetime.now