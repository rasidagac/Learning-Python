msg = 'Python Kursumuza Hoş Geldiniz. Ben Raşit Ağaç'.split()

sayilar = [1, 3, 5, 7, 9]

sonuc = sayilar
sonuc = sayilar[0]
sonuc = sayilar[4]
# sonuc = sayilar[5] # IndexError: list index out of range

isimler = ['ahmet', 'ali', 'can', 'ada']
# print(type(isimler[0]))

listeAli = ['ali', 20]
listeAhmet = ['ahmet', 22]

sonuc = listeAli[0]
sonuc = listeAli[1]

# ogrencielr = [['ali', 20], ['ahmet', 22]]
ogrencielr = [listeAli, listeAhmet]

sonuc = ogrencielr[0][0]
sonuc = ogrencielr[1][0]

print(sonuc)