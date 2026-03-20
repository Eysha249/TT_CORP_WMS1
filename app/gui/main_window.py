import tkinter as tk #import tkinter

def run_app():
    root = tk.Tk()

    root.title('TT Corp Work Management System')
    root.configure(background="white")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("800x500")

    tk.label(
        root,
        text="welcome to TT Corp Work Management System",
        bg="white"
    ).pack(paddy=10)

    image = tk.PhotoImage(file="assets/tt_logo.png")

    logo_label = tk.Label(root, image=image, bg="white")
    logo_label.image = image
    logo_label.pack(pady=10)

    root.mainloop()
