import datetime

from Domain.user import User

class Notification:
    def __init__(self, message: str, recipient: User):
        self.message = message
        self.recipient = recipient
        self.sentAt = datetime.datetime.now()
