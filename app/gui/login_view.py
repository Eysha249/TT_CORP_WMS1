import tkinter as tk # import Tkinter GUI library
from tkinter import messagebox # import pop up dialog box to show error messages, success messages and alerts
from app.services.auth_service import login_user  # import customer login function from login_user it will check username and password in SQLite database

class LoginView: # creating a class for loginview
    def __init__(self, root, login_success_callback): #root to main application window allows navigation to dashboard after login
        self.root = root # Saved value
        self.login_success_callback = login_success_callback #saved value

        self.root.title("TT Corp Login") # login window title
        self.root.geometry ("400x300") # size of window width and height

        self.create_widgets() # builds screen layout

        # create text label

def create_widgets(self):
    title_label = tk.Label(
        self.root,
        text = "TT Corp Work Management System",
        front=("Arial", 14, "bold")
    )
    title_label.pack(pady=20) #vertical spacing for widget on screen

