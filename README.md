RPG Balance Analyzer
Opis projektu

RPG Balance Analyzer to program napisany w języku Python, który analizuje balans postaci RPG. Wykorzystuje bibliotekę NumPy do wykonywania obliczeń matematycznych i operacji na tablicach.

Projekt powstał w ramach zadania Reverse Prompt Engineering. Początkowy program został stopniowo rozbudowany za pomocą promptów przekazywanych modelowi AI.

Funkcjonalności
Przechowywanie statystyk postaci w tablicach NumPy.
Normalizacja statystyk metodą min-max.
Obliczanie ważonej siły postaci.
Automatyczne przypisywanie ról.
Tworzenie rankingu postaci.
Walidacja danych wejściowych.
Symulacja pojedynków.
Obliczanie średnich szans wygranej.
Wyświetlanie macierzy pojedynków.
Eksport wyników do pliku CSV.
Automatyczne testy jednostkowe.
Wykorzystane technologie
Python 3
NumPy
CSV
unittest
Instalacja

Zainstaluj wymagane biblioteki:

bash
pip install -r requirements.txt

Uruchomienie programu

W terminalu wpisz:

bash
python main.py


Program wyświetli ranking postaci, statystyki oraz macierz pojedynków.

Dodatkowo wygeneruje plik:

ranking_postaci.csv

Uruchomienie testów

Aby uruchomić testy automatyczne, wpisz:

bash
python -m unittest test_main -v


Testy sprawdzają między innymi normalizację, walidację, ranking, role, pojedynki i eksport CSV.

Struktura projektu
main.py – główny program analizujący postacie.
test_main.py – testy automatyczne.
prompty.md – dokumentacja promptów wykorzystanych w przebudowie.
requirements.txt – wymagane biblioteki.
WERYFIKACJA.md – dokumentacja sprawdzania poprawności.
ranking_postaci.csv – raport wygenerowany przez program.
Wyniki

Program analizuje osiem postaci RPG.

Najsilniejszą postacią w aktualnym zestawie danych jest Berserker.

Średnia siła wszystkich postaci wynosi około 0.4709.

Autor

[Wpisz swoje imię i nazwisko]