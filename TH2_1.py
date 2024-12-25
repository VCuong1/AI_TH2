import re


def kiem_tra_hop_le(bieu_thuc):
   
    mau = r'^[A-Z()∧∨¬→↔ ]+$'
    return bool(re.match(mau, bieu_thuc))


def danh_gia_bieu_thuc(bieu_thuc, gia_tri_bien):
   
    bieu_thuc = bieu_thuc.replace('¬', ' not ')
    bieu_thuc = bieu_thuc.replace('∧', ' and ')
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


def main():
    
    bieu_thuc = input("Nhập biểu thức logic: ")
    
   
    if not kiem_tra_hop_le(bieu_thuc):
        print("Biểu thức không hợp lệ.")
        return

    
    gia_tri_bien = {}
    bien_mau = re.findall(r'[A-Z]', bieu_thuc)
    for bien in set(bien_mau):
        while True:
            gia_tri = input(f"Nhập giá trị cho {bien} (True/False): ")
            if gia_tri.lower() in ['true', 'false']:
                gia_tri_bien[bien] = gia_tri.lower() == 'true'
                break
            else:
                print("Giá trị không hợp lệ, vui lòng nhập lại (True/False).")
    
 
    ket_qua = danh_gia_bieu_thuc(bieu_thuc, gia_tri_bien)
    if ket_qua is not None:
        print(f"Kết quả của biểu thức là: {ket_qua}")


if __name__ == "__main__":
    main()