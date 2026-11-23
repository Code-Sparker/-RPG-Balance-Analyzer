# WERYFIKACJA PROJEKTU – RPG BALANCE ANALYZER

## 1. Cel weryfikacji

Celem weryfikacji było sprawdzenie, czy program RPG Balance Analyzer działa poprawnie i realizuje wymagania odtworzone na podstawie analizy wersji docelowej.

Sprawdzono poprawność obliczeń, normalizację statystyk, ranking postaci, przypisywanie ról, symulację pojedynków, walidację danych oraz eksport wyników do pliku CSV.

## 2. Zakres przeprowadzonych testów

| Wymaganie | Sposób sprawdzenia | Wynik |
|---|---|---|
| Wykorzystanie NumPy | Sprawdzenie struktury danych | Do sprawdzenia |
| Normalizacja min-max | Test wartości minimalnych i maksymalnych | Do sprawdzenia |
| Obsługa stałych kolumn | Test jednakowych wartości statystyki | Do sprawdzenia |
| Ważony wynik siły | Sprawdzenie obliczeń | Do sprawdzenia |
| Ranking postaci | Porównanie kolejności wyników | Do sprawdzenia |
| Przypisywanie ról | Sprawdzenie przypisanych ról | Do sprawdzenia |
| Walidacja danych | Test nieprawidłowych danych | Do sprawdzenia |
| Macierz pojedynków | Sprawdzenie wyników symulacji | Do sprawdzenia |
| Średnie szanse wygranej | Sprawdzenie obliczeń procentowych | Do sprawdzenia |
| Eksport CSV | Sprawdzenie wygenerowanego pliku | Do sprawdzenia |

## 3. Testy jednostkowe

Testy jednostkowe przygotowano w pliku `test_main.py`.

Ich zadaniem jest sprawdzenie poprawności poszczególnych funkcji programu, w szczególności:

- normalizacji statystyk,
- obliczania siły postaci,
- tworzenia rankingu,
- przypisywania ról,
- walidacji danych wejściowych,
- symulacji pojedynków,
- generowania macierzy pojedynków,
- eksportowania wyników do CSV.

Wynik testów należy uzupełnić po uruchomieniu polecenia:

`python -m unittest test_main -v`

**Wynik uruchomienia:** [WPISZ RZECZYWISTY WYNIK]

## 4. Korekty promptów – Reverse Prompt Engineering

### Korekta 1 – Obsługa stałych kolumn

**Problem:**

Podczas testowania należy sprawdzić przypadek, w którym wszystkie postacie mają identyczną wartość danej statystyki. Taka sytuacja może powodować dzielenie przez zero podczas normalizacji min-max.

**Zmiana promptu:**

Doprecyzowanie wymagania dotyczącego obsługi kolumn, w których wartość minimalna jest równa maksymalnej.

**Oczekiwany rezultat:**

Program powinien bezpiecznie obsługiwać takie kolumny, nie generując wartości NaN ani nieskończoności.

**Dowód weryfikacji:** [WPISZ WYNIK RZECZYWISTEGO TESTU]

### Korekta 2 – Walidacja danych wejściowych

**Problem:**

Należy sprawdzić zachowanie programu dla nieprawidłowych danych wejściowych, takich jak wartości ujemne, brakujące dane, NaN oraz nieskończoność.

**Zmiana promptu:**

Doprecyzowanie wymagań dotyczących walidacji danych przed rozpoczęciem obliczeń.

**Oczekiwany rezultat:**

Program powinien wykrywać nieprawidłowe dane i zgłaszać czytelny błąd zamiast wykonywać niepoprawne obliczenia.

**Dowód weryfikacji:** [WPISZ WYNIK RZECZYWISTEGO TESTU]

## 5. Weryfikacja eksportu CSV

Wyniki działania programu są eksportowane do pliku `ranking_postaci.csv`.

Podczas sprawdzania należy zweryfikować:

- obecność wszystkich analizowanych postaci,
- poprawność nagłówków kolumn,
- zgodność rankingu z wynikami programu,
- obecność informacji o rolach i sile postaci,
- poprawność średnich szans wygranej,
- możliwość otwarcia pliku i odczytania polskich znaków.

**Wynik:** [WPISZ RZECZYWISTY WYNIK]

## 6. Podsumowanie

Projekt RPG Balance Analyzer został przygotowany w ramach zadania Reverse Prompt Engineering.

Program jest rozwijany etapowo za pomocą serii promptów, których celem jest odtworzenie funkcjonalności programu docelowego bez przekazywania modelowi kodu wersji B.

Końcowa ocena zgodności powinna uwzględniać wyniki testów jednostkowych, testy przypadków brzegowych oraz porównanie zachowania programu z wymaganiami wersji docelowej.
