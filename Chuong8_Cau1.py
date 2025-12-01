import tkinter as tk
from tkinter import messagebox
import sys


def solve_equation():
    """Hàm xử lý logic giải phương trình bậc nhất ax + b = 0"""
    try:
        # Lấy giá trị hệ số a và b từ các ô nhập liệu (Entry widgets)
        a = float(entry_a.get())
        b = float(entry_b.get())

        ket_qua = ""

        # Giải phương trình bậc nhất: ax + b = 0  =>  ax = -b

        if a == 0:
            if b == 0:
                # 0x + 0 = 0 => Vô số nghiệm
                ket_qua = "Phương trình Vô số nghiệm (0x + 0 = 0)"
            else:
                # 0x + b = 0 (với b khác 0) => Vô nghiệm
                ket_qua = "Phương trình Vô nghiệm (0x + b = 0, b ≠ 0)"
        else:
            # Phương trình có 1 nghiệm duy nhất: x = -b / a
            x = -b / a
            # Định dạng kết quả làm tròn 2 chữ số thập phân
            ket_qua = f"x = {x:.2f}"

    except ValueError:
        # Xử lý trường hợp người dùng nhập không phải là số
        ket_qua = "Lỗi: Vui lòng nhập số hợp lệ!"
        messagebox.showerror(
            "Lỗi Nhập Liệu", "Hệ số a và b phải là giá trị số.")

    # Cập nhật kết quả vào Label hiển thị
    result_label.config(text=f"Kết quả: {ket_qua}")


def clear_fields():
    """Hàm xóa nội dung của các ô nhập liệu"""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Kết quả: ")
    entry_a.focus()  # Đặt con trỏ chuột về ô nhập a


def exit_app():
    """Hàm thoát ứng dụng"""
    # Sử dụng sys.exit(0) hoặc root.destroy()
    sys.exit(0)

# --- Cấu Hình Giao Diện Chính (Root Window) ---


# Tạo cửa sổ chính
root = tk.Tk()
root.title("PTB1")  # Đặt tiêu đề cửa sổ

# Thiết lập padding và căn giữa nội dung
root.geometry("300x250")
root.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

# Tiêu đề lớn
title_label = tk.Label(root, text="Phương Trình Bậc 1",
                       fg="red", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# --- Khung Chứa Các Ô Nhập Liệu ---
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=5)

# Hệ số a
tk.Label(input_frame, text="Hệ số a:").grid(
    row=0, column=0, sticky="w", pady=5)
entry_a = tk.Entry(input_frame)
entry_a.grid(row=0, column=1, padx=5, pady=5)
# Đặt giá trị mặc định theo hình mẫu
entry_a.insert(0, "5")

# Hệ số b
tk.Label(input_frame, text="Hệ số b:").grid(
    row=1, column=0, sticky="w", pady=5)
entry_b = tk.Entry(input_frame)
entry_b.grid(row=1, column=1, padx=5, pady=5)
# Đặt giá trị mặc định theo hình mẫu
entry_b.insert(0, "9")

# --- Khung Chứa Các Nút Bấm ---
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Nút "Giải"
solve_button = tk.Button(button_frame, text="Giải", command=solve_equation)
solve_button.pack(side=tk.LEFT, padx=5)

# Nút "Tiếp" (Thực hiện chức năng xóa nội dung)
clear_button = tk.Button(button_frame, text="Tiếp", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Nút "Thoát"
exit_button = tk.Button(button_frame, text="Thoát", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=5)

# --- Hiển Thị Kết Quả ---
# Label hiển thị kết quả. Bắt đầu với kết quả mẫu: x = -1.8
result_label = tk.Label(root, text="Kết quả: x = -1.8", font=("Arial", 10))
result_label.pack(pady=10)


# Chạy vòng lặp sự kiện chính của tkinter
root.mainloop()
