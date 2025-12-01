import xml.etree.ElementTree as ET
import os

# --- Cấu hình File ---
FILE_NHOM = "nhomthietbi.xml"
FILE_THIET_BI = "thietbi.xml"

# --- Cấu trúc dữ liệu XML dự kiến ---
# File nhomthietbi.xml: <dsnhom> -> <nhom ma="N1"> -> <ten>Nhóm 1</ten>
# File thietbi.xml: <dsthietbi> -> <thietbi ma="TB1"> -> <ten>Thiết bị 1</ten>, <manhom>N1</manhom>

# --- Hàm Tiện Ích Chung ---


def tao_file_xml_mau():
    """Tạo hai file XML mẫu nếu chúng chưa tồn tại."""
    # 1. Tạo File Nhóm Thiết Bị
    if not os.path.exists(FILE_NHOM):
        root_nhom = ET.Element('dsnhom')

        nhom1 = ET.SubElement(root_nhom, 'nhom', ma='N1')
        ET.SubElement(nhom1, 'ten').text = 'Máy Tính Xách Tay'

        nhom2 = ET.SubElement(root_nhom, 'nhom', ma='N2')
        ET.SubElement(nhom2, 'ten').text = 'Máy In'

        nhom3 = ET.SubElement(root_nhom, 'nhom', ma='N3')
        ET.SubElement(nhom3, 'ten').text = 'Thiết Bị Mạng'

        tree_nhom = ET.ElementTree(root_nhom)
        tree_nhom.write(FILE_NHOM, encoding='utf-8', xml_declaration=True)
        print(f"✅ Đã tạo file mẫu: {FILE_NHOM}")

    # 2. Tạo File Thiết Bị
    if not os.path.exists(FILE_THIET_BI):
        root_tb = ET.Element('dsthietbi')

        tb1 = ET.SubElement(root_tb, 'thietbi', ma='TB1')
        ET.SubElement(tb1, 'ten').text = 'Laptop Dell X'
        ET.SubElement(tb1, 'manhom').text = 'N1'

        tb2 = ET.SubElement(root_tb, 'thietbi', ma='TB2')
        ET.SubElement(tb2, 'ten').text = 'Máy In Canon'
        ET.SubElement(tb2, 'manhom').text = 'N2'

        tb3 = ET.SubElement(root_tb, 'thietbi', ma='TB3')
        ET.SubElement(tb3, 'ten').text = 'Router Cisco'
        ET.SubElement(tb3, 'manhom').text = 'N3'

        tb4 = ET.SubElement(root_tb, 'thietbi', ma='TB4')
        ET.SubElement(tb4, 'ten').text = 'Laptop HP Z'
        ET.SubElement(tb4, 'manhom').text = 'N1'

        tree_tb = ET.ElementTree(root_tb)
        tree_tb.write(FILE_THIET_BI, encoding='utf-8', xml_declaration=True)
        print(f"✅ Đã tạo file mẫu: {FILE_THIET_BI}")


def doc_xml_va_lay_root(ten_file):
    """Đọc file XML và trả về ElementTree và root element."""
    try:
        tree = ET.parse(ten_file)
        root = tree.getroot()
        return tree, root
    except FileNotFoundError:
        print(f"❌ Lỗi: File '{ten_file}' không tìm thấy.")
        return None, None
    except ET.ParseError as e:
        print(f"❌ Lỗi khi phân tích file XML '{ten_file}': {e}")
        return None, None


def lay_danh_sach_nhom(root_nhom):
    """Trích xuất danh sách nhóm thành dictionary {ma: ten}."""
    ds_nhom = {}
    if root_nhom is not None:
        for nhom in root_nhom.findall('nhom'):
            ma = nhom.get('ma')
            ten_element = nhom.find('ten')
            if ma and ten_element is not None:
                ds_nhom[ma] = ten_element.text
    return ds_nhom

# --- 1. Thêm/Ghi thiết bị mới vào XML ---


def them_thiet_bi(ma, ten, ma_nhom):
    """Thêm một thiết bị mới vào file thietbi.xml."""
    tree, root = doc_xml_va_lay_root(FILE_THIET_BI)
    if root is None:
        return

    # Kiểm tra xem mã thiết bị đã tồn tại chưa
    if root.find(f"thietbi[@ma='{ma}']") is not None:
        print(f"❌ Lỗi: Mã thiết bị {ma} đã tồn tại.")
        return

    # Tạo element thiết bị mới
    new_tb = ET.SubElement(root, 'thietbi', ma=ma)
    ET.SubElement(new_tb, 'ten').text = ten
    ET.SubElement(new_tb, 'manhom').text = ma_nhom

    # Ghi lại file XML
    tree.write(FILE_THIET_BI, encoding='utf-8', xml_declaration=True)
    print(f"✅ Đã thêm thiết bị {ten} ({ma}) vào file {FILE_THIET_BI}.")

# --- 2. Hiển thị danh sách thiết bị ---


def hien_thi_thiet_bi(root_tb, ds_nhom):
    """Hiển thị danh sách thiết bị cùng tên nhóm."""
    if root_tb is None:
        print("Không có dữ liệu thiết bị để hiển thị.")
        return
    print("\n--- DANH SÁCH THIẾT BỊ ---")
    print(
        f"| {'Mã TB':<8} | {'Tên Thiết Bị':<30} | {'Mã Nhóm':<8} | {'Tên Nhóm':<20} |")
    print("-" * 75)

    # Lặp qua tất cả các element <thietbi>
    for tb in root_tb.findall('thietbi'):
        ma = tb.get('ma')
        ten = tb.find('ten').text if tb.find('ten') is not None else "N/A"
        ma_nhom = tb.find('manhom').text if tb.find(
            'manhom') is not None else "N/A"

        ten_nhom = ds_nhom.get(ma_nhom, "Không xác định")

        print(f"| {ma:<8} | {ten:<30} | {ma_nhom:<8} | {ten_nhom:<20} |")
    print("-" * 75)

# --- 3. Lọc Danh sách thiết bị theo Nhóm thiết bị ---


def hien_thi_theo_nhom(root_tb, ds_nhom):
    """Hiển thị thiết bị được nhóm theo Tên Nhóm."""
    if root_tb is None:
        print("Không có dữ liệu thiết bị.")
        return

    # Tạo dictionary để nhóm thiết bị
    thietbi_theo_nhom = {ma_nhom: {'ten': ten_nhom, 'ds_tb': []}
                         for ma_nhom, ten_nhom in ds_nhom.items()}

    for tb in root_tb.findall('thietbi'):
        ma = tb.get('ma')
        ten = tb.find('ten').text
        ma_nhom = tb.find('manhom').text

        if ma_nhom in thietbi_theo_nhom:
            thietbi_theo_nhom[ma_nhom]['ds_tb'].append((ma, ten))

    print("\n--- DANH SÁCH THIẾT BỊ THEO NHÓM ---")
    for nhom_data in thietbi_theo_nhom.values():
        print(f"\n>> Nhóm: {nhom_data['ten']}")
        if nhom_data['ds_tb']:
            for ma, ten in nhom_data['ds_tb']:
                print(f"   - [{ma}] {ten}")
        else:
            print("   (Không có thiết bị nào trong nhóm này)")

# --- 4. Tìm kiếm thiết bị theo Mã và Tên ---


def tim_kiem_thiet_bi(root_tb, tu_khoa, ds_nhom):
    """Tìm kiếm thiết bị theo mã hoặc tên."""
    if root_tb is None:
        print("Không có dữ liệu thiết bị để tìm kiếm.")
        return

    tu_khoa = tu_khoa.lower()
    ket_qua = []

    for tb in root_tb.findall('thietbi'):
        ma = tb.get('ma').lower()
        ten = tb.find('ten').text.lower()
        ma_nhom = tb.find('manhom').text

        if tu_khoa in ma or tu_khoa in ten:
            ket_qua.append({
                'ma': tb.get('ma'),
                'ten': tb.find('ten').text,
                'ten_nhom': ds_nhom.get(ma_nhom, "Không xác định")
            })

    print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{tu_khoa}' ---")
    if ket_qua:
        for kq in ket_qua:
            print(
                f"- Mã: {kq['ma']} | Tên: {kq['ten']} | Nhóm: {kq['ten_nhom']}")
    else:
        print("Không tìm thấy thiết bị nào phù hợp.")

# --- Hàm Chạy Chính ---


def main_xml():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ THIẾT BỊ (XML File) ---")

    # 0. Tạo file mẫu nếu chưa có
    tao_file_xml_mau()

    # Đọc dữ liệu ban đầu
    _, root_nhom = doc_xml_va_lay_root(FILE_NHOM)
    tree_tb, root_tb = doc_xml_va_lay_root(FILE_THIET_BI)

    if root_nhom is None or root_tb is None:
        print("Không thể khởi tạo chương trình do lỗi đọc file XML.")
        return

    ds_nhom = lay_danh_sach_nhom(root_nhom)

    # 1. Thêm mới một thiết bị
    them_thiet_bi("TB5", "Máy Chiếu Sony", "N3")
    # Cần đọc lại file sau khi thêm để cập nhật dữ liệu (hoặc dùng tree_tb)
    tree_tb, root_tb = doc_xml_va_lay_root(FILE_THIET_BI)

    # 2. Hiển thị danh sách thiết bị
    hien_thi_thiet_bi(root_tb, ds_nhom)

    # 3. Hiển thị danh sách thiết bị theo nhóm
    hien_thi_theo_nhom(root_tb, ds_nhom)

    # 4. Tìm kiếm thiết bị theo Mã và Tên
    tim_kiem_thiet_bi(root_tb, "Laptop", ds_nhom)
    tim_kiem_thiet_bi(root_tb, "TB2", ds_nhom)


# Khởi chạy chương trình
main_xml()
