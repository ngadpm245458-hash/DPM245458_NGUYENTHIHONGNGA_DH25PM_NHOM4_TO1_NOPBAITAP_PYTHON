def nhap_day_tang_dan():
    """Yêu cầu người dùng nhập dãy số theo thứ tự tăng dần."""
    day_so = []

    print("Nhập dãy số theo thứ tự tăng dần (nhập 'x' để dừng):")

    while True:
        try:
            nhap_lieu = input(f"Nhập số thứ {len(day_so) + 1}: ")

            if nhap_lieu.lower() == 'x':
                break

            so_moi = float(nhap_lieu)

            # Kiểm tra điều kiện tăng dần
            if len(day_so) > 0 and so_moi <= day_so[-1]:
                print(
                    f"Lỗi: Số mới ({so_moi}) phải lớn hơn số trước đó ({day_so[-1]}). Vui lòng nhập lại.")
                continue

            day_so.append(so_moi)

        except ValueError:
            print("Lỗi: Vui lòng nhập một số hoặc 'x'.")

    print(f"\nDãy số đã nhập: {day_so}")

# nhap_day_tang_dan()
