def thong_ke_chuoi():
    """Chương trình thống kê các loại ký tự trong một chuỗi nhập vào."""

    # 1. Nhập chuỗi
    chuoi = input("Nhập vào một chuỗi bất kỳ: ")

    # 2. Khởi tạo các biến đếm
    dem_hoa = 0
    dem_thuong = 0
    dem_chu_so = 0
    dem_khoang_trang = 0
    dem_nguyen_am = 0

    # Ký tự đặc biệt (sẽ tính sau cùng)
    dem_ky_tu_dac_biet = 0

    # Định nghĩa các nguyên âm (chuyển tất cả thành chữ thường để dễ so sánh)
    NGUYEN_AM = "aeiouáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"

    # 3. Duyệt và đếm từng ký tự
    for ky_tu in chuoi:
        # Kiểm tra Chữ hoa/thường và Số
        if ky_tu.isalpha():
            if ky_tu.isupper():
                dem_hoa += 1
            elif ky_tu.islower():
                dem_thuong += 1

            # Kiểm tra Nguyên Âm/Phụ Âm (chỉ áp dụng cho các ký tự chữ cái)
            # Chuyển ký tự về chữ thường để so sánh với tập NGUYEN_AM
            if ky_tu.lower() in NGUYEN_AM:
                dem_nguyen_am += 1

        elif ky_tu.isdigit():
            dem_chu_so += 1

        elif ky_tu.isspace():
            dem_khoang_trang += 1

    # 4. Tính Phụ Âm và Ký tự đặc biệt

    # Tổng số ký tự chữ cái là Chữ hoa + Chữ thường
    tong_chu_cai = dem_hoa + dem_thuong
    dem_phu_am = tong_chu_cai - dem_nguyen_am

    # Ký tự đặc biệt = Tổng số ký tự - (Hoa + Thường + Số + Khoảng trắng)
    dem_ky_tu_dac_biet = len(chuoi) - (tong_chu_cai +
                                       dem_chu_so + dem_khoang_trang)

    # 5. Xuất kết quả
    print("\n--- KẾT QUẢ THỐNG KÊ CHUỖI ---")
    print(f"- Tổng số ký tự: {len(chuoi)}")
    print(f"- Số chữ IN HOA: {dem_hoa}")
    print(f"- Số chữ in thường: {dem_thuong}")
    print(f"- Số chữ là số: {dem_chu_so}")
    print(f"- Số ký tự đặc biệt: {dem_ky_tu_dac_biet}")
    print(f"- Số khoảng trắng: {dem_khoang_trang}")
    print(f"- Số chữ là Nguyên Âm: {dem_nguyen_am}")
    print(f"- Số chữ là Phụ Âm: {dem_phu_am}")
    print("-" * 30)


# Chạy chương trình
thong_ke_chuoi()
