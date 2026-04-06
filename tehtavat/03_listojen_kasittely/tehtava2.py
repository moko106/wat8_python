# Tehtävä 2: Kirjoita ohjelma, joka laskee listan keskiarvon. Vinkki: käytä valmiita sum() ja len() -funktioita.

def keskiarvo(luvut: list):
    pass

l1 = [-15, 18, -6, 1, -4, 6, 0, 15, -6, -2, 17, 11, -6, 10, -2, -7, 13, -3, 19, 0]
l2 = [18, -13, 13, -5, -2, 1, 13, -19, -1, -12, 19, 2, -20, 10, 10, -14, 2, -10, -1, -17]
l3 = [-20, 9, -4, 4, 16, 16, 15, -16, 9, -17, 18, 5, -3, 5, -7, -3, 14, -13, 5, -16]

def test():
    assert keskiarvo(l1) == 2.95
    assert keskiarvo(l2) == -1.3
    assert keskiarvo(l3) == 0.85


if __name__ == "__main__":
    print(keskiarvo(l1))
    print(keskiarvo(l2))
    print(keskiarvo(l3))
    test()
    print("OK!")