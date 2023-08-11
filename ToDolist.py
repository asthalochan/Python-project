import tkinter as tk
from tkinter import messagebox

class NeonToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg="#222222")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.create_task_entry()
        self.create_add_button()
        self.create_task_listbox()
        self.create_remove_button()

    def create_task_entry(self):
        self.task_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12), bg="#444444", fg="#00FF00", insertbackground="#00FF00")
        self.task_entry.pack(pady=10)

    def create_add_button(self):
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#00FF00", font=("Helvetica", 10, "bold"))
        self.add_button.pack()

    def create_task_listbox(self):
        self.task_listbox = tk.Listbox(self.root, width=30, font=("Helvetica", 12), selectbackground="#00FF00", selectmode=tk.SINGLE, bg="#444444", fg="#00FF00")
        self.task_listbox.pack(pady=10)

    def create_remove_button(self):
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="#FF00FF", font=("Helvetica", 10, "bold"))
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = NeonToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
