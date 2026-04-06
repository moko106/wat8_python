# Tehtävä 1: Vain positiiviset. Funktiolle annetaan syötteenä lista ja sen pitäisi palauttaa kyseisen listan positiiviset luvut.

def positiiviset(luvut: list):
    pass


l1 = [-1,-2,-3,1]
l2 = [0,1,2,3,-1]
l3 = []

def test():
    assert positiiviset(l1) == [1]
    assert positiiviset(l2) == [1,2,3]
    assert positiiviset(l3) == []


if __name__ == "__main__":
    print(positiiviset(l1))
    print(positiiviset(l2))
    print(positiiviset(l3))
    test()
    print("OK!")
