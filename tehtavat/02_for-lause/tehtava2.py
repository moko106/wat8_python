# Tehtävä 2: Tarkoituksena on palauttaa lista, jossa on funktion syötteenä annetun luvun kertotaulu 10:een asti.


def kertotaulu(n):
    pass
  

def test_kertotaulu():
    assert kertotaulu(10) == [10,20,30,40,50,60,70,80,90,100]
    assert kertotaulu(2) == [2,4,6,8,10,12,14,16,18,20]
    assert kertotaulu(0) == [0,0,0,0,0,0,0,0,0,0]

if __name__ == "__main__":
    test_kertotaulu()
    print("OK!")