import random


def nhap_list_khong_trung():
    """Nhập N và tạo list N số ngẫu nhiên không trùng nhau."""

    try:
        N = int(input("Nhập số lượng phần tử N: "))
        min_val = 1
        max_val = 1000  # Phạm vi số ngẫu nhiên

        if N <= 0:
            print("Lỗi: N phải lớn hơn 0.")
            return

        if N > (max_val - min_val + 1):
            print(
                f"Lỗi: N quá lớn so với phạm vi ngẫu nhiên [{min_val}, {max_val}].")
            return

        # Tạo set để đảm bảo tính duy nhất
        tap_hop_so = set()
        while len(tap_hop_so) < N:
            tap_hop_so.add(random.randint(min_val, max_val))

        # Chuyển set thành list và in ra
        list_ket_qua = list(tap_hop_so)
        print(f"List {N} số ngẫu nhiên KHÔNG trùng nhau: {list_ket_qua}")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

# nhap_list_khong_trung()
