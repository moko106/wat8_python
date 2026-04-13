# Tehtävä 5: Suodata sanakirja
# Palauta uusi sanakirja, jossa on vain ne avaimet,
# joiden arvo on suurempi kuin annettu raja.

def suodata(tiedot: dict, raja: int):
    pass


d1 = {"A": 3, "B": 7, "C": 10, "D": 2}
d2 = {"x": 1, "y": 2}
d3 = {}


def test():
    assert suodata(d1, 5) == {"B": 7, "C": 10}
    assert suodata(d2, 3) == {}
    assert suodata(d3, 1) == {}


if __name__ == "__main__":
    print(suodata(d1, 5))
    print(suodata(d2, 3))
    print(suodata(d3, 1))
    test()
    print("OK!")