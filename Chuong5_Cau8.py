import os

# Đường dẫn mẫu
duong_dan = r"d:/music/muabui.mp3"  # Dùng r"" để đảm bảo chuỗi không bị lỗi

# Lưu ý: Với đường dẫn thực tế, nên dùng os.path.sep (là '/') hoặc ('\')


def lay_ten_file_goc(duong_dan_file):
    """
    Lấy ra tên file hoàn chỉnh (ví dụ: muabui.mp3).
    Sử dụng os.path.basename để xử lý đường dẫn đa nền tảng.
    """
    # Hàm này tách phần tên file khỏi đường dẫn
    return os.path.basename(duong_dan_file)


def lay_ten_bai_hat(duong_dan_file):
    """
    Lấy ra tên bài hát (ví dụ: muabui), bỏ phần mở rộng (.mp3).
    """
    # 1. Lấy tên file gốc
    ten_file_goc = lay_ten_file_goc(duong_dan_file)

    # 2. Tách tên file và phần mở rộng (ví dụ: muabui.mp3 -> ('muabui', '.mp3'))
    # os.path.splitext là cách chuẩn để làm việc này.
    ten_bai_hat, _ = os.path.splitext(ten_file_goc)

    return ten_bai_hat


print("\n--- Câu 8: Tách lấy tên bài hát ---")
print(f"Đường dẫn: '{duong_dan}'")

# Yêu cầu 1: Lấy ra muabui.mp3
ten_file_mp3 = lay_ten_file_goc(duong_dan)
print(f"1. Tên file hoàn chỉnh: {ten_file_mp3}")  # Output: muabui.mp3

# Yêu cầu 2: Lấy ra muabui
ten_bai_hat = lay_ten_bai_hat(duong_dan)
print(f"2. Tên bài hát (không mở rộng): {ten_bai_hat}")  # Output: muabui

# Kiểm tra với đường dẫn bất kỳ khác:
duong_dan_khac = r"/home/user/music/my_favorite_song.wav"
print("\n--- Kiểm tra đường dẫn khác ---")
print(f"Tên file hoàn chỉnh: {lay_ten_file_goc(duong_dan_khac)}")
print(f"Tên bài hát: {lay_ten_bai_hat(duong_dan_khac)}")
