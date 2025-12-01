import math


def tinh_logarit():
    """Hàm tính logarit cơ số a của x (log_a x)"""
    print("Chương trình tính logarit cơ số a của x (log_a x)")

    try:
        # Nhập giá trị x
        x = float(input("Nhập giá trị x (x > 0): "))

        # Nhập giá trị cơ số a
        a = float(input("Nhập giá trị cơ số a (a > 0 và a != 1): "))

        # Kiểm tra điều kiện đầu vào
        if x <= 0:
            print("Lỗi: Giá trị x phải lớn hơn 0.")
            return

        if a <= 0:
            print("Lỗi: Giá trị cơ số a phải lớn hơn 0.")
            return

        if a == 1:
            print("Lỗi: Giá trị cơ số a phải khác 1.")
            return

        # Tính toán theo công thức log_a x = ln(x) / ln(a)
        # math.log(x) trong Python chính là ln(x)
        log_a_x = math.log(x) / math.log(a)

        # Xuất kết quả
        print(f"\n--- Kết quả ---")
        print(f"log_{a} {x} = {log_a_x:.6f}")  # Làm tròn 6 chữ số thập phân

    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}")


# Chạy hàm tính toán
tinh_logarit()
