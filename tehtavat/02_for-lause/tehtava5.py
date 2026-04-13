# Tehtävä 5: Funktiolle annetaan syötteeksi lista ja funktio palauttaa sen pituuden (len())
# Selvitä, mitä tarkoittaa, kun annetussa pohjassa on suluissa lista=[] (Vinkki: Oletusparametri)

def pituus(lista=[]):
    pass
  

l1 = [-15, 18, -6, 1, -4, 6, 0, 15]
l2 = [18, -13, 13, -5, -2, 1, 13, -19, -1, -12, 19, 2, -20, 10, 10, -14, 2]
l3 = [-20, 9, -4, 4, 16, 16, 15, -16, 9, -17, 18, 5, -3, 5, -7, -3, 14, -13, 5, -16]

def test():
    assert pituus(l1) == 8
    assert pituus(l2) == 17
    assert pituus(l3) == 20
    assert pituus() == 0

if __name__ == "__main__":
    test()
    print("OK!")