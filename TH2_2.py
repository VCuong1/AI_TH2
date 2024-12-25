import itertools
import re

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def kiem_tra_hop_le(bieu_thuc):
    # Các ký tự hợp lệ bao gồm: các chữ cái viết hoa, các toán tử logic, và dấu ngoặc
    mau = r'^[A-Z()∧∨¬→↔ ]+$'
    return bool(re.match(mau, bieu_thuc))

# Hàm đánh giá biểu thức logic
def danh_gia_bieu_thuc(bieu_thuc, gia_tri_bien):
    # Thay thế các toán tử logic bằng toán tử Python tương ứng
    bieu_thuc = bieu_thuc.replace('¬', ' not ')
    bieu_thuc = bieu_thuc.replace(' ', ' and ')
    bieu_thuc = bieu_thuc.replace('∨', ' or ')
    bieu_thuc = bieu_thuc.replace('→', ' <= ')
    bieu_thuc = bieu_thuc.replace('↔', ' == ')

    # Thay thế các biến bằng giá trị tương ứng
    for bien, gia_tri in gia_tri_bien.items():
        bieu_thuc = bieu_thuc.replace(bien, str(gia_tri))

    # Đánh giá biểu thức
    try:
        ket_qua = eval(bieu_thuc)
        return ket_qua
    except Exception as e:
        print(f"Lỗi khi đánh giá biểu thức: {e}")
        return None

# Hàm in bảng chân lý của biểu thức logic
def bang_chan_ly(bieu_thuc):
    # Tìm tất cả các biến trong biểu thức
    bien_mau = sorted(set(re.findall(r'[A-Z]', bieu_thuc)))
    
    # Tạo tất cả các tổ hợp giá trị True/False của các biến
    to_hop = list(itertools.product([False, True], repeat=len(bien_mau)))
    
    # In tiêu đề bảng chân lý
    print(" | ".join(bien_mau) + " | " + bieu_thuc)
    print("-" * (6 * len(bien_mau) + len(bieu_thuc) + 3))
    
    # Đánh giá biểu thức với từng tổ hợp giá trị và in kết quả
    for to in to_hop:
        gia_tri_bien = dict(zip(bien_mau, to))
        ket_qua = danh_gia_bieu_thuc(bieu_thuc, gia_tri_bien)
        gia_tri = " | ".join(map(str, to))
        print(f"{gia_tri} | {ket_qua}")

# Hàm chính
def main():
    # Nhập biểu thức logic từ người dùng
    bieu_thuc = input("Nhập biểu thức logic: ")
    
    # Kiểm tra tính hợp lệ của biểu thức
    if not kiem_tra_hop_le(bieu_thuc):
        print("Biểu thức không hợp lệ.")
        return

    # In bảng chân lý
    bang_chan_ly(bieu_thuc)

# Chạy chương trình
if __name__ == "__main__":
    main()