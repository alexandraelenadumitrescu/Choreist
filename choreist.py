import tkinter as tk

def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

#configuram fereastra principala
root = tk.Tk()
root.title("Choreist")

#configuram iconita
icon = tk.PhotoImage(file='unnamed.png')
root.iconphoto(True, icon)




#intrare pentru adaugarea sarcinilor noi
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind('<Return>', add_task)#putem adauga task uri si cu enter


#buton adaugare sarcini
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)


#lista
listbox = tk.Listbox(root, width=45, height=15, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)


#buton stergere sarcini selectate
delete_button = tk.Button(root, text="Delete Selected Tasks", command=delete_task)
delete_button.pack(pady=5)


#root in loop
root.mainloop()
