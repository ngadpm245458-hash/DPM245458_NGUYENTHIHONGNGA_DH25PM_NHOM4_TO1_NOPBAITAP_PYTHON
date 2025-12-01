import tkinter as tk
from tkinter import messagebox


def cau_8_do_f_sang_do_c():
    def do_f_sang_do_c(entry_f, ket_qua_c_var):
        """Công thức: C = (F - 32) * 5/9"""
        try:
            do_f = float(entry_f.get())
            do_c = (do_f - 32) * 5 / 9

            ket_qua_c_var.set(f"{do_c:.2f}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập độ F hợp lệ.")

    root = tk.Tk()
    root.title("Chuyển độ F -> độ C")

    ket_qua_c_var = tk.StringVar(value="Độ C ở đây")

    # Input
    tk.Label(root, text="Nhập độ F:").grid(
        row=1, column=0, sticky='e', padx=10, pady=5)
    entry_f = tk.Entry(root, width=15)
    entry_f.grid(row=1, column=1, padx=10, pady=5)
    entry_f.insert(0, "350")

    tk.Button(root, text="Chuyển", command=lambda: do_f_sang_do_c(
        entry_f, ket_qua_c_var)).grid(row=1, column=2, padx=10, pady=5)

    # Output
    tk.Label(root, text="Độ C:").grid(
        row=2, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=ket_qua_c_var, relief='sunken',
             width=15, bg='yellow').grid(row=2, column=1, padx=10, pady=5)

    # root.mainloop()
# cau_8_do_f_sang_do_c()
