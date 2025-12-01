def oscillate(start, stop):
    """
    Tạo ra một chuỗi số dao động từ start đến stop và ngược lại,
    sau đó tiếp tục dao động qua các giá trị âm.
    """

    # 1. Giai đoạn Tăng (start -> stop)
    # Ví dụ: -3, -2, -1, 0, 1, 2, 3, 4, 5
    for n in range(start, stop + 1):
        yield n

    # 2. Giai đoạn Giảm (stop-1 -> start)
    # Ví dụ: 4, 3, 2, 1, 0, -1, -2
    for n in range(stop - 1, start - 1, -1):
        yield n

    # 3. Giai đoạn Giảm xuống âm sâu (start-1 -> -(stop))
    # Ví dụ: -3, -4, -5
    for n in range(start - 1, -(stop) - 1, -1):
        yield n

    # 4. Giai đoạn Tăng trở lại 1 bước (-(stop)+1 -> start-1)
    # Ví dụ: -4
    for n in range(-(stop) + 1, start, 1):
        yield n


# Mã kiểm tra:
print("Kết quả hàm oscillate(-3, 5):")
ket_qua = []
for n in oscillate(-3, 5):
    ket_qua.append(str(n))

print(' '.join(ket_qua))

# Kết quả mong đợi: -3 -2 -1 0 1 2 3 4 5 4 3 2 1 0 -1 -2 -3 -4 -5 -4
