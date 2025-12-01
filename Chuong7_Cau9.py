import os

# --- Cấu hình File ---
FILE_SP = "sanpham.txt"
FILE_DM = "danhmuc.txt"
DELIMITER = ","

# --- Quản Lý Danh Mục (Đọc/Ghi đơn giản) ---


def doc_danh_muc():
    """Đọc danh mục từ file danhmuc.txt."""
    dm = {}
    if os.path.exists(FILE_DM):
        with open(FILE_DM, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 2:
                    ma, ten = parts
                    dm[ma] = ten
    return dm


def ghi_danh_muc(dm):
    """Ghi danh mục vào file danhmuc.txt."""
    with open(FILE_DM, 'w', encoding='utf-8') as f:
        for ma, ten in dm.items():
            f.write(f"{ma}{DELIMITER}{ten}\n")

# --- Quản Lý Sản Phẩm ---


def doc_san_pham():
    """Đọc danh sách sản phẩm từ file sanpham.txt."""
    ds_sp = []
    if os.path.exists(FILE_SP):
        with open(FILE_SP, 'r', encoding='utf-8') as f:
            for line in f:
                # Mã, tên, đơn giá, mã_danh_mục
                parts = line.strip().split(DELIMITER)
                if len(parts) == 4:
                    ds_sp.append({
                        'ma': parts[0],
                        'ten': parts[1],
                        'don_gia': float(parts[2]),
                        'ma_dm': parts[3]
                    })
    return ds_sp


def ghi_san_pham(ds_sp):
    """Ghi danh sách sản phẩm vào file sanpham.txt."""
    with open(FILE_SP, 'w', encoding='utf-8') as f:
        for sp in ds_sp:
            line = f"{sp['ma']}{DELIMITER}{sp['ten']}{DELIMITER}{sp['don_gia']}{DELIMITER}{sp['ma_dm']}\n"
            f.write(line)


def them_san_pham(ds_sp, sp_moi):
    """Thêm sản phẩm mới."""
    ds_sp.append(sp_moi)
    print(f"✅ Đã thêm sản phẩm {sp_moi['ten']}.")


def sua_san_pham(ds_sp, ma):
    """Sửa thông tin sản phẩm."""
    for sp in ds_sp:
        if sp['ma'] == ma:
            print(
                f"Thông tin hiện tại: Tên={sp['ten']}, Giá={sp['don_gia']}, Mã DM={sp['ma_dm']}")
            sp['ten'] = input("Nhập tên mới: ") or sp['ten']
            try:
                sp['don_gia'] = float(
                    input("Nhập đơn giá mới: ") or sp['don_gia'])
            except ValueError:
                print("Lỗi: Đơn giá không hợp lệ, giữ nguyên.")
            sp['ma_dm'] = input("Nhập mã danh mục mới: ") or sp['ma_dm']
            print(f"✅ Đã cập nhật sản phẩm có mã {ma}.")
            return True
    print(f"❌ Không tìm thấy sản phẩm có mã {ma}.")
    return False


def xoa_san_pham(ds_sp, ma):
    """Xóa sản phẩm theo mã."""
    initial_len = len(ds_sp)
    # Loại bỏ tất cả sản phẩm có mã trùng (mặc dù mã nên là duy nhất)
    ds_sp[:] = [sp for sp in ds_sp if sp['ma'] != ma]
    if len(ds_sp) < initial_len:
        print(f"✅ Đã xóa sản phẩm có mã {ma}.")
        return True
    print(f"❌ Không tìm thấy sản phẩm có mã {ma}.")
    return False


def tim_kiem_san_pham(ds_sp, tu_khoa):
    """Tìm kiếm sản phẩm theo tên hoặc mã."""
    ket_qua = [
        sp for sp in ds_sp
        if tu_khoa.lower() in sp['ten'].lower() or tu_khoa.lower() in sp['ma'].lower()
    ]
    return ket_qua


def sap_xep_san_pham(ds_sp, truong='ma', dao_nguoc=False):
    """Sắp xếp sản phẩm."""
    try:
        ds_sp.sort(key=lambda sp: sp.get(truong), reverse=dao_nguoc)
        print(f"✅ Đã sắp xếp theo trường '{truong}'.")
    except Exception as e:
        print(f"❌ Lỗi khi sắp xếp: {e}")

# --- Hàm chạy chính và hiển thị ---


def hien_thi_san_pham(ds_sp, dm):
    """Hiển thị danh sách sản phẩm."""
    if not ds_sp:
        print("Danh sách sản phẩm trống.")
        return
    print("\n--- DANH SÁCH SẢN PHẨM ---")
    print(f"| {'Mã':<5} | {'Tên Sản Phẩm':<20} | {'Đơn Giá':<10} | {'Mã DM':<5} | {'Tên Danh Mục':<15} |")
    print("-" * 70)
    for sp in ds_sp:
        ten_dm = dm.get(sp['ma_dm'], "Không rõ")
        print(
            f"| {sp['ma']:<5} | {sp['ten']:<20} | {sp['don_gia']:<10,.0f} | {sp['ma_dm']:<5} | {ten_dm:<15} |")
    print("-" * 70)


def main_sp():
    """Chức năng chính cho Quản lý Sản Phẩm."""
    ds_sp = doc_san_pham()
    dm = doc_danh_muc()

    # Thêm vài danh mục mẫu nếu trống
    if not dm:
        dm['DM01'] = 'Điện Tử'
        dm['DM02'] = 'Thực Phẩm'
        ghi_danh_muc(dm)

    print("--- CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM (Text File) ---")

    # Ví dụ sử dụng
    hien_thi_san_pham(ds_sp, dm)

    # 1. Thêm mới
    if not any(sp['ma'] == 'SP03' for sp in ds_sp):
        them_san_pham(ds_sp, {'ma': 'SP03', 'ten': 'Máy Ảnh Canon',
                      'don_gia': 12500000.0, 'ma_dm': 'DM01'})

    # 2. Sửa
    sua_san_pham(ds_sp, 'SP02')  # Giả sử SP02 đã tồn tại

    # 3. Tìm kiếm
    ket_qua_tk = tim_kiem_san_pham(ds_sp, 'Máy')
    print("\nKết quả tìm kiếm 'Máy':")
    hien_thi_san_pham(ket_qua_tk, dm)

    # 4. Sắp xếp
    sap_xep_san_pham(ds_sp, truong='don_gia', dao_nguoc=True)
    hien_thi_san_pham(ds_sp, dm)

    # 5. Xóa
    xoa_san_pham(ds_sp, 'SP01')  # Giả sử SP01 đã tồn tại

    # 6. Lưu và đọc lại
    ghi_san_pham(ds_sp)
    print(f"\n✅ Đã lưu danh sách sản phẩm vào file {FILE_SP}.")
    ds_sp_moi = doc_san_pham()
    print("\nDanh sách sau khi đọc lại:")
    hien_thi_san_pham(ds_sp_moi, dm)

# main_sp()
