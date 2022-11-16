### Monopolin luokkakaavio
``` mermaid
classDiagram
    Ruutu "40" --> "1" Pelilauta
    Pelaaja "2-8" --> "1" Pelilauta
    Pelaaja "1" --> "1" Pelinappula
    Pelinappula "0-8" --> "1" Ruutu
    Hotelli "0-1" --> "1" Ruutu
    Talo "0-4" --> "1" Ruutu
    Asemat ja laitokset "*" --> "*" Ruutu
    Sattuma ja yhteismaa "*" --> "*" Ruutu
    Normaalitkadut "*" --> "*" Ruutu
    Pelilauta "1" --> "1" Aloitusruutu
    Pelilauta "1" --> "1" Vankila

    class Pelilauta

    class Pelaaja{
    -Rahamäärä 
    }

    class Ruutu{
    -seuraava ruutu
    }
    
    class Pelinappula
    
    class Hotelli
    
    class Talo
    
    class Aloitusruutu{
    -toiminto
    }
    
    class Vankila{
    -toiminto
    }
    
    class Sattuma ja yhteismaa{
    -kortti
    -toiminto
    }
    
    class Asemat ja laitokset{
    -toiminto
    }
    
    class Normaalit kadut{
    -kadunnimi
    -toiminto
    }

```
