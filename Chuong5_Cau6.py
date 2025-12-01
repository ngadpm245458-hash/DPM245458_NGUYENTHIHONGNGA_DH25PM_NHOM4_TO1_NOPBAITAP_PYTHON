import re


def NegativeNumberInStrings(s):
    """
    Trích lọc và trả về danh sách các số nguyên âm có trong chuỗi.

    Args:
        s (str): Chuỗi đầu vào.

    Returns:
        list: Danh sách các số nguyên âm (dạng int).
    """

    # Biểu thức chính quy (Regex) để tìm số âm:
    # - (-): Tìm ký tự dấu trừ
    # - \d+: Tìm một hoặc nhiều chữ số theo sau
    # Dùng re.findall để tìm tất cả các mẫu phù hợp.
    pattern = r'-\d+'

    # re.findall trả về danh sách các chuỗi số âm (ví dụ: ['-5', '-12'])
    so_am_strings = re.findall(pattern, s)

    # Chuyển danh sách chuỗi số âm thành danh sách số nguyên (int)
    so_am_integers = [int(num_str) for num_str in so_am_strings]

    return so_am_integers


# Ví dụ kiểm tra:
chuoi_dau_vao = "abc-5xyz-12k9l-p"
ket_qua = NegativeNumberInStrings(chuoi_dau_vao)

print("--- Câu 6: Trích lọc số âm ---")
print(f"Chuỗi đầu vào: '{chuoi_dau_vao}'")
print(f"Các số nguyên âm trích lọc được: {ket_qua}")
# Output: [-5, -12]
