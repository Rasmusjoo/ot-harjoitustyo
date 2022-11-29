# Tasohyppelypeli
Sovelluksessa käyttäjä voi liikkua kartalla väistellen esteitä ja vihollisa klassisen tasohyppelypelin tyyliin. Sovellus on yksinpeli. Pelissä pelaajalla on kolme elämää joita hän voi menettää kohdatessaan vihollisia. Keräämällä kolikoita pelaaja saa pisteitä.

## Huomio Python-versiosta
Soovellus on suunniteltu Python 3.8 järjestelmälle ja sitä uudemmille versioille. Testaamiseen on käytetty Pythonin versiota 3.10.6. Etenkin vanhempia versioita käyttäessä voi ilmetä ongelmia.

## Dokumentaatio

[Vaatimusmaarittely](platformer/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](platformer/dokumentaatio/tuntikirjanpito.md)

[Changelog](platformer/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](platformer/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet komennolla: poetry install
2. Suorita vaadittavat alustustoimenpiteet komennolla: poetry run invoke build
3. Käynnistä sovellus komennolla: poetry run invoke start

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:

poetry run invoke start

### Testaus
Testit suoritetaan komennolla:

poetry run invoke test

### Testikattavuus
Testikattavuusraportin voi generoida komennolla:

poetry run invoke coverage report

Raportti generoituu htmlcov-hakemistoon.

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

poetry run invoke lint
