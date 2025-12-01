import math


def tinh_can_long_nhau():
    """Tính giá trị của biểu thức căn bậc 2 lồng nhau S(n)."""

    try:
        # Nhập số lần lồng nhau n
        n = int(input("Nhập số lần căn lồng nhau n (n > 0): "))

        if n <= 0:
            print("Lỗi: n phải là số nguyên dương.")
            return

        # Khởi tạo giá trị S ban đầu (cho dấu căn trong cùng)
        # Bắt đầu tính S từ trong ra ngoài: S = sqrt(2)
        S = math.sqrt(2)

        # Vòng lặp tính toán n-1 lần tiếp theo
        # Ta đã tính 1 lần căn ở trên (n=1), nên ta cần lặp thêm n-1 lần
        for i in range(2, n + 1):
            # Công thức lặp: S_moi = sqrt(2 + S_cu)
            S = math.sqrt(2 + S)

        # Xuất kết quả
        print(f"\n--- Kết quả ---")
        print(f"Giá trị S({n}) = {S:.8f}")

    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


# Chạy hàm tính toán
tinh_can_long_nhau()
