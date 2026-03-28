# 🐍 Python-tehtävät

Tervetuloa harjoittelemaan Pythonin perusteita!

## 📌 Ohjeet

* Kopioi tehtävän koodi omaan `.py`-tiedostoon
* Täydennä funktio kohtaan `pass`
* Aja ohjelma
* Jos kaikki toimii, näet viestin: **"OK!"** tai **"Testit menivät läpi!"**

---

# ✅ Tehtävä 1: Tervehdys

Tee funktio `tervehdys`, joka palauttaa tekstin:

> "Hyvää päivää <nimi>"

### 💡 Esimerkki:

`tervehdys("Matti")` → `"Hyvää päivää Matti"`

```python
def tervehdys(nimi):
    # Palauta teksti: "Hyvää päivää <nimi>"
    pass


def test_tervehdys():
    assert tervehdys("Matti") == "Hyvää päivää Matti"
    assert tervehdys("Liisa") == "Hyvää päivää Liisa"


if __name__ == "__main__":
    test_tervehdys()
    print("Testit menivät läpi!")
```

---

# ✅ Tehtävä 2: Tyhjä nimi

Muokkaa funktiota niin, että:

* Jos nimi on tyhjä (`""`) → palautetaan `"Hei tuntematon!"`
* Muuten → `"Hyvää päivää <nimi>"`

```python
def tervehdys(nimi):
    # Jos nimi on tyhjä, palauta "Hei tuntematon!"
    # Muuten: "Hyvää päivää <nimi>"
    pass


def test_tervehdys():
    assert tervehdys("") == "Hei tuntematon!"
    assert tervehdys("Matti") == "Hyvää päivää Matti"


if __name__ == "__main__":
    test_tervehdys()
    print("OK!")
```

---

# ✅ Tehtävä 3: Summa

Tee funktio, joka laskee kahden luvun summan.

```python
def summa(a, b):
    # Palauta lukujen summa
    pass


def test_summa():
    assert summa(2, 3) == 5
    assert summa(-1, 1) == 0


if __name__ == "__main__":
    test_summa()
    print("OK!")
```

---

# ⭐ Tehtävä 4: Luku on parillinen

Tee funktio, joka kertoo onko luku parillinen.

* Palauta `True`, jos luku on parillinen
* Muuten palauta `False`

```python
def parillinen(luku):
    # Palauta tieto, onko luku parillinen
    pass


def test_parillinen():
    assert parillinen(10) == True
    assert parillinen(31) == False


if __name__ == "__main__":
    test_parillinen()
    print("OK!")
```

---

## 🚀 Bonus

Kun saat kaikki tehtävät toimimaan:

* Kokeile lisätä omia testejä
* Muuta tulostuksia
* Tee oma funktio!

---
