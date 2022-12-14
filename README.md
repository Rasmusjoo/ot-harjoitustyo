# Tasohyppelypeli
Sovelluksessa käyttäjä voi liikkua kartalla väistellen esteitä ja vihollisia klassisen tasohyppelypelin tyyliin. Sovellus on yksinpeli. Pelissä pelaajalla on kolme elämää joita hän voi menettää kohdatessaan vihollisia. Vihollisia ei ainakaan vielä tässä vaiheessa pysty tuhoamaan. Keräämällä kolikoita pelaaja saa pisteitä. Taso läpäistään keräämällä sen lopussa oleva tähti.

## Huomio Python-versiosta
Sovellus on suunniteltu Python 3.8 järjestelmälle ja sitä uudemmille versioille. Testaamiseen on käytetty Pythonin versiota 3.10.6. Etenkin vanhempia versioita käyttäessä voi ilmetä ongelmia.

## Dokumentaatio

[Vaatimusmaarittely](platformer/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](platformer/dokumentaatio/tuntikirjanpito.md)

[Changelog](platformer/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](platformer/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](platformer/dokumentaatio/kaytto-ohje.md)

## Julkaisut
Linkki ensimmäiseen julkaisuun löytyy alta.

[Julkaisu 1](https://github.com/Rasmusjoo/ot-harjoitustyo/releases/tag/viikko5)

[Julkaisu 2](https://github.com/Rasmusjoo/ot-harjoitustyo/releases/tag/viikko6)

## Asennus
Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Pelin ohjaus

Pelissä liikutaan nuolinäppäimin oikealle tai vasemmalle. Lisäksi pelissä on kaksi eri suuruista hyppyä, 
joista pienempi tehdään painamalla SPACE painiketta ja suurempi ylänuolella. Hyppyjä ei voi suorittaa ilmassa.

Keskeyttää pelin voi painamalla P painiketta ja lopettaasen voi Q painikkeesta. Peli sammuu painamalla rastia yläkulmassa.
Pelin loputtua sen voi aloittaa uudelleen painamalla S painiketta.
