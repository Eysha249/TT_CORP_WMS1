import tkinter as tk # import Tkinter GUI library
from tkinter import messagebox # import pop up dialog box to show error messages, success messages and alerts
from app.services.auth_service import login_user  # import customer login function from login_user it will check username and password in SQLite database

class LoginView: # creating a class for loginview
    def __init__(self, root, login_success_callback):
        self.root = root
        self.login_success_callback = login_success_callback

        self.root.title("TT Corp Login")
        self.root.geometry ("400x300")

        self.create_widgets()


