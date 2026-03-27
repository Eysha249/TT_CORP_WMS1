import tkinter as tk

from App.Navigation import Navigation

root = tk.Tk()

navigator = Navigation(root)
root.geometry("300x300+50+50")
root.mainloop()