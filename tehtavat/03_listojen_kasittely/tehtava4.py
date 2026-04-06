# Tehtävä 4: Kirjoita ohjelma, joka palauttaa listan suuruusjärjestyksessä. Vinkki: käytä sorted()-funktiota.

def lajiteltu(luvut: list):
    pass

l1 = [-15, 18, -6, 1, -4, 6, 0, 15, -6, -2, 17, 11, -6, 10, -2, -7, 13, -3, 19, 0]
l2 = [18, -13, 13, -5, -2, 1, 13, -19, -1, -12, 19, 2, -20, 10, 10, -14, 2, -10, -1, -17]
l3 = [-20, 9, -4, 4, 16, 16, 15, -16, 9, -17, 18, 5, -3, 5, -7, -3, 14, -13, 5, -16]

def test():
    assert lajiteltu(l1) == [-15, -7, -6, -6, -6, -4, -3, -2, -2, 0, 0, 1, 6, 10, 11, 13, 15, 17, 18, 19]
    assert lajiteltu(l2) == [-20, -19, -17, -14, -13, -12, -10, -5, -2, -1, -1, 1, 2, 2, 10, 10, 13, 13, 18, 19]
    assert lajiteltu(l3) == [-20, -17, -16, -16, -13, -7, -4, -3, -3, 4, 5, 5, 5, 9, 9, 14, 15, 16, 16, 18]


if __name__ == "__main__":
    print(lajiteltu(l1))
    print(lajiteltu(l2))
    print(lajiteltu(l3))
    test()
    print("OK!")