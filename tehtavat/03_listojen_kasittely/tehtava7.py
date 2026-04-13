# Tehtävä 7: Yli viisi kirjainta. Funktiolle annetaan lista sanoja.
# Palauta *lukumäärä* niistä sanoista, joiden pituus on yli 5 kirjainta.

def yli_viisi_kirjainta(sanat: list):
    pass


l1 = [
    "python", "kissa", "ohjelmointi", "tee", "funktio",
    "tietokone", "hiiri", "näppäimistö", "ruutu", "muisti"
]

l2 = [
    "auto", "juna", "laiva", "tie", "pyörä", "bussi"
]

l3 = []

l4 = [
    "yliopisto", "koulu", "oppikirja", "vihko", "tietojenkäsittely",
    "opiskelija", "opettaja", "kurssi"
]


def test():
    assert yli_viisi_kirjainta(l1) == 5
    assert yli_viisi_kirjainta(l2) == 0
    assert yli_viisi_kirjainta(l3) == 0
    assert yli_viisi_kirjainta(l4) == 6


if __name__ == "__main__":
    print(yli_viisi_kirjainta(l1))
    print(yli_viisi_kirjainta(l2))
    print(yli_viisi_kirjainta(l3))
    print(yli_viisi_kirjainta(l4))
    test()
    print("OK!")