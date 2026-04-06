# Tehtävä 3: Kirjoita ohjelma, joka palauttaa pisimmän sanan listassa.

def pisin_sana(sanat: list):
    pisin=""
    for sana in sanat:
        #jos sana on pidempi kuin pisin, vaihda pisimmän tilalle nykyinen sana
        pass

l1 = ["industrialismi", "koriinheitto", "puola", "varrellinen","satunnaissuure",
      "punertavatukkainen", "analgeettisuus","kiisu","hellemekko","kuunnelma"]

l2 = ["poikkilakana","norsu","ulkoilujalkine","ruokailutauko","vesiliikunta",
      "rytmimusiikki","pilkkoutua","liikuntasota","miettimisaika","valokaapeli"]
l3 = ["maustevoi","valumuotti","kylpypyyhe","lei","huopanaula","sesonkiluonteisesti",
      "akileija","korkkipuu","sulo","lapsekkaasti"]

def test():
    assert pisin_sana(l1) == "punertavatukkainen"
    assert pisin_sana(l2) == "ulkoilujalkine"
    assert pisin_sana(l3) == "sesonkiluonteisesti"


if __name__ == "__main__":
    print(pisin_sana(l1))
    print(pisin_sana(l2))
    print(pisin_sana(l3))
    test()
    print("OK!")