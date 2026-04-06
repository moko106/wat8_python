# Python-osio

Tässä osiossa tutustut Python-ohjelmoinnin perusteisiin ja datan käsittelyyn. Tehtävät on jaettu osioihin, joista jokaisessa on muutamia tehtäviä. Kopioi tehtävän koodi editoriin, kirjoita funktio. Koodissa on valmiit testit, joilla voit kokeilla toimiiko ohjelma oikein.

## Osio 1

Tässä tutustut funktion käsitteeseen. Funktio alkaa aina def-sanalla, jonka jälkeen tulee funktion nimi. Tämän perässä suluissa voidaan antaa parametreja kullekin funktiolle. Esimerkiksi seuraava funktio laskee kahden luvun tulon.

```python
def tulo(a,b):
  return a*b
```

Funktion ensimmäisen rivin loppuun tulee kaksoispiste ja funktioon kuuluvat ohjelmointilauseet sisennetään. Usein funktion halutaan tekevän jotain syötteelle ja palauttavan uuden syötteen. Ylemmässä esimerkissä parametrit kerrotaan keskenään ja palautetaan ```return```-komennolla.

Parillisuuden voi tarkistaa ```%```-operaattorilla, joka on jakojäännösoperaattori. Laskussa 3 jaettuna 2:lla jakojäännös on 1 ja 20 jaettuna 5:llä, jakojäännös on 0 eli luku menee tasan 20:een.

## Osio 2

### For-lause

Tietokone on hyvin yksinkertainen, mutta sen nerokkuus piilee sen kyvyssä tehdä yksinkertaisia asioita monta peräjälkeen. For-lause, silmukka on erinomainen keino tähän. For-lausetta tuetaan usein ”in range” rajoittimella:
```python
for i in range (0,10):
 print(i)
```
Tämä ohjelma tulostaa ruudulle numerot 0-9 (huom. ei 10!)

Range-rajoitin sisältää myös vaihtoehtoisen muuntimen
```python
for i in range (0,25,3):
 print(i)
```

Tämä ohjelma tulostaa kolmen kertotaulun lukuun 24 asti, koska luku 3 osoittaa askeleen (step), jonka ohjelma hyppää yli joka kerta (0, 3, 6…)

### Lista

Muuttujien avulla säilötään yksittäisiä tietoja, listoilla voidaan säilöä tietokokonaisuuksia. Pythonissa listaan voi tallentaa mitä tahansa tietotyyppiä (vrt. monet muut, joissa lista sisältää vain yhdentyyppistä dataa (int, str, float jne.). Lista määritellään hakasuluilla.

```python
lista=["Matematiikka", "Fysiikka", "Kemia"]
print(lista)
```

Listaan voi lisätä elementtejä ```lista.append()``` komennolla. Listasta voi poistaa elementtejä 

i) ```lista.remove()``` -komennolla, jossa sulkuihin laitetaan se tieto, joka halutaan poistaa
ii) ```lista.pop()``` -komennolla, jossa sulkuihin laitetaan järjestysnumero, jonka tieto halutaan poistaa

Huom! Python - kuten usein muutkin ohjelmointikielet - aloittavat laskemisen 0:sta

Kokeilu 1
Kokeile, miten eri rivit muuttavat listaa!
```python
lista=["Mikko", "Matti", "Maija", "Liisa"]
print(lista)
lista.append("Viljami")
print(lista)
print(lista[1])
lista.pop(0)
print(lista)
lista.remove("Maija")
print(lista)
```

Kokeilu 2
Listan läpi voi ajaa myös silmukan, esimerkiksi for-lauseen.
```python
lista=["Mikko", "Matti", "Maija", "Liisa"]
for i in lista:
 print(i)
```

## Osio 3

Tässä osiossa ei tule juurikaan uutta infoa. Lue jokaisen tehtävänannon alussa oleva tehtävänanto huolella: sieltä löydät myös vinkkejä.
