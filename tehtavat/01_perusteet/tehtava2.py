# Tehtävä 2: Tyhjä nimi

def tervehdys(nimi):
    # Jos nimi on tyhjä, palauta "Hei tuntematon!"
    # Muuten: "Hyvää päivää <nimi>"
    pass


def test_tervehdys():
    assert tervehdys("") == "Hei tuntematon!"
    assert tervehdys("Matti") == "Hyvää päivää Matti"


if __name__ == "__main__":
    test_tervehdys()
    print("OK!")
