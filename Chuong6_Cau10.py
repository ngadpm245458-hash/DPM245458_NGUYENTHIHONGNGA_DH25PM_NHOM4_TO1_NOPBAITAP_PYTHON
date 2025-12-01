def nhap_matrix(ten_matrix):
    """Hàm nhập ma trận từ bàn phím."""
    try:
        rows = int(input(f"Nhập số hàng của ma trận {ten_matrix}: "))
        cols = int(input(f"Nhập số cột của ma trận {ten_matrix}: "))
        matrix = []
        print(f"Nhập các phần tử cho ma trận {ten_matrix} ({rows}x{cols}):")
        for i in range(rows):
            row = []
            for j in range(cols):
                val = float(input(f"[{i}][{j}]: "))
                row.append(val)
            matrix.append(row)
        return matrix, rows, cols
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ.")
        return None, 0, 0


def cong_matrix(A, B):
    """Cộng hai ma trận A và B."""
    rows = len(A)
    cols = len(A[0])
    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C


def tim_matrix_hoan_vi(M):
    """Tìm ma trận hoán vị (Transpose) của ma trận M."""
    rows = len(M)
    cols = len(M[0])
    # Hoán vị: số hàng mới = số cột cũ, số cột mới = số hàng cũ
    M_T = [[M[j][i] for j in range(rows)] for i in range(cols)]
    return M_T


def in_matrix(M, ten):
    """Hàm in ma trận ra màn hình."""
    print(f"\n--- Ma trận {ten} ---")
    for row in M:
        print(row)


def xu_ly_ma_tran():
    A, rows_A, cols_A = nhap_matrix("A")
    if A is None:
        return

    B, rows_B, cols_B = nhap_matrix("B")
    if B is None:
        return

    in_matrix(A, "A")
    in_matrix(B, "B")

    # Cộng 2 matrix
    if rows_A == rows_B and cols_A == cols_B:
        C = cong_matrix(A, B)
        in_matrix(C, "C (A + B)")
    else:
        print("\nKhông thể cộng hai ma trận vì kích thước không tương đồng.")

    # Ma trận hoán vị
    A_T = tim_matrix_hoan_vi(A)
    B_T = tim_matrix_hoan_vi(B)
    in_matrix(A_T, "A Hoán vị (A^T)")
    in_matrix(B_T, "B Hoán vị (B^T)")

# xu_ly_ma_tran()
