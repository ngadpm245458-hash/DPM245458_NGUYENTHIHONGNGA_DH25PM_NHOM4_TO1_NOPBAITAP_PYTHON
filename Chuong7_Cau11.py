def thong_ke_chuoi():
    """Thống kê các loại ký tự trong một chuỗi."""
    chuoi = input("Nhập vào một chuỗi bất kỳ: ")

    dem_hoa = 0
    dem_thuong = 0
    dem_chu_so = 0
    dem_khoang_trang = 0
    dem_nguyen_am = 0

    # Tập hợp nguyên âm cơ bản (có thể mở rộng cho tiếng Việt)
    NGUYEN_AM = "aeiouáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"

    for ky_tu in chuoi:
        if ky_tu.isalpha():
            if ky_tu.isupper():
                dem_hoa += 1
            elif ky_tu.islower():
                dem_thuong += 1

            # Kiểm tra Nguyên Âm/Phụ Âm
            if ky_tu.lower() in NGUYEN_AM:
                dem_nguyen_am += 1

        elif ky_tu.isdigit():
            dem_chu_so += 1

        elif ky_tu.isspace():
            dem_khoang_trang += 1

    # Tính Phụ Âm và Ký tự đặc biệt
    tong_chu_cai = dem_hoa + dem_thuong
    dem_phu_am = tong_chu_cai - dem_nguyen_am
    dem_ky_tu_dac_biet = len(chuoi) - (tong_chu_cai +
                                       dem_chu_so + dem_khoang_trang)

    print("\n--- KẾT QUẢ THỐNG KÊ ---")
    print(f"- Số chữ IN HOA: {dem_hoa}")
    print(f"- Số chữ in thường: {dem_thuong}")
    print(f"- Số chữ là số: {dem_chu_so}")
    print(f"- Số ký tự đặc biệt: {dem_ky_tu_dac_biet}")
    print(f"- Số khoảng trắng: {dem_khoang_trang}")
    print(f"- Số chữ là Nguyên Âm: {dem_nguyen_am}")
    print(f"- Số chữ là Phụ Âm: {dem_phu_am}")

# thong_ke_chuoi()
