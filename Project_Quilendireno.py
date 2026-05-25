# Design and implement a small restaurant reservation program that allows customers to book, view, and manage dining reservations. The system should calculate reservation costs based on different rates for adults and children, generate reports, and handle errors gracefully.

# System Features:
# 1. System Menu
# -View all Reservations
# -Make Reservation
# -Delete Reservation
# -Generate Report
# -Exit
# 2. Reservation Details
# -Customer name
# -Date and time of reservation
# -Number of adults (PHP 500/head)
# -Number of children (PHP 300/head)
# 3. Reports
# -List of all reservations with subtotals
# -Total number of adults and children
# -Grand total cost of all reservations
# 4. Technical Requirements
# -Apply Object-Oriented Programming (OOP) principles
# -Store reservation data in a text file
# -Implement exception handling for invalid inputs (e.g., letters instead of numbers, zero values, missing data)

"""
ITL224-18 Laboratory Project
Restaurant Dining Reservation System (GUI Version)
"""
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Constants
ADULT_RATE = 500
CHILD_RATE = 300
DATA_FILE = "reservations.txt"

# Business Logic Model Layer
class Reservation:
    def __init__(self, name: str, date: str, time_str: str, adults: int, children: int):
        self.name = name
        self.date = date
        self.time = time_str
        self.adults = adults
        self.children = children

    @property
    def subtotal(self) -> float:
        return (self.adults * ADULT_RATE) + (self.children * CHILD_RATE)

    def to_file_line(self) -> str:
        return f"{self.name}|{self.date}|{self.time}|{self.adults}|{self.children}\n"

    @classmethod
    def from_file_line(cls, line: str):
        parts = line.strip().split("|")
        if len(parts) != 5:
            raise ValueError("Corrupted data line.")
        name, date, time_str, adults, children = parts
        return cls(name, date, time_str, int(adults), int(children))


# Graphical User Interface Layer
class RestaurantSystemGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Restaurant Dining Reservation System")
        self.window.geometry("850x600")
        self.window.resizable(False, False)

        self.reservations = []
        self._load_from_file()

        self._setup_styles()
        self._create_widgets()
        self.refresh_table()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=25, font=("Arial", 9))

    def _create_widgets(self):
        # Top Title Banner
        title_frame = tk.Frame(self.window, bg="#1e293b", padding=10)
        title_frame.pack(fill="x", side="top")

        title_lbl = tk.Label(
            title_frame,
            text="RESTAURANT DINING RESERVATION SYSTEM",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1e293b"
        )
        title_lbl.pack()

        # Left Column: Data Form Entry
        form_frame = tk.LabelFrame(self.window, text=" Reservation Details ", font=("Arial", 10, "bold"), padx=15, pady=15)
        form_frame.place(x=20, y=70, width=280, height=340)

        tk.Label(form_frame, text="Customer Name:", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        self.ent_name = ttk.Entry(form_frame, font=("Arial", 10))
        self.ent_name.pack(fill="x", pady=2)

        tk.Label(form_frame, text="Reservation Date:", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        self.ent_date = ttk.Entry(form_frame, font=("Arial", 10))
        self.ent_date.insert(0, "Nov 10, 2024")
        self.ent_date.pack(fill="x", pady=2)

        tk.Label(form_frame, text="Reservation Time:", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        self.ent_time = ttk.Entry(form_frame, font=("Arial", 10))
        self.ent_time.insert(0, "12:00 pm")
        self.ent_time.pack(fill="x", pady=2)

        tk.Label(form_frame, text="Number of Adults (₱500/head):", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        self.ent_adults = ttk.Entry(form_frame, font=("Arial", 10))
        self.ent_adults.pack(fill="x", pady=2)

        tk.Label(form_frame, text="Number of Children (₱300/head):", font=("Arial", 9, "bold")).pack(anchor="w", pady=(5,0))
        self.ent_children = ttk.Entry(form_frame, font=("Arial", 10))
        self.ent_children.pack(fill="x", pady=2)

        # Action Buttons Area Below Form
        btn_frame = tk.Frame(self.window)
        btn_frame.place(x=20, y=425, width=280, height=150)

        btn_add = tk.Button(btn_frame, text="Make Reservation", bg="#10b981", fg="white", font=("Arial", 10, "bold"), command=self.make_reservation)
        btn_add.pack(fill="x", pady=4)

        btn_del = tk.Button(btn_frame, text="Delete Selected Reservation", bg="#ef4444", fg="white", font=("Arial", 10, "bold"), command=self.delete_reservation)
        btn_del.pack(fill="x", pady=4)

        btn_report = tk.Button(btn_frame, text="Generate Financial Report", bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), command=self.generate_report)
        btn_report.pack(fill="x", pady=4)

        btn_exit = tk.Button(btn_frame, text="Exit System", bg="#64748b", fg="white", font=("Arial", 10, "bold"), command=self.exit_system)
        btn_exit.pack(fill="x", pady=4)

        # Right Column: Data View Display Tree
        table_frame = tk.LabelFrame(self.window, text=" Current Active Bookings ", font=("Arial", 10, "bold"), padx=5, pady=5)
        table_frame.place(x=320, y=70, width=510, height=505)

        columns = ("id", "date", "time", "name", "adults", "children", "subtotal")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("id", text="#")
        self.tree.heading("date", text="Date")
        self.tree.heading("time", text="Time")
        self.tree.heading("name", text="Name")
        self.tree.heading("adults", text="Adults")
        self.tree.heading("children", text="Children")
        self.tree.heading("subtotal", text="Subtotal")

        self.tree.column("id", width=30, anchor="center")
        self.tree.column("date", width=95, anchor="center")
        self.tree.column("time", width=75, anchor="center")
        self.tree.column("name", width=130, anchor="w")
        self.tree.column("adults", width=50, anchor="center")
        self.tree.column("children", width=60, anchor="center")
        self.tree.column("subtotal", width=65, anchor="e")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Data Access Logic File Operations
    def _load_from_file(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r") as f:
                for line in f:
                    if line.strip():
                        try:
                            self.reservations.append(Reservation.from_file_line(line))
                        except ValueError:
                            pass
        except OSError as e:
            messagebox.showwarning("File Read Error", f"Could not read reservation data: {e}")

    def _save_to_file(self):
        try:
            with open(DATA_FILE, "w") as f:
                for r in self.reservations:
                    f.write(r.to_file_line())
        except OSError as e:
            messagebox.showerror("File Save Error", f"Could not save reservation data: {e}")

    #  Interactive Features & Control Mapping
    def refresh_table(self):
        # Clear existing data items out of table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Repopulate current lists array onto screen grid matrix
        for index, r in enumerate(self.reservations, start=1):
            self.tree.insert("", "end", values=(
                index,
                r.date,
                r.time,
                r.name,
                r.adults,
                r.children,
                f"₱{r.subtotal:,.2f}"
            ))

    def make_reservation(self):
        # UI Validation Checks
        name = self.ent_name.get().strip()
        date = self.ent_date.get().strip()
        time_str = self.ent_time.get().strip()
        adults_raw = self.ent_adults.get().strip()
        children_raw = self.ent_children.get().strip()

        # Input Error Handling Exception States
        if not name or not date or not time_str or not adults_raw or not children_raw:
            messagebox.showerror("Input Error", "All entry fields must be filled out.")
            return

        try:
            adults = int(adults_raw)
            children = int(children_raw)
        except ValueError:
            messagebox.showerror("Data Type Error", "Adults and Children values must be whole numeric integers.")
            return

        if adults < 0 or children < 0:
            messagebox.showerror("Value Error", "Head counts cannot accept negative quantities.")
            return
        if adults == 0:
            messagebox.showerror("Value Error", "Bookings require at least 1 primary Adult account registration.")
            return

        # Commit Operations
        new_res = Reservation(name, date, time_str, adults, children)
        self.reservations.append(new_res)
        self._save_to_file()
        self.refresh_table()

        # Confirm and Reset Fields
        messagebox.showinfo("Success", f"Reservation Saved!\nSubtotal: PHP {new_res.subtotal:,.2f}")
        self.ent_name.delete(0, tk.END)
        self.ent_adults.delete(0, tk.END)
        self.ent_children.delete(0, tk.END)

    def delete_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Missing", "Please click a row on the right table to select a record to delete.")
            return

        # Confirm before actioning removal
        item_values = self.tree.item(selected_item, "values")
        res_index = int(item_values[0]) - 1 # Get ID Column counter array position
        cust_name = item_values[3]

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to remove row reservation #{res_index + 1} for '{cust_name}'?")
        if confirm:
            self.reservations.pop(res_index)
            self._save_to_file()
            self.refresh_table()
