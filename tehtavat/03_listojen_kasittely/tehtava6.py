# Tehtävä 6: Jaa luvut positiivisiin ja negatiivisiin
# Funktiolle annetaan lista lukuja.
# Palauta kaksi listaa:
# 1) positiiviset luvut
# 2) negatiiviset luvut
# Nollia ei lisätä kumpaankaan listaan.
# Palauta tulos tuplena: (positiiviset, negatiiviset)

def jaa_luvut(luvut: list):
    pass

l1 = [-3, -1, 0, 1, 4, -5]
l2 = [0, 0, 0]
l3 = [5, 10, -2, -8, 3]
l4 = []

def test():
    assert jaa_luvut(l1) == ([1, 4], [-3, -1, -5])
    assert jaa_luvut(l2) == ([], [])
    assert jaa_luvut(l3) == ([5, 10, 3], [-2, -8])
    assert jaa_luvut(l4) == ([], [])

if __name__ == "__main__":
    print(jaa_luvut(l1))
    print(jaa_luvut(l2))
    print(jaa_luvut(l3))
    print(jaa_luvut(l4))
    test()
    print("OK!")
