# --- Cấu hình File ---
DATABASE_FILE = "database.txt"
DELIMITER = ";"

# --- 1. Nhóm hàm thao tác file (Bạn đã cung cấp) ---


def luuFile(path, line):
    """
    Lưu một dòng dữ liệu vào cuối file.
    """
    try:
        # Mở file ở chế độ 'a' (append) để thêm dữ liệu vào cuối
        with open(path, 'a', encoding='utf8') as file:
            file.write(line + "\n")

        print(f"✅ Đã lưu thành công dữ liệu vào file: {path}")
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")


def docFile(path):
    """
    Đọc tất cả các dòng từ file và trả về danh sách các sản phẩm (List of Lists).
    """
    arrProduct = []

    if not os.path.exists(path):
        print(f"❌ Lỗi: File '{path}' không tồn tại. Tạo file mới.")
        return arrProduct

    try:
        with open(path, 'r', encoding='utf8') as file:
            for line in file:
                data = line.strip()
                if data:
                    # Tách chuỗi thành danh sách các thuộc tính
                    # Cấu trúc: [Mã SP, Tên SP, Giá]
                    arr = data.split(DELIMITER)

                    # Chuyển đổi giá thành float ngay khi đọc
                    try:
                        arr[2] = float(arr[2])
                    except (IndexError, ValueError):
                        # Bỏ qua nếu dòng không đủ 3 phần hoặc giá không phải số
                        continue

                    arrProduct.append(arr)
        print(f"✅ Đã đọc {len(arrProduct)} sản phẩm từ file {path}.")
        return arrProduct
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return arrProduct

# --- 2. Hàm Nhập thông tin Sản phẩm ---


def nhapSanPham():
    """
    Nhập thông tin sản phẩm từ người dùng và lưu vào file.
    """
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM ---")

    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")

    # Xử lý ngoại lệ cho giá
    while True:
        try:
            gia = float(input("Nhập giá sản phẩm: "))
            if gia < 0:
                print("Giá phải lớn hơn hoặc bằng 0.")
                continue
            break
        except ValueError:
            print("Giá nhập vào không hợp lệ. Vui lòng nhập lại số.")

    # Tạo chuỗi dòng dữ liệu theo format: ma;ten;gia
    line = f"{ma}{DELIMITER}{ten}{DELIMITER}{gia}"

    # Lưu vào file
    luuFile(DATABASE_FILE, line)

# --- 3. Hàm Hiển thị Danh sách Sản phẩm ---


def xuatSanPham(dssp):
    """
    Hiển thị danh sách sản phẩm (List of Lists).
    """
    if not dssp:
        print("\nDanh sách sản phẩm trống.")
        return
    print("\n--- DANH SÁCH SẢN PHẨM ---")
    print(f"| {'Mã SP':<8} | {'Tên Sản Phẩm':<25} | {'Giá':<15} |")
    print("-" * 52)

    for row in dssp:
        # row là list: [Mã, Tên, Giá]
        if len(row) == 3:
            # Format giá trị Giá với dấu phân cách hàng nghìn
            gia_format = f"{row[2]:,.0f}"
            print(f"| {row[0]:<8} | {row[1]:<25} | {gia_format:<15} |")
    print("-" * 52)

# --- 4. Hàm Sắp xếp Sản phẩm theo Giá (Quick Sort) ---


def sorting(dssp):
    """
    Sắp xếp danh sách sản phẩm theo giá tăng dần bằng thuật toán sắp xếp (Quick Sort).
    Giá trị Giá nằm ở chỉ mục 2.
    """
    n = len(dssp)

    # Sắp xếp sử dụng Bubble Sort đơn giản (hoặc bạn có thể dùng Quick Sort/Merge Sort)
    # Ở đây sử dụng Bubble Sort để dễ kiểm soát thuật toán.
    for i in range(n):
        for j in range(0, n - i - 1):
            # So sánh giá (chỉ mục 2)
            if dssp[j][2] > dssp[j + 1][2]:
                # Hoán đổi vị trí
                dssp[j], dssp[j + 1] = dssp[j + 1], dssp[j]

    print("\n✅ Đã sắp xếp sản phẩm theo giá tăng dần.")
    return dssp

# --- Hàm Chạy Chính (Main) ---


if __name__ == "__main__":
    import os

    # Bước 1: Nhập thông tin và lưu vào file
    # Có thể gọi hàm này nhiều lần để thêm sản phẩm
    nhapSanPham()
    nhapSanPham()

    # Bước 2: Đọc dữ liệu từ file
    ds_san_pham = docFile(DATABASE_FILE)

    # Bước 3: Hiển thị danh sách trước khi sắp xếp
    xuatSanPham(ds_san_pham)

    # Bước 4: Sắp xếp theo giá
    ds_san_pham_sorted = sorting(ds_san_pham)

    # Bước 5: Hiển thị danh sách sau khi sắp xếp
    xuatSanPham(ds_san_pham_sorted)
