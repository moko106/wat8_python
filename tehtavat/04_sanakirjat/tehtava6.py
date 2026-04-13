# Tehtävä 6: Keskiarvo sanakirjasta
# Funktiolle annetaan sanakirja, jonka arvot ovat lukuja.
# Palauta arvojen keskiarvo.
# Jos sanakirja on tyhjä, palauta 0.

def keskiarvo_dict(tiedot: dict):
    pass


d1 = {"Matti": 8, "Liisa": 10, "Pekka": 6}
d2 = {"A": 5}
d3 = {}


def test():
    assert keskiarvo_dict(d1) == 8.0
    assert keskiarvo_dict(d2) == 5.0
    assert keskiarvo_dict(d3) == 0


if __name__ == "__main__":
    print(keskiarvo_dict(d1))
    print(keskiarvo_dict(d2))
    print(keskiarvo_dict(d3))
    test()
    print("OK!")