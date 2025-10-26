import tkinter as tk
def change_font():
    label.config(font=("Arial", 18, "bold"))
root = tk.Tk()
label = tk.Label(root, text="Hello, World!", font=("Helvetica", 14))
label.pack()
button = tk.Button(root, text="Change Font", command=change_font)
button.pack()
root.mainloop()
