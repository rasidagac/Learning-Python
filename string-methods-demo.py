website = 'https://www.sadikturan.com'
kursAdi = 'Python Dersleri: Sıfırdan İleri Seviye Python Programlama.'


# 1-
str = ' Hello World '
sonuc = str.strip()

# 2-
str = 'www.sadikturan.com'
sonuc = str.split('.')[1]

# 3-
sonuc = kursAdi.lower()

# 4-
sonuc = website.count('a')

# 5-
# sonuc = website.startswith('www')
sonuc = website.endswith('com')

# 6-
sonuc = website.find('.com')

# 7-
sonuc = kursAdi.isalpha()

# 8-
sonuc = 'Contents'.center(50, '*')

# 9-
sonuc = kursAdi.replace(' ', '-')

# 10-
sonuc = 'Hello World'.replace('World', 'There')

# 11-
sonuc = kursAdi.split()

print(sonuc)