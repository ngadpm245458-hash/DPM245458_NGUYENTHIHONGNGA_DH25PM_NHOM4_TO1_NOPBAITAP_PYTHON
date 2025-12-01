import os

# Cấu hình
FILE_SP = "sanpham.txt"
DELIMITER = ";"


def luuFile(path, line):
    with open(path, 'a', encoding='utf8') as file:
        file.write(line + "\n")


def docFile(path):
    ds_sp = []
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as file:
            for line in file:
                data = line.strip()
                if data:
                    arr = data.split(DELIMITER)
                    try:
                        # Chỉ mục 2 là Giá
                        arr[2] = float(arr[2])
                        ds_sp.append(arr)
                    except (IndexError, ValueError):
                        continue
    return ds_sp


def nhapSanPham_va_luu():
    # ... (Chi tiết hàm nhập)
    ma = input("Mã: ")
    ten = input("Tên: ")
    gia = input("Giá: ")
    luuFile(FILE_SP, f"{ma}{DELIMITER}{ten}{DELIMITER}{gia}")


def xuatSanPham(dssp):
    # ... (Chi tiết hàm hiển thị)
    if not dssp:
        return
    print("--- DANH SÁCH SP ---")
    for row in dssp:
        print(f"Mã: {row[0]}, Tên: {row[1]}, Giá: {row[2]:,.0f}")


def sorting(dssp):
    # Sắp xếp theo giá (chỉ mục 2) tăng dần
    dssp.sort(key=lambda sp: sp[2])
    return dssp

# main_sp_text_file()
