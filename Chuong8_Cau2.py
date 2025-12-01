import tkinter as tk
from tkinter import messagebox
import math
import sys


def solve_quadratic():
    """Hàm xử lý logic giải phương trình bậc hai ax^2 + bx + c = 0"""
    try:
        # Lấy giá trị hệ số a, b, và c từ các ô nhập liệu
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        ket_qua = ""

        if a == 0:
            # Nếu a = 0, chuyển thành phương trình bậc nhất: bx + c = 0
            if b == 0:
                if c == 0:
                    # 0x + 0 = 0 => Vô số nghiệm
                    ket_qua = "Phương trình Vô số nghiệm (a=0, b=0, c=0)"
                else:
                    # 0x + c = 0 (với c khác 0) => Vô nghiệm
                    ket_qua = "Phương trình Vô nghiệm (a=0, b=0, c≠0)"
            else:
                # bx + c = 0 có nghiệm duy nhất: x = -c / b
                x = -c / b
                ket_qua = f"x = {x:.2f}"
        else:
            # Giải phương trình bậc hai
            delta = b**2 - 4*a*c

            if delta < 0:
                # Delta âm => Vô nghiệm thực
                ket_qua = "Phương trình Vô nghiệm thực (Δ < 0)"
            elif delta == 0:
                # Delta bằng 0 => Nghiệm kép: x1 = x2 = -b / (2a)
                x = -b / (2*a)
                ket_qua = f"x1 = x2 = {x:.2f}"
            else:
                # Delta dương => Hai nghiệm phân biệt
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                ket_qua = f"x1 = {x1:.2f}; x2 = {x2:.2f}"

    except ValueError:
        # Xử lý trường hợp người dùng nhập không phải là số
        ket_qua = "Lỗi: Vui lòng nhập số hợp lệ!"
        messagebox.showerror(
            "Lỗi Nhập Liệu", "Hệ số a, b và c phải là giá trị số.")

    # Cập nhật kết quả vào Label hiển thị
    result_label.config(text=f"Kết quả: {ket_qua}")


def clear_fields():
    """Hàm xóa nội dung của các ô nhập liệu"""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_label.config(text="Kết quả: ")
    entry_a.focus()  # Đặt con trỏ chuột về ô nhập a


def exit_app():
    """Hàm thoát ứng dụng"""
    sys.exit(0)

# --- Cấu Hình Giao Diện Chính (Root Window) ---


# Tạo cửa sổ chính
root = tk.Tk()
root.title("PTB2")  # Đặt tiêu đề cửa sổ
root.geometry("300x300")
root.resizable(False, False)

# Tiêu đề lớn
title_label = tk.Label(root, text="Phương Trình Bậc 2",
                       fg="blue", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# --- Khung Chứa Các Ô Nhập Liệu ---
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=5)

# Hệ số a
tk.Label(input_frame, text="Hệ số a:").grid(
    row=0, column=0, sticky="w", pady=5)
entry_a = tk.Entry(input_frame)
entry_a.grid(row=0, column=1, padx=5, pady=5)
entry_a.insert(0, "4")  # Giá trị mẫu theo hình ảnh

# Hệ số b
tk.Label(input_frame, text="Hệ số b:").grid(
    row=1, column=0, sticky="w", pady=5)
entry_b = tk.Entry(input_frame)
entry_b.grid(row=1, column=1, padx=5, pady=5)
entry_b.insert(0, "2")  # Giá trị mẫu theo hình ảnh

# Hệ số c
tk.Label(input_frame, text="Hệ số c:").grid(
    row=2, column=0, sticky="w", pady=5)
entry_c = tk.Entry(input_frame)
entry_c.grid(row=2, column=1, padx=5, pady=5)
entry_c.insert(0, "-6")  # Giá trị mẫu theo hình ảnh

# --- Khung Chứa Các Nút Bấm ---
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Nút "Giải"
solve_button = tk.Button(button_frame, text="Giải", command=solve_quadratic)
solve_button.pack(side=tk.LEFT, padx=5)

# Nút "Tiếp" (Thực hiện chức năng xóa nội dung)
clear_button = tk.Button(button_frame, text="Tiếp", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Nút "Thoát"
exit_button = tk.Button(button_frame, text="Thoát", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=5)

# --- Hiển Thị Kết Quả ---
# Label hiển thị kết quả. Bắt đầu với kết quả mẫu: x1=-1.5; x2=1.0
result_label = tk.Label(
    root, text="Kết quả: x1=-1.5; x2=1.0", font=("Arial", 10))
result_label.pack(pady=10)


# Chạy vòng lặp sự kiện chính của tkinter
root.mainloop()
