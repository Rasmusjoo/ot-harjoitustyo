# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on seuraava:

```mermaid
classDiagram
    Assets --> Sprites

    class Assets{-pictures}

    class Sprites

```

## Sovelluslogiikka

Ohjelman sovelluslogiikan muodostavat luokat Level ja Gameloop. Level vastaa tason luomisesta ja sen sisällöstä. Gameloop ohjaa tason tapahtumia ja pelitiloja.

```mermaid
classDiagram
    Level --> Gameloop

    class Level

    class Gameloop

```

## Päätoiminnallisuudet

### Liikkuminen

Liikkuminen toimii seuraavan kuvan mukaisesti. Oletetaan, että peli on jo käynnissä ja pelaajan ntiellä ei ole estettä.

```mermaid
sequenceDiagram
actor U as User
participant G as Gameloop
participant L as Level

U->>G:painallus
alt painallus oikea tai vasen nuolinäppäin
G->>+L:siirrä hahmoa sivusuunnassa
L->>-G:hahmo siirtyy haluttuun suuntaan
else painallus SPACE tai ylös
G->>+L:jump() tai superjump()
L->>-G:hahmo hyppää
end



```
