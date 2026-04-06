# Tehtävä 3: Funktiolle annetaan kaksi syötettä: a ja b.
# Jos a on suurempi kuin b, funktio palauttaa -1
# Muuten funktio palauttaa kaikki parilliset luvut näiden kahden väliltä (sisältäen sekä a että b)


def parilliset(a,b):
    pass
  

def test_parilliset():
    assert parilliset(2,10) == [2,4,6,8,10]
    assert parilliset(1,1) == []
    assert parilliset(11,15) == [12,14]

if __name__ == "__main__":
    test_parilliset()
    print("OK!")