class Jatekos:
    def __init__(self, sor: str):
        v = sor.strip().split(';')
        self.mez = int(v[0])
        self.nev = v[1]
        self.nemz = v[2]
        self.poszt = v[3]
        self.szul = int(v[4])


def magyar(csapat) -> bool:
    for j in csapat:
        if j.nemz == 'magyar':
            return True
    return False


def db_olasz(csapat) -> int:
    c = 0
    for j in csapat:
        if j.nemz == 'olasz':
            c += 1
    return c


def legfiatalabb(csapat) -> str:
    maxi = 0
    for i in range(1, len(csapat)):
        if csapat[i].szul > csapat[maxi].szul:
            maxi = i
    return csapat[maxi].nev


def atlageletkor(csapat) -> float:
    sum = 0
    for j in csapat:
        sum += (2022 - j.szul)
    return round(sum / len(csapat), 2)


def legidosebb_csatar(csapat) -> str:
    mini = 0
    while csapat[mini].poszt != 'csatár':
        mini += 1
    for i in range(1, len(csapat)):
        if csapat[i].poszt == 'csatár' and csapat[i].szul < csapat[mini].szul:
            mini = i
    return csapat[mini].nev


# 6. feladat [csak hogy meglegyen]:
def posztok(csapat) -> dict:
    dict = {}
    for j in csapat:
        if j.poszt not in dict.keys():
            dict[j.poszt] = 1
        else: dict[j.poszt] += 1
    return dict


# 8. feladat [szintén]
def pont_3_szuletett(csapat) -> list:
    dict = {}
    for j in csapat:
        if j.szul not in dict.keys():
            dict[j.szul] = 1
        else: dict[j.szul] += 1
    pontharom = []
    for kvp in dict.items():
        if kvp[1] == 3:
            pontharom.append(kvp[0])
    return pontharom