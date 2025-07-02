import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        m1 = entry_m1.get()
        v1 = entry_v1.get()
        m2 = entry_m2.get()
        v2 = entry_v2.get()
        m1 = float(m1) if m1 != '' else None
        v1 = float(v1) if v1 != '' else None
        m2 = float(m2) if m2 != '' else None
        v2 = float(v2) if v2 != '' else Nonee
        
        if m1 is None and v1 and m2 and v2:
            m1 = (m2 * v2) / v1
            result.set(f"M1 = {m1:.4f} mol/L")

        elif v1 is None and m1 and m2 and v2:
            v1 = (m2 * v2) / m1
            result.set(f"V1 = {v1:.2f} mL")

        elif m2 is None and m1 and v1 and v2:
            m2 = (m1 * v1) / v2
            result.set(f"M2 = {m2:.4f} mol/L")

        elif v2 is None and m1 and v1 and m2:
            v2 = (m1 * v1) / m2
            result.set(f"V2 = {v2:.2f} mL")

        else:
            result.set("Please leave ONE box empty to calculate.")
    except:
        messagebox.showerror("Error", "Please enter numbers only.")

window = tk.Tk()
window.title("Molarity Calculator")

tk.Label(window, text="Enter 3 values. Leave 1 box empty to calculate it.").grid(row=0, columnspan=2, pady=10)


tk.Label(window, text="M1 (mol/L):").grid(row=1, column=0)
entry_m1 = tk.Entry(window)
entry_m1.grid(row=1, column=1)

tk.Label(window, text="V1 (mL):").grid(row=2, column=0)
entry_v1 = tk.Entry(window)
entry_v1.grid(row=2, column=1)

tk.Label(window, text="M2 (mol/L):").grid(row=3, column=0)
entry_m2 = tk.Entry(window)
entry_m2.grid(row=3, column=1)

tk.Label(window, text="V2 (mL):").grid(row=4, column=0)
entry_v2 = tk.Entry(window)
entry_v2.grid(row=4, column=1)

tk.Button(window, text="Calculate", command=calculate).grid(row=5, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(window, textvariable=result, fg="blue", font=("Arial", 12)).grid(row=6, columnspan=2)

window.mainloop()
