import module as m

juventus = []

for s in open('juve.txt', encoding='utf-8'):
    juventus.append(m.Jatekos(s))

# 1. feladat:
print(f'1. feladat: igazolt játékosok száma: {len(juventus)}')

# 2. feladat:
print('2. feladat:', end=' ')
if m.magyar(juventus): print('van magyar játékos')
else: print('nincs magyar játékos')

# 3. feladat:
print(f'3. feladat: összesen {m.db_olasz(juventus)} olasz játékos van a csapatban')

# 4. feladat:
print(f'4. feladat: legfiatalabb játékos: {m.legfiatalabb(juventus)}')

# 5. feladat:
print(f'a Juventusban az átlagéletkor: {m.atlageletkor(juventus)}')

# 6. feladat:
# kihagyjuk, mert még nem tanultunk rá módszert
# de egyébként:
print('6. feladat:')
for kvp in m.posztok(juventus).items():
    print(f'\t{kvp[0]}: {kvp[1]} db')


# 7. feladat:
print(f'a Juventus legidősebb csatára: {m.legidosebb_csatar(juventus)}')

# 8. feladat:
# szintén kihagyjuk, ugyan azon okból
# de egyébként:
print(f'8. feladat: az {m.pont_3_szuletett(juventus)} években született pontosan 3 játékos.')