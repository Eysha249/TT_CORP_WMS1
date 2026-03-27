import tkinter as tk

from App import Navigation

class AuthenticationPage:
    def __init__(self, root:tk, navigator: Navigation):
      print("Initializing Auth page")
      self.root = root
      self.navigator = navigator
      pass

    def render(self):
      print("Rendering Auth page")
      self.root.title("Tk Example")
      self.root.configure(background="green")
      self.root.minsize(200, 200)
      self.root.maxsize(500, 500)
      self.button = tk.Button(self.root, text="Dashboard", command=lambda: self.navigator.navigate_to("dashboard"))
      self.button.pack()
      

    def destroy(self):
       self.button.destroy()