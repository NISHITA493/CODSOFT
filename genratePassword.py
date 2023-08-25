import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.task_entry = tk.Entry(root)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)

        self.task_entry.pack(padx=10, pady=5, fill=tk.X)
        self.add_button.pack(padx=10, pady=5, fill=tk.X)
        self.task_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        self.complete_button.pack(padx=10, pady=5, fill=tk.X)
        self.remove_button.pack(padx=10, pady=5, fill=tk.X)

        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = f.read().splitlines()
                self.update_task_listbox()
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            self.tasks[index] = "[Completed] " + task
            self.update_task_listbox()
            self.save_tasks()

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
