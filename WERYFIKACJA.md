WERYFIKACJA PROJEKTU – RPG BALANCE ANALYZER

Autor: [Wpisz imię i nazwisko]
Temat: Reverse Prompt Engineering – system balansu postaci RPG

1. Cel testowania

Celem testowania było sprawdzenie poprawności działania programu analizującego balans postaci RPG.

Sprawdzono obliczenia NumPy, normalizację statystyk, przypisywanie ról, ranking, walidację danych, macierz pojedynków, średnie szanse wygranej oraz eksport CSV.

2. Wyniki testów automatycznych

Wykonano polecenie:

bash
python -m unittest test_main -v


Wynik rzeczywistego uruchomienia:

Liczba testów: 16
Testy zakończone powodzeniem: 16
Testy zakończone błędem: 0
Czas wykonania: 0.112 sekundy
Końcowy status: OK
3. Tabela wymaganie → działanie → dowód
Wymaganie	Działa?	Dowód
Dane w tablicach NumPy	TAK	NAZWY, STATYSTYKI
Normalizacja min-max	TAK	test_normalizacja
Obsługa stałych kolumn	TAK	test_stala_kolumna
Ważone obliczanie siły	TAK	oblicz_sile()
Ranking postaci	TAK	test_ranking
Stabilny ranking	TAK	test_stabilny_ranking_przy_remisie
Przypisywanie ról	TAK	test_role
Walidacja danych	TAK	Testy duplikatów, NaN i wartości ujemnych
Macierz pojedynków	TAK	test_macierz_pojedynkow
Obsługa remisów	TAK	test_remis
Średnie szanse wygranej	TAK	test_srednie_szanse
Eksport CSV	TAK	test_csv
4. Wynik rankingu

Po uruchomieniu programu otrzymano następującą kolejność:

Miejsce	Postać	Siła
1	Berserker	0.5349
2	Łotrzyk	0.5106
3	Paladyn	0.4889
4	Mag	0.4750
5	Łucznik	0.4587
6	Wojownik	0.4538
7	Strażnik	0.4500
8	Druid	0.3950

Średnia siła wszystkich postaci wyniosła 0.4709.

Najsilniejszą postacią został Berserker.

5. Eksport CSV

Program poprawnie utworzył plik ranking_postaci.csv.

Zastosowano:

Kodowanie UTF-8 z BOM.
Separator średnik.
Nagłówki: Miejsce, Postać, Rola, Siła, Średnia szansa wygranej.
Numerowanie miejsc od 1.
Cztery miejsca po przecinku dla siły.
Procentowy format średniej szansy wygranej.

Poprawność zapisu sprawdzono testem test_csv, który zakończył się powodzeniem.

6. Dodatkowe przypadki testowe

Sprawdzono:

Kolumny zawierające identyczne wartości.
Dwie postacie o identycznej sile.
Zduplikowane nazwy postaci.
Ujemne statystyki.
Wartości NaN.
Wartości nieskończone.
Nieprawidłowy wymiar macierzy.
Dane zawierające tylko jedną postać.

Wszystkie przygotowane testy zakończyły się powodzeniem.

7. Dwie korekty promptów
Korekta 1 – normalizacja stałych kolumn

Problem: Przy identycznych wartościach statystyki w kolumnie rozpiętość wynosi zero. Zwykła normalizacja mogłaby prowadzić do dzielenia przez zero.

Wprowadzona poprawka: Wymaganie wykorzystania np.divide, parametru out oraz where.

Test: test_stala_kolumna.

Wynik: Test zakończył się powodzeniem. Stałe kolumny zawierają zera.

Korekta 2 – remisy w rankingu i pojedynkach

Problem: Postacie o identycznej sile powinny mieć równe szanse wygranej, a ranking powinien zachowywać kolejność wejściową.

Wprowadzona poprawka: Wymaganie ustawienia przekątnej macierzy na 0.5 oraz zastosowania stabilnego sortowania np.argsort(-sila, kind="stable").

Testy:

test_remis
test_stabilny_ranking_przy_remisie

Wynik: Oba testy zakończyły się powodzeniem.

8. Wnioski

Przebudowany program wykorzystuje bibliotekę NumPy do wektorowego przetwarzania statystyk postaci.

Dodano normalizację, ważone obliczanie siły, klasyfikację ról, ranking, walidację danych oraz model prawdopodobieństwa wygranej w pojedynkach.

Program generuje raport i eksportuje wyniki do CSV.

Przygotowane testy automatyczne potwierdziły poprawność sprawdzonych funkcjonalności.

Projekt spełnia główne wymagania techniczne zadania. Pełną zgodność z oryginalną wersją docelową należy potwierdzić przez porównanie z jej kompletnym kodem.