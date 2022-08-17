diller = ['Python', 'C#', 'Java', 'Javascript', 'React']

sonuc = diller
sonuc = type(diller)
sonuc = diller[:3]
sonuc = diller[-1]
sonuc = diller[-4:-1]
# diller[0] = 'HTML'
diller[-1] = 'HTML'

sonuc = len(diller)
sonuc = diller + ['Agular', 'Vue.js']

# if bloğu
if 'Python' in diller: 
    print('Değer listenin bir elemanı')

# döngüler
for x in diller:
    print(x)

del diller[0]

sonuc = diller

print(sonuc)