import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

def add_task(event=None):
    task = simpledialog.askstring("Add task", "Enter a task:")
    if task:
        tasks.insert(tk.END, task)

def delete_task(event):
    if tasks.curselection():
        tasks.delete(tasks.curselection())

def exit_program():
    root.quit()

# Create window
root = tk.Tk()
root.title("Fox-ToDo")

# Load and show image
image = Image.open("C:/Users/abiga/OneDrive/Desktop/CSD-325/Module 10/445.png")
image = image.resize((120, 120), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=5)


list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# Task Listbox
tasks = tk.Listbox(list_frame, height=10, width=50)
tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks.yview)


# Label with instructions
label = tk.Label(root, text="Double-click to add task. Right-click to delete.")
label.pack()

# Menu
menu = tk.Menu(root, bg="#007ACC", fg="white")
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0, bg="#007ACC", fg="white")
file_menu.add_command(label="Add Task", command=add_task)
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)

# Bindings
tasks.bind("<Double-Button-1>", add_task)
tasks.bind("<Button-3>", delete_task)

root.mainloop()
