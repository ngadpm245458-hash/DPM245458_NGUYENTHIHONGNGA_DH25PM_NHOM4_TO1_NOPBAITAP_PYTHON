def kiem_tra_nguyen_to(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def xu_ly_mang_so_tu_nhien():
    """Nhập mảng số tự nhiên và thực hiện thống kê."""

    # Ví dụ mẫu: M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]
    chuoi_nhap = input(
        "Nhập mảng số tự nhiên (cách nhau bởi dấu phẩy hoặc khoảng trắng): ")

    try:
        M = [int(s) for s in chuoi_nhap.replace(
            ',', ' ').split() if s.isdigit()]
    except:
        print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng chỉ nhập số tự nhiên.")
        return

    le = []
    chan = []
    nguyen_to = []
    khong_nguyen_to = []

    for so in M:
        if so % 2 != 0:
            le.append(so)
        else:
            chan.append(so)

        if kiem_tra_nguyen_to(so):
            nguyen_to.append(so)
        else:
            khong_nguyen_to.append(so)

    print("\n--- KẾT QUẢ XỬ LÝ MẢNG ---")

    # Dòng 1: Số lẻ
    print(f"Dòng 1: Gồm các số lẻ: {le}, tổng cộng có {len(le)} số lẻ.")

    # Dòng 2: Số chẵn
    print(
        f"Dòng 2: Gồm các số chẵn: {chan}, tổng cộng có {len(chan)} số chẵn.")

    # Dòng 3: Số nguyên tố
    print(f"Dòng 3: Gồm các số nguyên tố: {nguyen_to}")

    # Dòng 4: Số không phải nguyên tố
    print(f"Dòng 4: Gồm các số không phải là số nguyên tố: {khong_nguyen_to}")

# xu_ly_mang_so_tu_nhien()
