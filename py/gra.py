# # Import tkinter
# import tkinter as tk
# # Create window
# root = tk.Tk()
# # Set window title
# root.title("Hello World GUI")
# # Set window size
# root.geometry("1260x200")
# # Create label with text
# label = tk.Label(root, text="Hello, World!")
# # Add label to window
# label.pack()
# # Start the GUI loop
# root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Gui application")
root.geometry("500x300")
label = tk.Label(root,text="Hurray Hurray")
label.pack()
root.mainloop()