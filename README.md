# TẠO FONT CHỮ CHỨA KÝ TỰ ẨN

## Yêu cầu

0. Phan tich tham so dong lenh de ho tro compare ca 2 duoi ttf và svg
getopt

1.  qui dịnh về font gốc và font có thay đổi ở 1 kí. Ví dụ
  - font gốc: font1.ttf
  - font sửa:  font1_a.ttf;  font1_A.ttf
2. Mỗi font và các sửa đổi phải để trong 1 thư mục qui định: fonts\font1\
3. Chương trình tao file diff cho phép quét toàn bộ thư mục của 1 font .\fonts\font1 và tạo ra các file diff.

4. Ghép file font gốc với các file diff.

Tạo font có 4 kí tự chứa mã hoá
```dos
   python -m create_encrypted_font.py  font1.ttf  "aAcB""   font1_out.ttf
```


## Báo cáo thiết kế chi tiết

1. Vào thư mục chính của dự án.
2. Gõ lệnh

```shell
python3 -m pydoc -b
```

Như vậy ta có thể truy cập vào website ở url sau để xem báo cáo online <http://localhost:58388/>


