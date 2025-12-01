import time
import os

# Định nghĩa 4 hình dưới dạng chuỗi đa dòng (multiline string)
HINH_1 = """
    * * * * *
  * * * *
 * * * * *
* * * * * *
"""

HINH_2 = """
* * * * * *
 * * * * *
  * * * *
   * * *
    * * """

HINH_3 = """
* * * * * *
* * * * * * * * *
* * *
* *
*
"""

HINH_4 = """
      *
    * * *
  * * * * *
* * * * * * *
"""


def ve_hinh_dung_sleep(delay_seconds=5):
    """
    Vẽ 4 hình lần lượt, cách nhau bởi thời gian delay_seconds.
    """

    cac_hinh = [HINH_1, HINH_2, HINH_3, HINH_4]

    print(f"Bắt đầu vẽ 4 hình, mỗi hình cách nhau {delay_seconds} giây...")

    # Lặp qua từng hình trong danh sách
    for i, hinh in enumerate(cac_hinh):
        # Xóa màn hình console trước khi vẽ hình mới (tùy chọn, để code chạy sạch hơn)
        # Sử dụng 'cls' cho Windows và 'clear' cho Linux/macOS
        # os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n--- VẼ HÌNH {i + 1} ---")
        print(hinh)

        # Nếu chưa phải hình cuối cùng, tạm dừng (sleep)
        if i < len(cac_hinh) - 1:
            print(f"(Chờ {delay_seconds} giây trước khi vẽ hình tiếp theo...)")
            time.sleep(delay_seconds)
        else:
            print("\nĐã hoàn thành vẽ tất cả 4 hình.")


# Chạy hàm vẽ hình với độ trễ 5 giây
ve_hinh_dung_sleep(delay_seconds=5)
