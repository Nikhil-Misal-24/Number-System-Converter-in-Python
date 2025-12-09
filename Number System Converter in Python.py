import tkinter as tk
from tkinter import messagebox, ttk

# Convert number to decimal
def to_decimal(number, base):
    return int(number, base)

# Convert decimal to desired base
def from_decimal(number, base):
    return format(number, {
        2: 'b',
        8: 'o',
        10: 'd',
        16: 'X'
    }[base])

# Conversion logic
def convert_number():
    try:
        number = entry_number.get().upper()
        from_base = int(combo_from.get())
        to_base = int(combo_to.get())

        decimal_value = to_decimal(number, from_base)
        result = from_decimal(decimal_value, to_base)

        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
        entry_result.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Invalid number for selected base!")

# Clear fields
def clear_fields():
    entry_number.delete(0, tk.END)
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.config(state="readonly")


# ---------------- GUI ----------------

app = tk.Tk()
app.title("Number System Converter")
app.geometry("430x420")
app.configure(bg="#1e1e1e")

title = tk.Label(
    app, 
    text=" Number System Converter ",
    font=("Poppins", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=15)

frame = tk.Frame(app, bg="#1e1e1e")
frame.pack(pady=10)

# Number Input
tk.Label(frame, text="Enter Number:", font=("Poppins", 12), bg="#1e1e1e", fg="white").grid(row=0, column=0, pady=10)
entry_number = tk.Entry(frame, font=("Poppins", 12), width=25)
entry_number.grid(row=0, column=1, pady=10)

# Base Options
bases = [2, 8, 10, 16]

tk.Label(frame, text="From Base:", font=("Poppins", 12), bg="#1e1e1e", fg="white").grid(row=1, column=0, pady=10)
combo_from = ttk.Combobox(frame, values=bases, width=5, state="readonly")
combo_from.set(10)
combo_from.grid(row=1, column=1, sticky="w")

tk.Label(frame, text="To Base:", font=("Poppins", 12), bg="#1e1e1e", fg="white").grid(row=2, column=0, pady=10)
combo_to = ttk.Combobox(frame, values=bases, width=5, state="readonly")
combo_to.set(2)
combo_to.grid(row=2, column=1, sticky="w")

# Buttons
tk.Button(app, text="Convert", width=20, command=convert_number).pack(pady=10)
tk.Button(app, text="Clear", width=20, command=clear_fields).pack(pady=5)

# Result Field
tk.Label(app, text="Result:", font=("Poppins", 12), bg="#1e1e1e", fg="white").pack(pady=5)
entry_result = tk.Entry(app, font=("Poppins", 13), width=30, state="readonly")
entry_result.pack()

# Footer
footer = tk.Label(app, text="Made with by Nikhil Misal", font=("Poppins", 11), bg="#1e1e1e", fg="white")
footer.pack(side="bottom", pady=15)

app.mainloop()
