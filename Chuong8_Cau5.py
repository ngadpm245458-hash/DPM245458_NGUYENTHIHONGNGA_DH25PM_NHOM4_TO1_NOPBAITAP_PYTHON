import tkinter as tk
from tkinter import messagebox


def xu_ly_ok():
    """Xử lý sự kiện khi nhấn OK."""
    old_pass = old_pass_entry.get()
    new_pass1 = new_pass_entry1.get()
    new_pass2 = new_pass_entry2.get()

    # Logic kiểm tra mật khẩu đơn giản
    if new_pass1 != new_pass2:
        messagebox.showerror("Lỗi", "Mật khẩu mới không khớp!")
    elif len(new_pass1) < 6:
        messagebox.showwarning("Cảnh báo", "Mật khẩu mới quá ngắn.")
    elif old_pass == new_pass1:
        messagebox.showinfo("Thông báo", "Mật khẩu mới phải khác mật khẩu cũ.")
    else:
        # Giả lập thành công
        messagebox.showinfo("Thành công", "Đã thay đổi mật khẩu thành công!")
        root_pass.destroy()


def xu_ly_cancel():
    """Hủy bỏ và đóng cửa sổ."""
    root_pass.destroy()


# Khởi tạo cửa sổ
root_pass = tk.Tk()
root_pass.title("Enter New Password")
root_pass.geometry("350x200")

# Tiêu đề
title_label = tk.Label(
    root_pass, text="Enter New Password", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Khung nhập liệu
fields = [
    ("Old Password", 1, "old_pass"),
    ("New Password", 2, "new_pass1"),
    ("Enter New Password Again", 3, "new_pass2")
]

# Tạo các Label và Entry
old_pass_entry = tk.Entry(root_pass, show="*", width=20)
new_pass_entry1 = tk.Entry(root_pass, show="*", width=20)
new_pass_entry2 = tk.Entry(root_pass, show="*", width=20)

entries = {
    "old_pass": old_pass_entry,
    "new_pass1": new_pass_entry1,
    "new_pass2": new_pass_entry2
}

for text, row, key in fields:
    label = tk.Label(root_pass, text=text + ":", anchor='e')
    label.grid(row=row, column=0, sticky='e', padx=10, pady=5)

    entries[key].grid(row=row, column=1, padx=10, pady=5, sticky='w')

# Nút OK và Cancel
btn_ok = tk.Button(root_pass, text="OK", width=8, command=xu_ly_ok)
btn_ok.grid(row=4, column=0, padx=10, pady=10, sticky='e')

btn_cancel = tk.Button(root_pass, text="Cancel", width=8, command=xu_ly_cancel)
btn_cancel.grid(row=4, column=1, padx=10, pady=10, sticky='w')

# root_pass.mainloop()
