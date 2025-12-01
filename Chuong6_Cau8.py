def sap_xep_giam_dan():
    """Nhập dãy số thực và sắp xếp theo thứ tự giảm dần."""

    try:
        N = int(input("Nhập số lượng phần tử N của mảng: "))
        if N <= 0:
            print("Lỗi: N phải lớn hơn 0.")
            return

        M = []
        for i in range(N):
            so = float(input(f"Nhập phần tử M[{i}] (số thực): "))
            M.append(so)

        print(f"\nDãy số ban đầu: {M}")

        # Sắp xếp GIẢM DẦN
        M.sort(reverse=True)

        print(f"Dãy số sau khi sắp xếp giảm dần: {M}")

    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ.")

# sap_xep_giam_dan()
