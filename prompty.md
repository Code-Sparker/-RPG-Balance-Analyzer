Reverse Prompt Engineering – system balansu postaci RPG

Autor: [Wpisz swoje imię i nazwisko]
Przedmiot: Informatyka
Temat: Reverse Prompt Engineering
Cel: Przebudowa programu RPG z wersji A do systemu analizującego balans postaci z wykorzystaniem NumPy.

1. Prompt – zmiana struktury danych

Cel: Zastąpienie listy słowników tablicami NumPy.

Prompt wysłany do AI:

Przebuduj sposób przechowywania danych postaci RPG.

Wymagania:

Zastosuj bibliotekę NumPy.
Nazwy postaci umieść w tablicy NAZWY.
Statystyki umieść w dwuwymiarowej tablicy STATYSTYKI.
Zachowaj kolejność statystyk: HP, atak, obrona, szybkość.
Ustaw typ danych statystyk na float.
Utwórz osobną tablicę wag WAGI o wartościach 0.20, 0.40, 0.25, 0.15.
Utwórz stałą KOLUMNY z nazwami statystyk.
Zachowaj wszystkie osiem początkowych postaci.

Kryterium sprawdzenia: tablica statystyk musi mieć osiem wierszy i cztery kolumny, a liczba nazw musi odpowiadać liczbie postaci.

2. Prompt – normalizacja i obliczanie siły

Cel: Zastąpienie starego wzoru obliczania siły normalizacją min-max.

Prompt wysłany do AI:

Dodaj do programu funkcje normalizuj(dane) i oblicz_sile(dane).

Wymagania:

Zastosuj normalizację min-max osobno dla każdej kolumny.
Wykorzystaj np.min i np.ptp.
Zabezpiecz stałe kolumny przed dzieleniem przez zero.
Wykorzystaj np.divide, out i where.
Oblicz siłę jako iloczyn macierzy znormalizowanych danych i wag.
Zastosuj mnożenie macierzowe NumPy @.
Nie używaj pętli do obliczania siły każdej postaci osobno.

Kryterium sprawdzenia: wartości znormalizowane muszą mieścić się w przedziale 0–1, a kolumny o stałych wartościach muszą zawierać same zera.

3. Prompt – role postaci i ranking

Cel: Dodanie automatycznej klasyfikacji postaci i rankingu.

Prompt wysłany do AI:

Dodaj funkcję okresl_role(dane) i system rankingu.

Wymagania:

Postać z atakiem co najmniej 35 i szybkością co najmniej 12 otrzymuje rolę Szturmowiec.
Postać z HP co najmniej 120 i obroną co najmniej 18 otrzymuje rolę Obrońca.
Pozostałe postacie otrzymują rolę Wszechstronny.
Jeżeli postać spełnia oba warunki, pierwszeństwo ma Szturmowiec.
Wykorzystaj wektorowe operacje NumPy i np.select.
Utwórz ranking malejący według siły.
Przy identycznych wynikach zachowaj kolejność początkową, wykorzystując stabilne sortowanie.

Kryterium sprawdzenia: każda postać musi mieć jedną rolę, a ranking musi zawierać wszystkie postacie.

4. Prompt – macierz pojedynków

Cel: Symulowanie prawdopodobieństwa wygranej pomiędzy postaciami.

Prompt wysłany do AI:

Dodaj funkcję macierz_pojedynkow(sila).

Wymagania:

Oblicz różnice siły wszystkich par postaci za pomocą broadcastingu NumPy.
Zastosuj wzór logistyczny 1 / (1 + exp(-8 * różnica)).
Wynik musi być kwadratową macierzą.
Na przekątnej ustaw wartości 0.5.
Prawdopodobieństwa wygranej dwóch różnych postaci w przeciwnych kierunkach muszą sumować się do 1.
Nie stosuj zagnieżdżonych pętli.

Kryterium sprawdzenia: przekątna macierzy ma zawierać 0.5, a suma macierzy i jej transpozycji musi dawać macierz jedynek.

5. Prompt – walidacja danych

Cel: Zabezpieczenie programu przed błędnymi danymi.

Prompt wysłany do AI:

Dodaj funkcję waliduj(nazwy, dane).

Wymagania:

Sprawdź, czy macierz jest dwuwymiarowa.
Sprawdź, czy zawiera dokładnie cztery kolumny.
Liczba wierszy musi odpowiadać liczbie nazw.
Muszą istnieć przynajmniej dwie postacie.
Nazwy muszą być unikatowe.
Statystyki muszą być skończonymi liczbami.
Statystyki nie mogą być ujemne.
Przy niepoprawnych danych zgłaszaj ValueError z czytelnym komunikatem.
Wykorzystaj np.isfinite i np.any.

Kryterium sprawdzenia: funkcja musi wykrywać duplikaty, wartości ujemne, NaN, nieskończoność i nieprawidłowy kształt danych.

6. Prompt – średnie szanse i raport

Cel: Rozbudowanie wyników programu.

Prompt wysłany do AI:

Dodaj obliczanie średnich szans wygranej każdej postaci oraz czytelny raport.

Wymagania:

Wykorzystaj macierz pojedynków.
Oblicz średnią szansę wygranej z pozostałymi postaciami.
Nie uwzględniaj pojedynku postaci z samą sobą.
Wyświetl ranking, nazwę, rolę, siłę i średnią szansę wygranej.
Siłę pokazuj z dokładnością do czterech miejsc po przecinku.
Szanse wygranej pokazuj procentowo.
Dodaj statystyki ogólne, w tym średnią siłę i liczbę postaci.

Kryterium sprawdzenia: raport musi zawierać wszystkie postacie, a średnie szanse muszą być liczone bez przekątnej macierzy.

7. Prompt – eksport CSV

Cel: Dodanie zapisu wyników do pliku.

Prompt wysłany do AI:

Dodaj funkcję zapisz_csv(sciezka, nazwy, role, sila, srednie_szanse, ranking).

Wymagania:

Wykorzystaj bibliotekę csv.
Zapisuj dane w kodowaniu utf-8-sig.
Użyj separatora średnika.
Dodaj nagłówki: Miejsce, Postać, Rola, Siła, Średnia szansa wygranej.
Dane zapisuj w kolejności rankingu.
Numerację rozpocznij od 1.
Siłę zapisuj z czterema miejscami po przecinku.
Szanse zapisuj procentowo z dwoma miejscami po przecinku.
Przy otwieraniu pliku zastosuj newline="".

Kryterium sprawdzenia: plik CSV musi zawierać wszystkie postacie i poprawne polskie znaki.

8. Prompt – testy i integracja

Cel: Połączenie wszystkich funkcji w kompletny program.

Prompt wysłany do AI:

Dodaj funkcję testy() oraz końcową funkcję main().

Wymagania:

Przetestuj normalizację danych.
Przetestuj kolumny o stałych wartościach.
Przetestuj macierz pojedynków.
Sprawdź przekątną macierzy.
Sprawdź symetrię prawdopodobieństw.
Wykorzystaj np.testing.assert_allclose.
W funkcji main() wykonaj walidację, testy, obliczenia siły, klasyfikację, ranking, pojedynki i eksport CSV.
Dodaj punkt wejścia if __name__ == "__main__":.
Zachowaj podział programu na funkcje.

Kryterium sprawdzenia: program ma uruchamiać się bez błędów, przechodzić testy i generować plik CSV.

9. Podsumowanie

Przebudowa programu została podzielona na osiem etapów. Każdy prompt odpowiada za konkretną funkcjonalność.

Dzięki temu możliwe jest stopniowe rozwijanie programu i sprawdzanie poprawności poszczególnych elementów.

Kolejność przebudowy:

Struktura danych.
Normalizacja i obliczanie siły.
Role i ranking.
Macierz pojedynków.
Walidacja.
Średnie szanse i raport.
Eksport CSV.
Testy i integracja.