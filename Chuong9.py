import math


def find_factors(n: int) -> list:
    """
    Tìm tất cả các ước số (factors) dương của số nguyên n.
    """
    n = abs(n)
    if n == 0:
        return []

    factors = []
    # Chỉ cần kiểm tra từ 1 đến căn bậc hai của n
    # (Ước số sẽ luôn đi theo cặp)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            # Thêm ước số cặp, trừ trường hợp i*i = n
            if i * i != n:
                factors.append(n // i)

    # Sắp xếp lại danh sách ước số
    factors.sort()
    return factors

# Ví dụ: find_factors(12) -> [1, 2, 3, 4, 6, 12]


def find_multiples(n: int, k: int = 10) -> list:
    """
    Tìm k bội số đầu tiên của số nguyên n.
    Mặc định tìm 10 bội số đầu tiên (n*1, n*2, ..., n*k).
    """
    if k <= 0:
        return []

    multiples = []
    for i in range(1, k + 1):
        multiples.append(n * i)
    return multiples


# Ví dụ: find_multiples(5, 5) -> [5, 10, 15, 20, 25]


def find_hcf(a: int, b: int) -> int:
    """Tìm Ước số chung lớn nhất (HCF/GCD) của a và b bằng thuật toán Euclidean."""
    return math.gcd(a, b)  # Sử dụng hàm gcd có sẵn trong thư viện math (Python 3.5+)


def find_lcm(a: int, b: int) -> int:
    """Tìm Bội số chung nhỏ nhất (LCM)."""
    if a == 0 or b == 0:
        return 0
    hcf_val = find_hcf(a, b)
    lcm_val = abs(a * b) // hcf_val
    return lcm_val


def chuong_10_main_demo():
    print("--- CHƯƠNG 10: THUẬT TOÁN SỐ HỌC HOÀN CHỈNH ---")
    try:
        n = int(input("Nhập số nguyên n (để tìm ước/bội): "))

        # DEMO cho 1 số (Bài 1c, 1d)
        print(f"\n[Bài 1c] Ước số của {n}: {find_factors(n)}")
        print(f"[Bài 1d] 10 Bội số đầu tiên của {n}: {find_multiples(n, 10)}")

        # DEMO cho 2 số (Bài 1a, 1b)
        a = n
        b_str = input(f"\nNhập số nguyên b (để tìm HCF/LCM với {a}): ")
        if b_str:
            b = int(b_str)
            hcf = find_hcf(a, b)
            lcm = find_lcm(a, b)

            print(
                f"\n[Bài 1a] Ước chung lớn nhất (HCF/GCD) của {a} và {b} là: {hcf}")
            print(
                f"[Bài 1b] Bội chung nhỏ nhất (LCM) của {a} và {b} là: {lcm}")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
