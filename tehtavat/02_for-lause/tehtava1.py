# Tehtävä 1: Lisää luvut 1:stä n:ään asti listaan ja palauta se.

def loop(n):
  tulos = []
  for i in range(1,n+1):
     tulos.append(i)
  return tulos
  

def test_loop():
    assert loop(10) == [1,2,3,4,5,6,7,8,9,10]
    assert loop(2) == [1,2]
    assert loop(0) == []

if __name__ == "__main__":
    test_loop()
    print("OK!")
