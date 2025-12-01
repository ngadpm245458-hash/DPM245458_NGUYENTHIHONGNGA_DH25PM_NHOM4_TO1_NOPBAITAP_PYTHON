import json
import os

# --- Cấu hình File ---
FILE_JSON = "sinhvien.json"

# --- Thao tác File JSON ---


def doc_du_lieu_json():
    """Đọc dữ liệu từ file JSON, trả về dict các lớp học."""
    if os.path.exists(FILE_JSON):
        with open(FILE_JSON, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Trả về cấu trúc rỗng nếu file JSON bị lỗi
                return {}
    return {}


def ghi_du_lieu_json(du_lieu):
    """Ghi dữ liệu (dict các lớp học) vào file JSON."""
    with open(FILE_JSON, 'w', encoding='utf-8') as f:
        json.dump(du_lieu, f, indent=4, ensure_ascii=False)
    print(f"✅ Đã lưu dữ liệu vào file {FILE_JSON}.")

# --- Quản Lý Sinh Viên ---


def them_sinh_vien(du_lieu, ma_lop, sv_moi):
    """Thêm sinh viên mới vào một lớp."""
    if ma_lop in du_lieu:
        du_lieu[ma_lop]['sinh_vien'].append(sv_moi)
        print(f"✅ Đã thêm SV {sv_moi['ten']} vào lớp {ma_lop}.")
        return True
    print(f"❌ Lỗi: Không tìm thấy lớp có mã {ma_lop}.")
    return False


def sua_sinh_vien(du_lieu, ma_sv):
    """Sửa thông tin sinh viên theo mã SV."""
    for lop_data in du_lieu.values():
        for sv in lop_data['sinh_vien']:
            if sv['ma'] == ma_sv:
                print(
                    f"Thông tin hiện tại: Tên={sv['ten']}, Năm Sinh={sv['nam_sinh']}")
                sv['ten'] = input("Nhập tên mới: ") or sv['ten']
                try:
                    sv['nam_sinh'] = int(
                        input("Nhập năm sinh mới: ") or sv['nam_sinh'])
                except ValueError:
                    print("Lỗi: Năm sinh không hợp lệ, giữ nguyên.")
                print(f"✅ Đã cập nhật SV có mã {ma_sv}.")
                return True
    print(f"❌ Không tìm thấy SV có mã {ma_sv}.")
    return False


def xoa_sinh_vien(du_lieu, ma_sv):
    """Xóa sinh viên theo mã SV."""
    for ma_lop, lop_data in du_lieu.items():
        initial_len = len(lop_data['sinh_vien'])
        # Tạo danh sách SV mới, loại bỏ SV có mã trùng
        lop_data['sinh_vien'][:] = [
            sv for sv in lop_data['sinh_vien'] if sv['ma'] != ma_sv]
        if len(lop_data['sinh_vien']) < initial_len:
            print(f"✅ Đã xóa SV có mã {ma_sv} khỏi lớp {ma_lop}.")
            return True
    print(f"❌ Không tìm thấy SV có mã {ma_sv}.")
    return False


def tim_kiem_sinh_vien(du_lieu, tu_khoa):
    """Tìm kiếm sinh viên theo tên hoặc mã."""
    ket_qua = []
    for ma_lop, lop_data in du_lieu.items():
        for sv in lop_data['sinh_vien']:
            if tu_khoa.lower() in sv['ten'].lower() or tu_khoa.lower() in sv['ma'].lower():
                ket_qua.append({'lop': lop_data['ten'], 'sinh_vien': sv})
    return ket_qua


def sap_xep_sinh_vien(du_lieu, truong='ma', dao_nguoc=False):
    """Sắp xếp sinh viên trong từng lớp."""
    try:
        for lop_data in du_lieu.values():
            lop_data['sinh_vien'].sort(
                key=lambda sv: sv.get(truong), reverse=dao_nguoc)
        print(f"✅ Đã sắp xếp tất cả SV theo trường '{truong}'.")
    except Exception as e:
        print(f"❌ Lỗi khi sắp xếp: {e}")

# --- Hàm chạy chính và hiển thị ---


def hien_thi_du_lieu(du_lieu):
    """Hiển thị toàn bộ cấu trúc lớp học và sinh viên."""
    if not du_lieu:
        print("Dữ liệu lớp học/sinh viên trống.")
        return

    print("\n--- DỮ LIỆU LỚP HỌC & SINH VIÊN ---")
    for ma_lop, lop_data in du_lieu.items():
        print(f"\n--- Lớp: {lop_data['ten']} ({ma_lop}) ---")
        if lop_data['sinh_vien']:
            print(f"| {'Mã SV':<8} | {'Tên Sinh Viên':<25} | {'Năm Sinh':<10} |")
            print("-" * 50)
            for sv in lop_data['sinh_vien']:
                print(
                    f"| {sv['ma']:<8} | {sv['ten']:<25} | {sv['nam_sinh']:<10} |")
            print("-" * 50)
        else:
            print("  (Không có sinh viên nào)")


def main_sv():
    """Chức năng chính cho Quản lý Sinh Viên."""
    du_lieu = doc_du_lieu_json()

    # Thêm dữ liệu mẫu nếu trống
    if not du_lieu:
        du_lieu['LT01'] = {'ten': 'Lập Trình Python', 'sinh_vien': []}
        du_lieu['K02'] = {'ten': 'Kế Toán 02', 'sinh_vien': []}

    print("--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (JSON File) ---")

    # Ví dụ thêm sinh viên
    them_sinh_vien(du_lieu, 'LT01', {
                   'ma': 'SV001', 'ten': 'Nguyễn Văn A', 'nam_sinh': 2003})
    them_sinh_vien(du_lieu, 'LT01', {
                   'ma': 'SV003', 'ten': 'Trần Thị C', 'nam_sinh': 2001})
    them_sinh_vien(du_lieu, 'K02', {
                   'ma': 'SV002', 'ten': 'Lê Văn B', 'nam_sinh': 2004})

    hien_thi_du_lieu(du_lieu)

    # 1. Sửa
    sua_sinh_vien(du_lieu, 'SV001')

    # 2. Sắp xếp (theo năm sinh)
    sap_xep_sinh_vien(du_lieu, truong='nam_sinh', dao_nguoc=False)
    hien_thi_du_lieu(du_lieu)

    # 3. Tìm kiếm
    ket_qua_tk = tim_kiem_sinh_vien(du_lieu, 'văn')
    print("\nKết quả tìm kiếm 'văn':")
    for kq in ket_qua_tk:
        print(
            f"- Lớp {kq['lop']} | Mã: {kq['sinh_vien']['ma']}, Tên: {kq['sinh_vien']['ten']}")

    # 4. Xóa
    xoa_sinh_vien(du_lieu, 'SV003')

    # 5. Lưu
    ghi_du_lieu_json(du_lieu)

# main_sv()
