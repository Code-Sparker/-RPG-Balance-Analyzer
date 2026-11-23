# WERYFIKACJA PROJEKTU – RPG BALANCE ANALYZER

## 1. Cel weryfikacji

Celem weryfikacji było sprawdzenie, czy program RPG Balance Analyzer realizuje wymagania odtworzone na podstawie analizy wersji docelowej.

Sprawdzono poprawność obliczeń, normalizację statystyk, ranking postaci, przypisywanie ról, walidację danych, symulację pojedynków oraz eksport wyników do pliku CSV.

## 2. Zakres przeprowadzonych testów

| Wymaganie | Sposób sprawdzenia | Wynik |
|---|---|---|
| Wykorzystanie NumPy | Sprawdzenie struktury danych i działania programu | Potwierdzone |
| Normalizacja min-max | Test wartości minimalnych i maksymalnych | Działa |
| Obsługa stałych kolumn | Test jednakowych wartości statystyki | Działa |
| Ważony wynik siły | Test obliczania siły | Przetestowane |
| Ranking postaci | Test kolejności wyników | Działa |
| Przypisywanie ról | Test przypisanych ról | Działa |
| Walidacja danych | Test nieprawidłowych danych | Działa |
| Macierz pojedynków | Test macierzy i symetrii wyników | Działa |
| Średnie szanse wygranej | Test obliczeń średnich | Działa |
| Eksport CSV | Odczyt wygenerowanego pliku | Działa |
| Filtrowanie postaci | Wymaga osobnego potwierdzenia | Niepotwierdzone |
| Statystyki zbiorcze | Wymaga osobnego potwierdzenia średnich, minimów i maksimów | Niepotwierdzone |

## 3. Testy jednostkowe

Testy jednostkowe przygotowano w pliku `test_main.py` z wykorzystaniem biblioteki `unittest`.

Sprawdzają one:

- normalizację statystyk,
- obsługę stałych kolumn,
- obliczanie siły postaci,
- tworzenie rankingu,
- stabilność rankingu przy remisie,
- przypisywanie ról,
- walidację danych wejściowych,
- macierz pojedynków,
- średnie szanse wygranej,
- eksport wyników do CSV,
- wybrane przypadki brzegowe.

Polecenie uruchamiające testy:

`python -m unittest test_main -v`

**Wynik uruchomienia:**

`Ran 20 tests in 0.097s`

`OK`

Wszystkie 20 testów zakończyło się powodzeniem.

## 4. Korekty i doprecyzowanie promptów – Reverse Prompt Engineering

### Korekta 1 – Obsługa stałych kolumn

**Prompt pierwotny:** PROMPT 2.

**Problem:**

Normalizacja min-max może prowadzić do dzielenia przez zero, gdy wszystkie postacie mają identyczną wartość danej statystyki.

**Doprecyzowanie wymagania:**

Program powinien wykrywać kolumny, w których minimum jest równe maksimum, i przypisywać im bezpieczną wartość znormalizowaną równą zero.

**Oczekiwany rezultat:**

Brak wartości NaN i nieskończoności w wyniku normalizacji.

**Dowód weryfikacji:**

Test `test_stala_kolumna` zakończył się wynikiem OK.

### Korekta 2 – Walidacja danych wejściowych

**Prompt pierwotny:** PROMPT 5.

**Problem:**

Nieprawidłowe dane mogą prowadzić do błędnych obliczeń lub nieczytelnych błędów programu.

**Doprecyzowanie wymagania:**

Walidacja powinna obejmować:

- powtarzające się nazwy postaci,
- wartości ujemne,
- wartości NaN,
- nieskończoność,
- nieprawidłowy wymiar tablicy,
- niezgodną liczbę nazw i zestawów statystyk.

**Oczekiwany rezultat:**

Program powinien zgłaszać `ValueError` dla niepoprawnych danych.

**Dowód weryfikacji:**

Testy `test_duplikaty`, `test_ujemne_dane`, `test_nan`, `test_nieskonczonosc`, `test_zly_wymiar` oraz `test_niezgodna_liczba_nazw_i_statystyk` zakończyły się wynikiem OK.

## 5. Weryfikacja działania programu

Program uruchomiono poleceniem:

`python main.py`

Wynik działania:

- przeprowadzono analizę 8 postaci,
- wygenerowano ranking postaci,
- przypisano role,
- obliczono siłę postaci,
- wygenerowano macierz pojedynków 8 × 8,
- obliczono średnie szanse wygranej,
- wyświetlono statystyki zbiorcze przedstawione przez program.

Najsilniejszą postacią według wygenerowanego rankingu został Berserker.

Program zakończył działanie bez błędów.

## 6. Weryfikacja eksportu CSV

Wygenerowany plik: `ranking_postaci.csv`.

Sprawdzono:

- obecność wszystkich 8 postaci,
- poprawność nagłówków,
- separator średnikowy,
- polskie znaki,
- zgodność kolejności rankingu z wynikiem programu,
- zapis siły postaci,
- zapis przypisanych ról,
- zapis średnich szans wygranej.

Plik został odczytany w PowerShell za pomocą polecenia:

`Get-Content .\ranking_postaci.csv -Encoding UTF8`

**Wynik:**

Eksport CSV zakończył się powodzeniem. Wszystkie 8 postaci zostało zapisanych poprawnie.

## 7. Podsumowanie

Projekt RPG Balance Analyzer został przygotowany w ramach zadania Reverse Prompt Engineering.

Program został rozwinięty etapowo za pomocą ośmiu głównych promptów, których celem było odtworzenie funkcjonalności wersji docelowej bez przekazywania modelowi kodu wersji B podczas procesu tworzenia.

Przeprowadzone testy potwierdziły poprawność sprawdzonych funkcjonalności programu.

Wykonano 20 testów jednostkowych i wszystkie zakończyły się wynikiem OK. Dodatkowo uruchomiono cały program i sprawdzono wygenerowany plik CSV.

Przetestowano również przypadki brzegowe dotyczące stałych kolumn oraz nieprawidłowych danych wejściowych.

Funkcje filtrowania i szczegółowych statystyk zbiorczych wymagają osobnego potwierdzenia. Pełna zgodność z wersją docelową powinna zostać ostatecznie potwierdzona przez porównanie wyników obu programów.

Projekt realizuje sprawdzone założenia Reverse Prompt Engineering i posiada udokumentowany proces testowania.