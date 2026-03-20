import tkinter as tk    
root = tk.Tk()
#Setting window properties
root.title("TT Corp Work Management System") #title of window
root.configure(background="white") #window background colour
root.minsize(200, 200) # 
root.maxsize(500, 500) # 
root.geometry("800x500") # window size

#create labels for WMS
tk.Label(root, text = "Welcome to TT Corp Work Management System").pack() #creats label for welcome greeting

#Display an image
image = tk.PhotoImage(file="data/assets/TT Corp Logo Image.png") # Import image from data/assets

logo_label = tk.Label(root,image=image) #Place image inside a label
logo_label.pack()


root.mainloop()