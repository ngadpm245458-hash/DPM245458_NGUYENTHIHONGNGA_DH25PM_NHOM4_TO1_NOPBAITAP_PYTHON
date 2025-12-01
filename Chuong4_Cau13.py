import math


def tinh_tong_uoc(n):
    """
    Tính tổng các ước số nguyên dương của n, KHÔNG KỂ chính nó.

    Args:
        n (int): Số nguyên dương cần kiểm tra.

    Returns:
        int: Tổng các ước số của n (trừ n).
    """
    if n <= 1:
        return 0  # Số nguyên tố, 1, hoặc 0 không có tổng ước đáng kể

    tong_uoc = 1  # Bắt đầu với 1 (luôn là ước số)

    # Chỉ cần lặp đến căn bậc 2 của n để tối ưu tốc độ
    limit = int(math.sqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            tong_uoc += i            # Cộng ước i
            uoc_doi = n // i         # Tìm ước đối diện
            if uoc_doi != i:
                # Cộng ước đối diện (tránh lặp với số chính phương)
                tong_uoc += uoc_doi

    return tong_uoc


def kiem_tra_so_hoan_thien(n):
    """Kiểm tra xem n có phải là số hoàn thiện (Perfect Number) hay không."""
    if n <= 0:
        return False
    # Số hoàn thiện là số có tổng các ước (không kể nó) BẰNG chính nó
    return tinh_tong_uoc(n) == n


def kiem_tra_so_thinh_vuong(n):
    """Kiểm tra xem n có phải là số thịnh vượng (Abundant Number) hay không."""
    if n <= 0:
        return False
    # Số thịnh vượng là số có tổng các ước (không kể nó) LỚN HƠN nó
    return tinh_tong_uoc(n) > n


# Mã kiểm tra:

n1 = 6
n2 = 12
n3 = 28
n4 = 15

print(f"\n--- Kiểm tra Số học ---")

# Kiểm tra số 6 (Ví dụ: 1+2+3 = 6)
tong_6 = tinh_tong_uoc(n1)
print(f"Tổng ước của {n1} (trừ nó): {tong_6}")
print(f"Số {n1} là số hoàn thiện? {kiem_tra_so_hoan_thien(n1)}")    # True
print(f"Số {n1} là số thịnh vượng? {kiem_tra_so_thinh_vuong(n1)}")   # False

print("-" * 20)

# Kiểm tra số 12 (Ví dụ: 1+2+3+4+6 = 16 > 12)
tong_12 = tinh_tong_uoc(n2)
print(f"Tổng ước của {n2} (trừ nó): {tong_12}")
print(f"Số {n2} là số hoàn thiện? {kiem_tra_so_hoan_thien(n2)}")    # False
print(f"Số {n2} là số thịnh vượng? {kiem_tra_so_thinh_vuong(n2)}")  # True

print("-" * 20)

# Kiểm tra số 28 (Ví dụ: 1+2+4+7+14 = 28)
tong_28 = tinh_tong_uoc(n3)
print(f"Tổng ước của {n3} (trừ nó): {tong_28}")
print(f"Số {n3} là số hoàn thiện? {kiem_tra_so_hoan_thien(n3)}")    # True
print(f"Số {n3} là số thịnh vượng? {kiem_tra_so_thinh_vuong(n3)}")  # False
