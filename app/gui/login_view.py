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

    #username label

    username_label = tk.Entry(self.root, text="Username")
    username_label.pack()
    
    #username entry box

    self.username_entry = tk.Entry(self.root, width=30)
    self.username_entry.pack.pack(pady=5)

    #password label
    
    password_label = tk.Label(self.root,text="password")
    password_label.pack()

   #password entry box
    self.password_entry = tk.Entry(self.root, width=30, show="*")
    self.password_entry.pack(pady=5)

    #create clickable botton

    login_button = tk.Button(
        self.root,
        text="Login",
        width=15,
        command=self.handle_login #runs function when the botton is clicked
    )

