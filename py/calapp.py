import tkinter as tk 
from tkinter import messagebox

def find_sum():

    num1= entry1.get()
    num2 = entry2.get()
    if num1.isdigit() and num2.isdigit() :
     result = int(num1) + int(num2)
     messagebox.showinfo("Result", f"Sum:{result}")
    else:
     messagebox.showerror("Error","Enter valid numbers")

root = tk.Tk()
root.title("Calculator App")

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# tk.button(root,text="Find Sum", command=Cal_app).pack(pady=10))


# root = tk.Tk()
# root.title("Calculator")
root.geometry("600x300")
# label =tk.Label(root,text="Welcome to the calculator app")
# label.pack()

# num1 =float(input("Enter a first number:"))
# num2 =float(input("Enter a second number;"))

# sum = num1 + num2

tk.Button(root,text="Find sum",command=find_sum).pack(pady=10)
 #button.pack()
root.mainloop()