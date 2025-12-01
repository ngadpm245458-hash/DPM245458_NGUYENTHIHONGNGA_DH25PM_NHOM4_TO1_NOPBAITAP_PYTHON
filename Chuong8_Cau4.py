import tkinter as tk


def nhap_so(so):
    """Thêm số hoặc dấu thập phân vào ô hiển thị."""
    hien_thi.insert(tk.END, so)


def phep_toan(op):
    """Thêm phép toán vào ô hiển thị."""
    hien_thi.insert(tk.END, op)


def tinh_ket_qua():
    """Tính toán biểu thức hiện tại."""
    try:
        bieu_thuc = hien_thi.get()
        # Dùng eval() để tính toán biểu thức (cần cẩn thận khi dùng eval trong ứng dụng thực)
        ket_qua = eval(bieu_thuc)
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, str(ket_qua))
    except Exception:
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, "LỖI")


def xoa_mot_ky_tu():
    """Xóa ký tự cuối cùng."""
    hien_thi.delete(len(hien_thi.get()) - 1, tk.END)


def xoa_tat_ca():
    """Xóa toàn bộ màn hình."""
    hien_thi.delete(0, tk.END)


# Khởi tạo cửa sổ
root_cal = tk.Tk()
root_cal.title("Calculator đơn giản")

# Màn hình hiển thị
hien_thi = tk.Entry(root_cal, width=20, font=('Arial', 16),
                    bd=5, relief='sunken', justify='right')
hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Định nghĩa các nút
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('/', 4, 3)
]

# Tạo và đặt vị trí các nút
for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        def command(t=text): return nhap_so(t)
    else:  # Phép toán
        def command(t=text): return phep_toan(t)

    btn = tk.Button(root_cal, text=text, width=5, height=2, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Nút Xóa (C) và Kết quả (=)
btn_c = tk.Button(root_cal, text="C", width=5, height=2, command=xoa_tat_ca)
btn_c.grid(row=4, column=2, padx=5, pady=5)

btn_equal = tk.Button(root_cal, text="=", width=5,
                      height=2, command=tinh_ket_qua)
btn_equal.grid(row=5, column=3, padx=5, pady=5)

btn_backspace = tk.Button(root_cal, text="←", width=5,
                          height=2, command=xoa_mot_ky_tu)
btn_backspace.grid(row=5, column=2, padx=5, pady=5)

# root_cal.mainloop()
