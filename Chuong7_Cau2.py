import os

# --- Cấu hình File ---
DATABASE_FILE = "oasl_so.txt"
DELIMITER = ","

# --- Các hàm Thao tác File cơ bản ---


def luuFile(path, data):
    """
    Lưu một dòng dữ liệu (data) vào cuối file (path).
    """
    try:
        # Mở file ở chế độ 'a' (append) để thêm dữ liệu vào cuối
        with open(path, 'a', encoding='utf8') as file:
            file.write(data + "\n")  # Thêm ký tự xuống dòng
    except Exception as e:
        print(f"❌ Lỗi khi ghi file {path}: {e}")


def docFile(path):
    """
    Đọc tất cả các dòng từ file và trả về danh sách các chuỗi số được phân tách.
    Mỗi dòng file tương ứng với một phần tử là list các chuỗi số.
    """
    arrSo = []

    if not os.path.exists(path):
        print(f"❌ Lỗi: File '{path}' không tồn tại. Trả về danh sách rỗng.")
        return arrSo

    try:
        # Mở file ở chế độ 'r' (read)
        with open(path, 'r', encoding='utf8') as file:
            for line in file:
                data = line.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng
                if data:
                    # Tách chuỗi thành danh sách các chuỗi số theo dấu phẩy
                    arr = data.split(DELIMITER)
                    arrSo.append(arr)

        return arrSo
    except Exception as e:
        print(f"❌ Lỗi khi đọc file {path}: {e}")
        return arrSo

# --- Hàm Thực hiện Yêu cầu (a) và (b) ---


def xu_ly_du_lieu(ds_chuoi_so):
    """
    Hàm xử lý dữ liệu: 
    a) Chuyển mỗi dòng thành List các số thực (float).
    b) Xuất các số trên mỗi dòng ra màn hình.

    Args:
        ds_chuoi_so (list): Danh sách các list chuỗi số, đọc từ docFile.
    """
    print("\n--- KẾT QUẢ XỬ LÝ DỮ LIỆU ---")

    for i, dong_chuoi in enumerate(ds_chuoi_so):
        list_so_thuc = []

        # 1. Chuyển đổi sang số thực (float)
        for chuoi_so in dong_chuoi:
            try:
                # Xử lý trường hợp có khoảng trắng thừa
                so_thuc = float(chuoi_so.strip())
                list_so_thuc.append(so_thuc)
            except ValueError:
                print(
                    f"   [Cảnh báo] Dòng {i+1}: '{chuoi_so}' không phải là số hợp lệ. Bỏ qua.")

        # 2. Xuất kết quả
        print(f"\n--- Dòng {i+1} ---")

        # a) List chứa các số thực (đã xử lý)
        print(f"a) List các số thực: {list_so_thuc}")

        # b) Xuất các số ra màn hình
        print("b) Xuất từng số trên màn hình: ", end="")
        for so in list_so_thuc:
            # Format để hiển thị đẹp hơn
            print(f"{so:.2f}", end="\t")
        print()  # Xuống dòng

# --- Hàm Chạy Chính (Main) ---


if __name__ == "__main__":

    # 1. Tạo File Test (Khởi tạo file và lưu dữ liệu mẫu)
    # Xóa file cũ nếu có để đảm bảo chỉ có dữ liệu mới
    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)

    print("--- 1. Tạo File Dữ Liệu Mẫu ---")

    # Dữ liệu mẫu theo hình minh họa
    data_list = [
        "5,-4,7,9,3,1.20",
        "15,9.8,-38,-3,15",
        "5,-4,77,-9,3,-7",
        "55,44,27",
        "-50,26"
    ]

    for data in data_list:
        luuFile(DATABASE_FILE, data)
    print(f"✅ Đã lưu {len(data_list)} dòng vào file {DATABASE_FILE}.")

    # 2. Đọc Dữ liệu từ File
    ds_chuoi_so = docFile(DATABASE_FILE)

    # 3. Xử lý Dữ liệu
    if ds_chuoi_so:
        xu_ly_du_lieu(ds_chuoi_so)
    else:
        print("\nKhông có dữ liệu hợp lệ để xử lý.")
