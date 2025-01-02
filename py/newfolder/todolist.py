import tkinter as tk

def add_task():
    task =entry.get()
    if task != "" :
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)

def on_key_press(event):
    if event.keysym == "Return":
        add_task()
def del_task():
    listbox.delete(tk.ANCHOR)
    


# listbox = tk.Listbox(root,)
# entry = tk.entry(root, width=30 )
# delete = tk.delete

root = tk.Tk()
root.title("Todo List App")

root.bind('<Return>', on_key_press)

entry = tk.Entry(root, width=30)
entry.pack()

# label = tk.Label(root, text="Welcome to the todo list App",)
# label.pack(pady=4)
add_button =tk.Button(root,text="Add task",command=add_task)
add_button.pack(pady=5)

 
del_button =tk.Button(root,text="Delete task",command=del_task)
del_button.pack(pady=5)

listbox=tk.Listbox(root)
listbox.pack(pady=10)

# tk.button(root,text="Add task",command=add_task(pady=20))
# tk.button(root,text="Del task"command=del_task(pady=10))
root.geometry("600x300")
root.mainloop()