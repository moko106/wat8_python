# Tehtävä 5: Mediaani on listan keskimmäinen arvo, kun aineisto on suuruusjärjestyksessä. Kirjoita 3 funktiota:
# 1) Funktiolle annetaan lista, jossa on pariton määrä lukuja. Palauta keskimmäinen. Vinkki: kokeile // laskutoimitus.
# 2) Funktiolle annetaan lista, jossa on parillinen määrä lukuja. Palauta kahden keskimmäisen keskiarvo.
# 3) Funktio, joka tarkistaa onko listan pituus parillinen vai pariton ja kutsuu sen mukaista ohjelmaa (1 tai 2)

def mediaani_pariton(luvut: list):
    pass

def mediaani_parillinen(luvut: list):
    pass

def mediaani(luvut: list):
    pass

l1 = [22, 20, 14, 40, 24, 2, 5, 23, 30]
l2 = [32, 44, 39, 50, 8, 38, 43, 16, 28]
l3 = [4, 11, 47, 23, 14, 33, 15, 10, 43, 17]
l4 = [28, 8, 4, 5, 28, 19, 38, 40, 4, 29]
l5 = [4, 43, 44, 33, 42, 1, 1, 40, 24, 48, 18, 34, 2, 49, 9, 30, 11, 43, 30, 15, 30, 6, 48, 30, 9, 42, 42, 11, 4, 38, 39, 12, 42, 13, 5, 25, 49, 41, 1, 34, 1, 48, 41, 34, 49, 43, 40, 18, 19, 40, 29]
l6 = [35, 24, 24, 25, 25, 39, 21, 44, 46, 32, 45, 32, 24, 26, 16, 9, 24, 19, 28, 3, 3, 24, 19, 42, 38, 50, 8, 11, 29, 21, 18, 44, 40, 25, 13, 27, 13, 23, 32, 36, 21, 7, 42, 41, 40, 7, 28, 1, 6, 16]

def test1():
    assert mediaani_pariton(l1) == 22
    assert mediaani_pariton(l2) == 38

def test2():
    assert mediaani_parillinen(l3) == 16.0
    assert mediaani_parillinen(l4) == 23.5

def test3():
    assert mediaani(l5) == 30
    assert mediaani(l6) == 24.5

if __name__ == "__main__":
    print("Funktio 1 (pariton määrä lukuja):")
    print(f'Testi 1 pitäisi olla 22, sinun funktio palauttaa: {mediaani_pariton(l1)}')
    print(f'Testi 2 pitäisi olla 38, sinun funktio palauttaa: {mediaani_pariton(l2)}')
    test1()
    print("Funktio 1 ok!")
    print("Funktio 2 (parillinen määrä lukuja):")
    print(f'Testi 3 pitäisi olla 16.0, sinun funktio palauttaa: {mediaani_parillinen(l3)}')
    print(f'Testi 4 pitäisi olla 23.5, sinun funktio palauttaa: {mediaani_parillinen(l4)}')
    test2()
    print("Funktio 2 ok!")
    print("Funktio 3 (yhdistetty):")
    print(f'Testi 5 pitäisi olla 30, sinun funktio palauttaa: {mediaani(l5)}')
    print(f'Testi 5 pitäisi olla 24.5, sinun funktio palauttaa: {mediaani(l6)}')
    print("Funktio 3 ok!")