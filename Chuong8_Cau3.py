import tkinter as tk
from tkinter import messagebox


def tinh_toan(phep_toan):
    """Xử lý các phép toán khi nhấn nút."""
    try:
        so_a = float(entry_a.get())
        so_b = float(entry_b.get())
        ket_qua = 0

        if phep_toan == 'cong':
            ket_qua = so_a + so_b
        elif phep_toan == 'tru':
            ket_qua = so_a - so_b
        elif phep_toan == 'nhan':
            ket_qua = so_a * so_b
        elif phep_toan == 'chia':
            if so_b == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                ket_qua_var.set("LỖI")
                return
            ket_qua = so_a / so_b

        # Xuất kết quả với 2 chữ số thập phân
        ket_qua_var.set(f"{ket_qua:.2f}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ vào cả hai ô.")
        ket_qua_var.set("LỖI")


# 1. Khởi tạo cửa sổ
root = tk.Tk()
root.title("Cộng trừ nhân chia")
root.geometry("300x250")  # Đặt kích thước cố định

# 2. Tiêu đề
label_title = tk.Label(root, text="Cộng trừ nhân chia",
                       font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=10)

# 3. Input cho số a
label_a = tk.Label(root, text="số a:")
label_a.grid(row=1, column=1, sticky='e', padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=2, padx=5, pady=5)
entry_a.insert(0, "6")  # Giá trị mặc định

# 4. Input cho số b
label_b = tk.Label(root, text="số b:")
label_b.grid(row=2, column=1, sticky='e', padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=2, padx=5, pady=5)
entry_b.insert(0, "7")  # Giá trị mặc định

# 5. Kết quả
label_kq = tk.Label(root, text="kết quả:")
label_kq.grid(row=3, column=1, sticky='e', padx=5, pady=5)
ket_qua_var = tk.StringVar(value="-1.0")  # Biến lưu kết quả
label_result = tk.Label(root, textvariable=ket_qua_var,
                        relief='sunken', width=10)
label_result.grid(row=3, column=2, padx=5, pady=5)

# 6. Các nút phép toán (Cộng, Trừ, Nhân, Chia)
btn_cong = tk.Button(
    root, text="Cộng", command=lambda: tinh_toan('cong'), width=8)
btn_cong.grid(row=1, column=0, padx=10, pady=5)

btn_tru = tk.Button(
    root, text="Trừ", command=lambda: tinh_toan('tru'), width=8)
btn_tru.grid(row=2, column=0, padx=10, pady=5)

btn_nhan = tk.Button(
    root, text="Nhân", command=lambda: tinh_toan('nhan'), width=8)
btn_nhan.grid(row=3, column=0, padx=10, pady=5)

btn_chia = tk.Button(
    root, text="Chia", command=lambda: tinh_toan('chia'), width=8)
btn_chia.grid(row=4, column=0, padx=10, pady=5)

# 7. Nút Thoát
btn_thoat = tk.Button(root, text="Thoát", command=root.quit, width=8)
btn_thoat.grid(row=4, column=2, padx=5, pady=5, sticky='e')

# Chạy vòng lặp chính
# root.mainloop()
