import tkinter as tk
from tkinter import messagebox


def cau_9_tinh_bmi():
    def phan_tich_tinh_trang(bmi):
        """Phân tích tình trạng sức khỏe theo tiêu chuẩn WHO."""
        if bmi < 18.5:
            return "Gầy (Thiếu cân)", "Có"
        elif bmi < 25.0:
            return "Bình thường", "Thấp"
        elif bmi < 30.0:
            return "Thừa cân", "Trung bình"
        else:
            return "Béo phì", "Cao"

    def tinh_bmi(entry_chieu_cao, entry_can_nang, bmi_var, tinh_trang_var, nguy_co_var):
        """Công thức BMI: Cân nặng (kg) / Chiều cao^2 (m^2)"""
        try:
            chieu_cao_cm = float(entry_chieu_cao.get())
            can_nang_kg = float(entry_can_nang.get())

            if chieu_cao_cm <= 0 or can_nang_kg <= 0:
                messagebox.showerror(
                    "Lỗi", "Chiều cao và Cân nặng phải lớn hơn 0.")
                return

            chieu_cao_m = chieu_cao_cm / 100.0
            bmi = can_nang_kg / (chieu_cao_m ** 2)

            tinh_trang, nguy_co = phan_tich_tinh_trang(bmi)

            bmi_var.set(f"{bmi:.2f}")
            tinh_trang_var.set(tinh_trang)
            nguy_co_var.set(nguy_co)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

    root = tk.Tk()
    root.title("Phần mềm tính BMI")

    bmi_var = tk.StringVar(value="X")
    tinh_trang_var = tk.StringVar(value="Đốt X")
    nguy_co_var = tk.StringVar(value="Đốt X")

    # Input Chiều cao
    tk.Label(root, text="Nhập chiều cao:").grid(
        row=0, column=0, sticky='e', padx=10, pady=5)
    entry_chieu_cao = tk.Entry(root, width=15)
    entry_chieu_cao.grid(row=0, column=1, padx=10, pady=5)
    entry_chieu_cao.insert(0, "172")

    # Input Cân nặng
    tk.Label(root, text="Nhập cân nặng:").grid(
        row=1, column=0, sticky='e', padx=10, pady=5)
    entry_can_nang = tk.Entry(root, width=15)
    entry_can_nang.grid(row=1, column=1, padx=10, pady=5)
    entry_can_nang.insert(0, "78")

    # Nút Tính BMI
    tk.Button(root, text="Tính BMI", width=15, bg='blue', fg='white', command=lambda: tinh_bmi(
        entry_chieu_cao, entry_can_nang, bmi_var, tinh_trang_var, nguy_co_var)).grid(row=2, column=1, padx=10, pady=10)

    # Output BMI
    tk.Label(root, text="BMI của bạn:").grid(
        row=3, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=bmi_var, relief='sunken', width=15,
             bg='yellow').grid(row=3, column=1, padx=10, pady=5)

    # Output Tình trạng
    tk.Label(root, text="Tình trạng của bạn:").grid(
        row=4, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=tinh_trang_var, relief='sunken',
             width=15, bg='yellow').grid(row=4, column=1, padx=10, pady=5)

    # Output Nguy cơ phát triển bệnh
    tk.Label(root, text="Nguy cơ phát triển bệnh:").grid(
        row=5, column=0, sticky='e', padx=10, pady=5)
    tk.Label(root, textvariable=nguy_co_var, relief='sunken', width=15,
             bg='yellow').grid(row=5, column=1, padx=10, pady=5)

    # Nút Thoát
    tk.Button(root, text="Thoát", width=15, command=root.destroy).grid(
        row=6, column=1, padx=10, pady=10)

    # root.mainloop()
# cau_9_tinh_bmi()
