# RPG Balance Analyzer

## Opis projektu

RPG Balance Analyzer to program służący do analizowania i porównywania balansu postaci w grach RPG.

Projekt został wykonany w ramach zadania Reverse Prompt Engineering. Celem było odtworzenie funkcjonalności programu docelowego na podstawie analizy kodu początkowego i przygotowanie serii promptów prowadzących model AI przez kolejne etapy przebudowy.

Model AI otrzymał wyłącznie kod początkowy. Kod wersji docelowej nie był przekazywany modelowi jako gotowe rozwiązanie.

## Funkcjonalności

Program oferuje:

- przechowywanie statystyk postaci w tablicach NumPy,
- normalizację statystyk metodą min-max,
- obliczanie ważonego wyniku siły postaci,
- tworzenie rankingu postaci,
- automatyczne przypisywanie ról,
- filtrowanie postaci,
- obliczanie statystyk zbiorczych,
- walidację danych wejściowych,
- symulację pojedynków,
- generowanie macierzy szans zwycięstwa,
- obliczanie średnich szans wygranej,
- eksport wyników do pliku CSV.

## Wykorzystane technologie

- Python 3
- NumPy
- csv
- unittest

## Struktura projektu

| Plik | Opis |
|---|---|
| `main.py` | Główny program analizatora |
| `test_main.py` | Testy jednostkowe |
| `prompty.md` | Dokumentacja promptów wykorzystanych w procesie |
| `WERYFIKACJA.md` | Dokumentacja testów i weryfikacji |
| `ranking_postaci.csv` | Wyniki analizy postaci |
| `requirements.txt` | Lista wymaganych bibliotek |

## Instalacja

Wymagany jest Python 3.

Zainstaluj wymagane biblioteki poleceniem:

```bash
pip install -r requirements.txt
```

## Uruchamianie programu

Uruchom terminal w folderze projektu i wpisz:

```bash
python main.py
```

Program przeprowadzi analizę postaci i wygeneruje wyniki, w tym plik CSV.

## Uruchamianie testów

Aby uruchomić testy jednostkowe, wpisz:

```bash
python -m unittest test_main -v
```

## Wyniki

Program generuje plik:

`ranking_postaci.csv`

Zawiera on wyniki analizy, ranking postaci, ich role, wartości siły oraz średnie szanse zwycięstwa.

## Reverse Prompt Engineering

Proces przebudowy został podzielony na osiem etapów opisanych w pliku `prompty.md`.

Każdy etap wprowadza kolejne wymagania techniczne, począwszy od wykorzystania NumPy, poprzez normalizację, ranking i symulację pojedynków, aż do walidacji i testowania.

## Weryfikacja

Szczegółowe informacje o testach i sprawdzaniu poprawności programu znajdują się w pliku `WERYFIKACJA.md`.

## Autor

Imię i nazwisko: [viktoriisa yasiukevych]
