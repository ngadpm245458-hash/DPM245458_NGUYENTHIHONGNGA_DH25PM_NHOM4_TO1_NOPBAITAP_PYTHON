def toi_uu_danh_tu(chuoi_goc):
    """
    Tối ưu chuỗi danh từ: loại bỏ khoảng trắng dư thừa và viết hoa chữ cái đầu mỗi từ.
    """

    # 1. Loại bỏ khoảng trắng đầu/cuối chuỗi và dùng split() để tách các từ.
    #    split() tự động xử lý mọi khoảng trắng dư thừa giữa các từ.
    cac_tu = chuoi_goc.strip().split()

    if not cac_tu:
        return ""  # Trả về chuỗi rỗng nếu đầu vào là khoảng trắng

    # 2. Xử lý từng từ: chuyển về chữ thường, sau đó viết hoa chữ cái đầu (capitalize())
    cac_tu_toi_uu = []
    for tu in cac_tu:
        # Ví dụ: 'dUY' -> 'duy' -> 'Duy'
        tu_toi_uu = tu.lower().capitalize()
        cac_tu_toi_uu.append(tu_toi_uu)

    # 3. Ghép các từ lại với nhau bằng một khoảng trắng đơn
    chuoi_toi_uu = " ".join(cac_tu_toi_uu)

    return chuoi_toi_uu


# Ví dụ kiểm tra:
input_str = "  TrẦn  dUy   thAnH "
output_str = toi_uu_danh_tu(input_str)

print("\n--- Câu 7: Tối ưu danh từ ---")
print(f"Input: '{input_str}'")
print(f"Output: '{output_str}'")
# Output: 'Trần Duy Thanh'
