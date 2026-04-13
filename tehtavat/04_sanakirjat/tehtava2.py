#Tehtävä 2: Kirjoita funktio, jolle annetaan syötteeksi lista. Funktio palauttaa sanakirjan, jossa avaimena on sana ja arvona sanan esiintymismäärä.


def maarat(sanat):
    tulos = {}
    for i in sanat:
        if i not in tulos:
            tulos[i]=0
        tulos[i]+=1
    return tulos

listat = [
    ['mango', 'luumu', 'luumu', 'aprikoosi', 'appelsiini', 'appelsiini', 'aprikoosi', 'mango', 'mango', 'appelsiini', 'mango', 'aprikoosi', 'luumu', 'luumu', 'aprikoosi', 'appelsiini', 'omena', 'omena', 'omena', 'luumu', 'appelsiini', 'appelsiini', 'aprikoosi', 'aprikoosi', 'appelsiini', 'appelsiini', 'omena', 'appelsiini', 'luumu', 'omena', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'appelsiini', 'appelsiini', 'omena', 'luumu', 'luumu', 'aprikoosi', 'appelsiini', 'aprikoosi', 'omena', 'omena', 'omena', 'luumu', 'luumu', 'luumu', 'luumu', 'omena', 'mango', 'appelsiini', 'appelsiini', 'aprikoosi', 'omena', 'luumu', 'appelsiini', 'luumu', 'aprikoosi', 'omena', 'omena', 'luumu', 'appelsiini', 'luumu', 'omena', 'mango', 'appelsiini', 'omena', 'appelsiini', 'mango', 'mango', 'omena', 'mango', 'omena', 'appelsiini', 'luumu', 'luumu', 'luumu', 'mango', 'mango', 'aprikoosi', 'aprikoosi', 'mango', 'luumu', 'aprikoosi', 'aprikoosi', 'appelsiini', 'aprikoosi', 'mango', 'luumu', 'mango', 'mango', 'mango', 'omena', 'appelsiini', 'luumu', 'omena', 'aprikoosi', 'aprikoosi', 'luumu', 'mango', 'omena', 'mango', 'aprikoosi', 'aprikoosi', 'luumu', 'mango', 'mango', 'omena', 'aprikoosi', 'appelsiini', 'omena', 'mango', 'mango', 'aprikoosi', 'luumu', 'omena', 'luumu', 'luumu', 'mango', 'aprikoosi', 'luumu'],
    ['mango', 'mango', 'luumu', 'appelsiini', 'appelsiini', 'luumu', 'aprikoosi', 'luumu', 'appelsiini', 'appelsiini', 'luumu', 'mango', 'luumu', 'luumu', 'omena', 'mango', 'luumu', 'mango', 'omena', 'omena', 'appelsiini', 'luumu', 'mango', 'omena', 'luumu', 'omena', 'luumu', 'mango', 'aprikoosi', 'omena', 'luumu', 'omena', 'omena', 'mango', 'appelsiini', 'omena', 'appelsiini', 'mango', 'aprikoosi', 'omena', 'omena', 'mango', 'omena', 'mango', 'aprikoosi', 'aprikoosi', 'omena', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'appelsiini', 'mango', 'aprikoosi', 'mango', 'aprikoosi', 'omena', 'omena', 'appelsiini', 'aprikoosi', 'aprikoosi', 'mango', 'aprikoosi', 'luumu', 'omena', 'aprikoosi', 'appelsiini', 'aprikoosi', 'aprikoosi', 'luumu', 'mango', 'aprikoosi', 'aprikoosi', 'luumu', 'omena', 'luumu', 'aprikoosi', 'mango', 'luumu', 'omena', 'aprikoosi', 'mango', 'omena', 'appelsiini', 'omena', 'appelsiini', 'mango', 'luumu', 'appelsiini', 'aprikoosi', 'aprikoosi', 'mango', 'luumu', 'appelsiini', 'aprikoosi', 'appelsiini', 'luumu', 'mango', 'aprikoosi', 'luumu', 'omena', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'aprikoosi', 'omena', 'mango', 'luumu', 'mango', 'mango', 'aprikoosi', 'appelsiini', 'mango', 'mango', 'luumu', 'appelsiini', 'appelsiini', 'aprikoosi', 'mango', 'omena']
    ]

for i in listat:
    print(maarat(i))

def test():
    assert maarat(listat[0]) == {'mango': 23, 'luumu': 28, 'aprikoosi': 25, 'appelsiini': 22, 'omena': 23}
    assert maarat(listat[1]) == {'mango': 26, 'luumu': 22, 'appelsiini': 18, 'aprikoosi': 32, 'omena': 23}

if __name__ == "__main__":
    test()
    print("OK!")

