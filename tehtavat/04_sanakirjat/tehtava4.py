# Tehtävä 4: Suurin arvo
# Palauta se avain, jolla on sanakirjan suurin arvo.
# Jos sanakirja on tyhjä, palauta None.

def suurin_avain(tiedot: dict):
    pass


d1 = {"omena": 5, "banaani": 2, "päärynä": 7}
d2 = {"A": 1}
d3 = {}


def test():
    assert suurin_avain(d1) == "päärynä"
    assert suurin_avain(d2) == "A"
    assert suurin_avain(d3) is None


if __name__ == "__main__":
    print(suurin_avain(d1))
    print(suurin_avain(d2))
    print(suurin_avain(d3))
    test()
    print("OK!")