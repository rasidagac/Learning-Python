website = 'https://www.sadikturan.com'
kursAdi = 'Python Dersleri: Sıfırdan İleri Seviye Python Programlama.'

print(len(kursAdi))

print(website[8:11])

print(website[-3:])
print(website[len(website)-3:])

print(kursAdi[:15])
print(kursAdi[-15:])

print(kursAdi[::-1])

helloWord = 'Hello world'
# helloWord = helloWord.replace('w', 'W')
# print(helloWord)

print(helloWord[:6] + 'W' + helloWord[7:])

abc = 'abc'

print('abc' * 3)

print(f"Alfabenin ilk üç harfi {abc} {abc} {abc}")

name, surname, age , job = 'Raşit', 'Ağaç', 26, 'Stajyer'

print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}')