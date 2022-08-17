# 1-
tel = ['Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8']

# 2-
sonuc = len(tel)

# 3-
sonuc = tel[0]
sonuc = tel[-1]

# 4-
tel[0] = 'Samsung S9'
sonuc = tel

# 5-
if 'Samsung S6' in tel:
    sonuc = 'Evet'

# 6-
sonuc = tel[-3]

# 7-
sonuc = tel[:2]

# 8-
# tel.insert(-2, 'Samsung S9')
tel[-2] = 'Samsung S9'
tel[-1] = 'Samsung S10'
sonuc = tel

# 9-
tel = tel + ['iPhone X', 'iPhone XR']
sonuc = tel

# 10-
del tel[-1]
sonuc = tel

# 11-
sonuc = tel[::-1]

# 12-
kullaniciA = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
kullaniciB = ['Sena', 'Turan', 1999, [80, 80, 70]]
kullaniciC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]
kullanicilar = [kullaniciA, kullaniciB, kullaniciC]

# 13-
for x in kullanicilar:
    print(x)
    print('Adı: ' + x[0])
    print('Soyadı: ' + x[1])
    print('D Tarihi: ' + str(x[2]))
    print('Notları: ' + str(x[3]))
    print('----------------------------------------------------------------')


print(sonuc)