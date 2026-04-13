#Tehtävä 1: Kirjoita funktio, joka yhdistää kaksi listaa yhdeksi sanakirjaksi, jossa ensimmäinen lista toimii avaimena ja jälkimmäinen kunkin avaimen arvona.
#Esimerkiksi oppilaiden kokeiden arvosanat voisivat olla
#[Matti, Mikko, Miro]
#[7.5, 8, 10]
#{Matti: 7.5, Mikko: 8, Miro: 10}

def yhdista(otsikot: list, arvot: list) -> dict:
    pass

listat=[
    (["Matti", "Mikko", "Miro"],[7.5,8,10]),
    (["Pirkko", "Marjaana"], [5, 9.75])
]

for i in listat:
    print(yhdista(i[0], i[1]))

def test():
    assert yhdista(listat[0][0], listat[0][1]) == {"Matti": 7.5, "Mikko": 8, "Miro": 10}
    assert yhdista(listat[1][0], listat[1][1]) == {"Pirkko": 5, "Marjaana": 9.75}

if __name__ == "__main__":
    test()
    print("OK!")
