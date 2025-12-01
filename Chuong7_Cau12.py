import random
import os

# --- Cấu hình File ---
FILE_CSV = "quanlynhanvien_data.csv"
DELIMITER = ";"
SO_DONG = 10
SO_COT = 10
GIA_TRI_TOI_DA = 100  # Giá trị ngẫu nhiên từ 0 đến 99

# 1. Hàm tạo và lưu File CSV


def tao_va_luu_csv(ten_file, so_dong, so_cot, gioi_han_tren=100):
    """
    Tạo và lưu dữ liệu ngẫu nhiên vào file CSV.

    Args:
        ten_file (str): Tên file để lưu.
        so_dong (int): Số lượng dòng dữ liệu cần tạo (10).
        so_cot (int): Số lượng cột/số ngẫu nhiên trên mỗi dòng (10).
        gioi_han_tren (int): Giới hạn trên của giá trị ngẫu nhiên (vd: 100).
    """
    print(f"--- 1. Tạo và Lưu File {ten_file} ---")

    du_lieu = []

    # Tạo dữ liệu ngẫu nhiên
    for i in range(so_dong):
        # Tạo SO_COT số ngẫu nhiên (từ 0 đến gioi_han_tren - 1)
        row = [random.randrange(gioi_han_tren) for _ in range(so_cot)]
        du_lieu.append(row)

    # Ghi dữ liệu vào file
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            for row in du_lieu:
                # Chuyển các số thành chuỗi và nối bằng dấu chấm phẩy ";"
                line = DELIMITER.join(map(str, row))
                f.write(line + "\n")

        print(
            f"✅ Đã tạo thành công {so_dong} dòng, mỗi dòng {so_cot} số ngẫu nhiên vào file '{ten_file}'.")
        print("\n--- Nội dung File mẫu ---")
        # In ra 3 dòng đầu tiên để xem
        for i, row in enumerate(du_lieu):
            if i < 3:
                print(DELIMITER.join(map(str, row)))
            elif i == 3:
                print("...")
        print("---------------------------")

    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")

# 2. Hàm đọc File CSV và tính tổng


def doc_csv_va_tinh_tong(ten_file):
    """
    Đọc file CSV, tính tổng giá trị các phần tử trên mỗi dòng và in ra.

    Args:
        ten_file (str): Tên file CSV cần đọc.
    """
    print(f"\n--- 2. Đọc File {ten_file} và Tính Tổng ---")

    if not os.path.exists(ten_file):
        print(f"❌ Lỗi: File '{ten_file}' không tồn tại.")
        return

    tong_tat_ca = 0

    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            print(
                f"| {'Dòng':<5} | {'Nội Dung (10 số)':<50} | {'Tổng Giá Trị':<12} |")
            print("-" * 75)

            for so_dong, line in enumerate(f, 1):
                # 1. Loại bỏ ký tự xuống dòng và khoảng trắng thừa
                line = line.strip()
                if not line:
                    continue  # Bỏ qua dòng trống

                # 2. Tách chuỗi thành danh sách các chuỗi số
                parts = line.split(DELIMITER)

                # 3. Chuyển các chuỗi số thành số nguyên (int)
                try:
                    so_nguyen = [int(p) for p in parts]
                except ValueError:
                    print(
                        f"Lỗi ở Dòng {so_dong}: Có dữ liệu không phải là số.")
                    continue

                # 4. Tính tổng
                tong_dong = sum(so_nguyen)
                tong_tat_ca += tong_dong

                # 5. Xuất kết quả
                noi_dung_ngan = DELIMITER.join(parts[:10])
                print(f"| {so_dong:<5} | {noi_dung_ngan:<50} | {tong_dong:<12} |")

            print("-" * 75)
            print(
                f"✅ Đã xử lý xong. Tổng giá trị của tất cả các phần tử là: {tong_tat_ca}")

    except Exception as e:
        print(f"❌ Lỗi không xác định khi đọc/xử lý file: {e}")

# --- Hàm Chạy Chính ---


def main_csv():
    # 1. Tạo và Lưu file
    tao_va_luu_csv(FILE_CSV, SO_DONG, SO_COT, GIA_TRI_TOI_DA)

    # 2. Đọc file và Tính Tổng
    doc_csv_va_tinh_tong(FILE_CSV)


# Khởi chạy chương trình
main_csv()
