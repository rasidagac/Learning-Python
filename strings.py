ad = 'Raşid'
soyad= 'Ağaç'
yas = '26'

msg = 'Benim adım ' + ad  + ' ve soyadım ' + soyad + '. Yaşım ise ' + yas + '.'
karakterSayisi = len(msg)

print(msg[karakterSayisi-1])

print(msg[-10:]) #-10 dan sonrasını yazar
print(msg[0:40:2])  # 0'dan başlayarak 1'er atlaya atlaya yazar
print(msg[::1]) # tamamını yazar
print(msg[::-1]) # 0'dan başlayarak -1 (yani geri geri yazar
