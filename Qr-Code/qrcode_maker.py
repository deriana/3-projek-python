import qrcode

print("=" * 40)
print("Qr.Code Generator")
print("=" * 40)

data = input("Masukkan Data Yang Ingin Diubah Ke Qr Code: ")
box_size = int(input("Masukkan Ukuran Qr Code Nya: "))
fill_color =input("Masukkan Warna Color Nya: ")
back_color =input("Masukkan Base Warna Qr.Code Nya: ")

if back_color:
    print('='*30)
    print('QR Code Telah Selasai Dibuat')
    print('-'*30)
    
qr = qrcode.QRCode(
  version=1,
  box_size=box_size,
  border=2,)

qr.add_data(data)
img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save("qrcode.jpg")