import math


def do_dai_doan_AB():
    """Tính độ dài đoạn thẳng AB."""
    try:
        xA = float(input("Nhập xA: "))
        yA = float(input("Nhập yA: "))
        xB = float(input("Nhập xB: "))
        yB = float(input("Nhập yB: "))

        # Công thức khoảng cách: d_AB = sqrt((xB - xA)^2 + (yB - yA)^2)
        do_dai = math.sqrt((xB - xA)**2 + (yB - yA)**2)
        print(f"Độ dài đoạn AB là: {do_dai:.4f}")
    except ValueError:
        print("Lỗi: Vui lòng nhập số thực hợp lệ.")

# do_dai_doan_AB()
