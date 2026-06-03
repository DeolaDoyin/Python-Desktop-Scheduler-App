import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os  

DATA_FILE = 'events.json'

# Load & Save Functions
def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=2)

# GUI App Class
class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Scheduler")

        self.events = load_events()

        # Input Fields
        tk.Label(root, text="Event Title:").pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack()

        tk.Label(root, text="Date & Time (YYYY-MM-DD HH:MM):").pack()
        self.datetime_entry = tk.Entry(root, width=40)
        self.datetime_entry.pack()

        # Buttons
        tk.Button(root, text="Add Event", command=self.add_event).pack(pady=5)
        tk.Button(root, text="Delete Selected", command=self.delete_event).pack(pady=5)

        # Event List
        self.event_listbox = tk.Listbox(root, width=60, height=10)
        self.event_listbox.pack()
        self.update_event_list()

    def add_event(self):
        title = self.title_entry.get()
        dt_str = self.datetime_entry.get()
        try:
            datetime.strptime(dt_str, "%Y-%m-%d %H:%M")  # validate format
            self.events.append({"title": title, "datetime": dt_str})
            self.events.sort(key=lambda e: e["datetime"])  # keep sorted
            save_events(self.events)
            self.update_event_list()
            self.title_entry.delete(0, tk.END)
            self.datetime_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date", "Use format YYYY-MM-DD HH:MM")

    def delete_event(self):
        selection = self.event_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Select an event to delete.")
            return
        index = selection[0]
        del self.events[index]
        save_events(self.events)
        self.update_event_list()

    def update_event_list(self):
        self.event_listbox.delete(0, tk.END)
        for e in self.events:
            self.event_listbox.insert(tk.END, f"{e['datetime']} - {e['title']}")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()
