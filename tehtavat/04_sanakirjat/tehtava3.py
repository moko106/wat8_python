# Tehtävä 3: Arvojen summa
# Funktiolle annetaan sanakirja, jonka arvot ovat lukuja.
# Palauta arvojen summa.

def summa_dict(tiedot: dict):
    pass


d1 = {"Matti": 10, "Liisa": 8, "Pekka": 6}
d2 = {"A": 1, "B": 2, "C": 3}
d3 = {}


def test():
    assert summa_dict(d1) == 24
    assert summa_dict(d2) == 6
    assert summa_dict(d3) == 0


if __name__ == "__main__":
    print(summa_dict(d1))
    print(summa_dict(d2))
    print(summa_dict(d3))
    test()
    print("OK!")