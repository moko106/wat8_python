# Tehtävä 4: Funktiolle annetaan merkkijono syötteenä ja sen pitäisi palauttaa se listana


def str_to_list(string):
    pass
  

def test():
    assert str_to_list("python") == ["p", "y", "t", "h", "o", "n"]
    assert str_to_list("") == []

if __name__ == "__main__":
    test()
    print("OK!")