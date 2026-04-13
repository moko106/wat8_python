# Tehtävä 7: Useampi arvo per avain
# Funktiolle annetaan lista pareja (nimi, arvosana).
# Palauta sanakirja, jossa avain on nimi ja arvo lista arvosanoista.

def ryhmittele(tiedot: list) -> dict:
    pass


l1 = [("Matti", 8), ("Liisa", 9), ("Matti", 7), ("Pekka", 6)]
l2 = [("A", 1), ("A", 2), ("A", 3)]
l3 = []


def test():
    assert ryhmittele(l1) == {"Matti": [8, 7], "Liisa": [9], "Pekka": [6]}
    assert ryhmittele(l2) == {"A": [1, 2, 3]}
    assert ryhmittele(l3) == {}


if __name__ == "__main__":
    print(ryhmittele(l1))
    print(ryhmittele(l2))
    print(ryhmittele(l3))
    test()
    print("OK!")