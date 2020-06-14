# XML Biblia po Polsku Open Song
Poprawki pliku xml Biblii Warszawskej programu Open Song.

## Autor poprawek
> Górka Mateusz, \
> [kzswieb.eu](kzswieb.eu)

## Autor plików
> Nieznany

## Open Song
Strona programu [Open Song](http://www.opensong.org/)

___
## Zakres poprawek

### PBW
- Poprawiona interpunkcja
    - usunięto spacja przed ",.;:!?"
    - dodano spację po ".,"

- Zmiana nazw ksiąg na krótsze

- Dostosowanie podziału wersów i rozdziałów do KJV

    Podział werstów i rozdziałów PBW różni się wzgędem KJV, więc aby Open Song wyświetlał poprawnie wszystkie wersety wprowadzono wiele zmian, np.:

    - w Psalmach werset 1 jest często połączony z 2
    - Jeżeli podział rozdziału jest w różnych miejscach początkowe wersety znajdują się w poprzednim rozdziale, lub końcowe w następnym.

### Nowe Przymierze
- Poprawiona interpunkcja
    - przecinek zamiast kropek w odpowiednichm miejscach (tylko literówki, nie zmiana budowy zdań)
    - sprawdzenie spacji przed i po znakach ",.;:!?"

- Poprawa układu tagów

- Dostosowanie podziału wersów i rozdziałów do KJV
    - 3 Jana 1,15 i 14 <- połączone
    - Objawienie 12,17 i 18 <- połączone

___
## Skrypty
### roznice_w_podziale_py
Program zwraca miejsca w których podział ksiąg, rozdziałów i wersetów różni się ilościowo.

### polacz_pliki_py
Program łączy dwa pliki Biblii ze sobą, poprzez połączenie wersetów.

Pozwala to połączyć dwa różne tłumaczenia ze sobą.

- W przypadku większej liczby wersetów jednego z tłumaczeń różnicę dodaje do ostatniego wersetu rozdziału, oraz zwraca ostrzeżenie.
- W przypadku różnej liczby rozdziałów zwraca błąd i przerywa działanie.
- W przypadku różnej liczby ksiąg zwraca błąd i przerywa działanie.

___
## Planowane zmiany
- Kolejne polskie przekłady

## Tagi
PBW, PBT, Biblia Warszawska, Brytyjka, Kościół, Bóg,