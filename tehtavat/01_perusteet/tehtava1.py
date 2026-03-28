# Tehtävä 1: Tervehdys

def tervehdys(nimi):
    # Palauta teksti: "Hyvää päivää <nimi>"
    pass


def test_tervehdys():
    assert tervehdys("Matti") == "Hyvää päivää Matti"
    assert tervehdys("Liisa") == "Hyvää päivää Liisa"


if __name__ == "__main__":
    test_tervehdys()
    print("Testit menivät läpi!")
