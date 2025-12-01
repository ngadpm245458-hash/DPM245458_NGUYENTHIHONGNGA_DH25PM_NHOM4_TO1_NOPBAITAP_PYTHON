import math

# Nhập tọa độ điểm A
try:
    x_A = float(input("Nhập tọa độ x của điểm A (xA): "))
    y_A = float(input("Nhập tọa độ y của điểm A (yA): "))

    # Nhập tọa độ điểm B
    x_B = float(input("Nhập tọa độ x của điểm B (xB): "))
    y_B = float(input("Nhập tọa độ y của điểm B (yB): "))

    # Tính bình phương hiệu tọa độ x và y
    delta_x_sq = (x_B - x_A)**2
    delta_y_sq = (y_B - y_A)**2

    # Áp dụng công thức khoảng cách (dùng math.sqrt)
    do_dai_AB = math.sqrt(delta_x_sq + delta_y_sq)

    # Xuất kết quả
    print(f"\n--- Kết quả ---")
    print(f"Tọa độ A: ({x_A}, {y_A})")
    print(f"Tọa độ B: ({x_B}, {y_B})")
    print(f"Độ dài đoạn AB là: {do_dai_AB:.4f}")  # Làm tròn 4 chữ số thập phân

except ValueError:
    print("Lỗi: Vui lòng nhập các giá trị số hợp lệ cho tọa độ.")
