import tkinter as tk
from tkinter import messagebox


def cau_7_duong_am_lich():
    def duong_lich_sang_am_lich(entry_duong, nam_am_var, nam_tuoi_var):
        """Tính Can Chi (Âm lịch) dựa trên năm Dương lịch (sử dụng công thức tính Can Chi đơn giản)."""
        try:
            nam_duong = int(entry_duong.get())

            # Mảng Can (10) và Chi (12)
            Can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp",
                   "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
            Chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu",
                   "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

            # Công thức tính Can: (Năm + 6) % 10. Canh = 0
            # Công thức tính Chi: (Năm + 8) % 12. Thân = 0
            # Đây là công thức đơn giản, có thể sai lệch 1 Can Chi so với lịch chuẩn.
            can_index = (nam_duong + 6) % 10
            chi_index = (nam_duong + 8) % 12

            nam_am = f"{Can[can_index]} {Chi[chi_index]}"

            nam_am_var.set(nam_am)
            nam_tuoi_var.set(Chi[chi_index])

        except ValueError:
            messagebox.showerror(
                "Lỗi", "Vui lòng nhập năm dương lịch hợp lệ (số nguyên).")

    root = tk.Tk()
    root.title("Dương Lịch -> Âm Lịch")

    nam_am_var = tk.StringVar(value="Nhâm Tuất")
    nam_tuoi_var = tk.StringVar(value="Tuất")

    # Input
    tk.Label(root, text="Nhập năm dương:").grid(
        row=1, column=0, sticky='e', padx=10, pady=5)
    entry_duong = tk.Entry(root, width=15)
    entry_duong.grid(row=1, column=1, padx=10, pady=5)
    entry_duong.insert(0, "1982")

    tk.Button(root, text="Chuyển", command=lambda: duong_lich_sang_am_lich(
        entry_duong, nam_am_var, nam_tuoi_var)).grid(row=1, column=2, padx=10, pady=5)

    # Output
    tk.Label(root, text="Năm âm:").grid(
        row=2, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=nam_am_var, relief='sunken', width=15,
             bg='yellow').grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Năm tuổi:").grid(
        row=3, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=nam_tuoi_var, relief='sunken',
             width=15, bg='yellow').grid(row=3, column=1, padx=10, pady=5)

    # root.mainloop()
# cau_7_duong_am_lich()
