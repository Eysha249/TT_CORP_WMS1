import tkinter as tk

from App import Navigation

class DashboardPage:
    def __init__(self, root:tk, navigator: Navigation):
      print("DashboardPage init")
      self.navigator = navigator
      self.root = root
      pass

    def render(self):
      print("DashboardPage render")
      self.root.title("Tk Example")
      self.root.configure(background="blue")
      self.root.minsize(200, 200)
      self.root.maxsize(500, 500)
      self.button = tk.Button(self.root, text="Login", command=lambda: self.navigator.navigate_to("login"))
      self.button.pack()
      

    def destroy(self):
       self.button.destroy()
      