import tkinter as tk

def greet():
    label.config(text="Hello,Welcome to tkinter")
root = tk.Tk()
root.title("Interactive GUl")
label = tk.Label(root, text="Click the button to get greateed")
font=("Arial",14)
label.pack(pady=20)

button =tk.Button(root,text="Greet Me",command=greet)
button.pack(pady=10)

root.geometry("400x300")
root.mainloop()