import itertools
import re

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def kiem_tra_hop_le(bieu_thuc):
    mau = r'^[A-Z()∧∨¬→↔ ]+$'
    return bool(re.match(mau, bieu_thuc))

# Hàm thay thế các toán tử logic bằng toán tử Python tương ứng
def thay_the_toan_tu(bieu_thuc):
    bieu_thuc = bieu_thuc.replace('¬', ' not ')
    bieu_thuc = bieu_thuc.replace('∧', ' and ')
    bieu_thuc = bieu_thuc.replace('∨', ' or ')
    bieu_thuc = bieu_thuc.replace('→', '<=')
    bieu_thuc = bieu_thuc.replace('↔', '==')
    return bieu_thuc

# Hàm đánh giá biểu thức logic
def danh_gia_bieu_thuc(bieu_thuc, gia_tri_bien):
    bieu_thuc = thay_the_toan_tu(bieu_thuc)
    for bien, gia_tri in gia_tri_bien.items():
        bieu_thuc = bieu_thuc.replace(bien, str(gia_tri))
    return eval(bieu_thuc)

# Hàm tạo bảng chân lý và kiểm tra chứng minh
def tu_dong_chung_minh(menh_de, ket_luan):
    # Xác định các biến logic
    bien_mau = sorted(set(re.findall(r'[A-Z]', ' '.join(menh_de) + ' ' + ket_luan)))
    # Tạo tất cả các tổ hợp giá trị True/False của các biến
    to_hop = list(itertools.product([False, True], repeat=len(bien_mau)))
    
    # Kiểm tra từng tổ hợp giá trị
    for to in to_hop:
        gia_tri_bien = dict(zip(bien_mau, to))
        menh_de_dung = all(danh_gia_bieu_thuc(md, gia_tri_bien) for md in menh_de)
        ket_luan_dung = danh_gia_bieu_thuc(ket_luan, gia_tri_bien)
        # Nếu mệnh đề đúng nhưng kết luận sai, kết luận không được chứng minh
        if menh_de_dung and not ket_luan_dung:
            return False
    return True

# Hàm chính
def main():
    # Nhập các mệnh đề
    menh_de = input("Nhập các mệnh đề, cách nhau bởi dấu phẩy: ").split(',')
    menh_de = [md.strip() for md in menh_de]
    # Nhập kết luận cần chứng minh
    ket_luan = input("Nhập kết luận cần chứng minh: ").strip()
    
    # Kiểm tra tính hợp lệ của các mệnh đề và kết luận
    if not all(kiem_tra_hop_le(md) for md in menh_de) or not kiem_tra_hop_le(ket_luan):
        print("Mệnh đề hoặc kết luận không hợp lệ.")
        return
    
    # Tự động chứng minh
    ket_qua = tu_dong_chung_minh(menh_de, ket_luan)
    if ket_qua:
        print("Kết luận được chứng minh là đúng.")
    else:
        print("Kết luận không được chứng minh là đúng.")

# Chạy chương trình
if __name__ == "__main__":
    main()