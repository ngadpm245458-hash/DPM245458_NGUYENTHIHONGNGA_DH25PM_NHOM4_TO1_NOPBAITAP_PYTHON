import tkinter as tk


def tao_nut_style():
    """Tạo giao diện hiển thị các loại style (relief) khác nhau."""
    root_style = tk.Tk()
    root_style.title("Button Styles")

    styles = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

    # Tạo tiêu đề cột
    tk.Label(root_style, text="Button Style:", font=(
        'Arial', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5)
    for col, style_name in enumerate(styles):
        tk.Label(root_style, text=style_name, font=('Arial', 10, 'bold')).grid(
            row=0, column=col + 1, padx=5, pady=5)

    # Thử nghiệm với các borderwidth khác nhau
    for row_index, bw in enumerate([1, 2, 4]):
        # Label hiển thị borderwidth
        tk.Label(root_style, text=f"borderwidth: {bw}").grid(
            row=row_index + 1, column=0, padx=5, pady=5)

        # Tạo các nút với style khác nhau
        for col_index, style_name in enumerate(styles):
            btn = tk.Button(
                root_style,
                text=style_name,
                relief=style_name,
                borderwidth=bw,
                width=8
            )
            btn.grid(row=row_index + 1, column=col_index + 1, padx=5, pady=5)

    # root_style.mainloop()

# tao_nut_style()
