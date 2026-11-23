# PROMPTY – RPG BALANCE ANALYZER

## Cel projektu

Celem projektu jest stopniowe przekształcenie początkowego programu analizującego postacie RPG w bardziej rozbudowany analizator balansu.

Przebudowa odbywa się etapami przy użyciu modelu AI. Model otrzymuje wyłącznie kod początkowy (wersja A), a następnie realizuje kolejne wymagania przekazywane za pomocą promptów.

Kod wersji docelowej B nie jest przekazywany modelowi.

---

## PROMPT 1 – Zmiana struktury danych na NumPy

**Opis zmiany:** Zastąpienie podstawowej struktury danych tablicami NumPy.

**Treść promptu:**

Przeanalizuj otrzymany kod programu RPG i zmodyfikuj sposób przechowywania danych postaci.

Wymagania:
1. Wykorzystaj bibliotekę NumPy.
2. Przechowuj nazwy postaci w osobnej tablicy.
3. Przechowuj wartości statystyk w dwuwymiarowej tablicy NumPy.
4. Zachowaj powiązanie nazw postaci z odpowiednimi statystykami.
5. Zadbaj o czytelność kodu i oddzielenie danych od obliczeń.

Nie usuwaj istniejących danych postaci. Przedstaw kompletny zmodyfikowany kod.

## PROMPT 2 – Normalizacja statystyk i ważony wynik siły

**Opis zmiany:** Wprowadzenie normalizacji min-max oraz obliczania łącznej siły postaci.

**Treść promptu:**

Rozbuduj program o normalizację statystyk postaci.

Wymagania:
1. Zastosuj normalizację min-max do każdej kolumny statystyk.
2. Wykorzystaj operacje wektorowe NumPy zamiast ręcznego przetwarzania każdej postaci.
3. Zabezpiecz normalizację przed dzieleniem przez zero, gdy wszystkie wartości w kolumnie są identyczne.
4. Oblicz ważony wynik siły postaci.
5. Zastosuj następujące wagi: HP – 0.20, atak – 0.40, obrona – 0.25, szybkość – 0.15.
6. Wynik siły powinien być liczbą z przedziału od 0 do 1.

Sprawdź, czy suma wag wynosi 1. Zachowaj poprawność wcześniejszego kodu.

## PROMPT 3 – Ranking i automatyczne przypisywanie ról

**Opis zmiany:** Dodanie rankingu postaci oraz automatycznego określania ich ról.

**Treść promptu:**

Dodaj do programu system rankingu postaci RPG.

Wymagania:
1. Posortuj postacie malejąco według obliczonego wyniku siły.
2. Wykorzystaj NumPy do sortowania.
3. Zachowaj powiązanie nazwy, statystyk i wyniku siły.
4. Zastosuj stabilne sortowanie, aby postacie z identycznym wynikiem zachowały pierwotną kolejność.
5. Dodaj automatyczne przypisywanie ról na podstawie dominujących statystyk postaci.
6. Wyświetl nazwę postaci, miejsce w rankingu, wynik siły i przypisaną rolę.

Nie przypisuj ról losowo. Reguły przypisywania powinny być jednoznaczne i powtarzalne.

## PROMPT 4 – Filtrowanie i statystyki zbiorcze

**Opis zmiany:** Rozbudowanie analizy o filtrowanie postaci i statystyki całej grupy.

**Treść promptu:**

Dodaj do programu funkcjonalność filtrowania i analizowania postaci RPG.

Wymagania:
1. Umożliw filtrowanie postaci na podstawie wartości ich statystyk.
2. Wykorzystaj maski logiczne NumPy.
3. Oblicz średnie wartości poszczególnych statystyk.
4. Oblicz minimalne i maksymalne wartości statystyk.
5. Wyświetl czytelne podsumowanie wyników.
6. Zadbaj o poprawną obsługę sytuacji, w której filtr nie zwraca żadnej postaci.

Nie zmieniaj wyników rankingu dla danych, które nie zostały przefiltrowane.

## PROMPT 5 – Walidacja danych wejściowych

**Opis zmiany:** Zabezpieczenie programu przed nieprawidłowymi danymi.

**Treść promptu:**

Dodaj dokładną walidację danych wejściowych programu RPG Balance Analyzer.

Wymagania:
1. Sprawdź, czy tablica statystyk ma prawidłowy wymiar.
2. Sprawdź, czy liczba nazw odpowiada liczbie zestawów statystyk.
3. Odrzuć nieprawidłowe wartości liczbowe.
4. Wykrywaj wartości NaN oraz nieskończoność.
5. Odrzuć ujemne wartości statystyk.
6. Sprawdź, czy nazwy postaci są prawidłowe.
7. Zwracaj czytelne komunikaty błędów.

Walidacja powinna odbywać się przed wykonywaniem obliczeń. Nie pozwól, aby błędne dane powodowały nieprawidłowe wyniki programu.

## PROMPT 6 – Symulacja pojedynków i macierz wyników

**Opis zmiany:** Dodanie mechanizmu porównywania postaci w pojedynkach.

**Treść promptu:**

Rozbuduj program o symulację pojedynków pomiędzy wszystkimi postaciami.

Wymagania:
1. Wykorzystaj obliczone wyniki siły postaci.
2. Zastosuj matematyczny model logistyczny do wyznaczania szans zwycięstwa.
3. Wygeneruj dwuwymiarową macierz pojedynków.
4. Każda komórka macierzy powinna przedstawiać szansę zwycięstwa postaci z wiersza nad postacią z kolumny.
5. Szanse powinny być przedstawione jako wartości procentowe.
6. Szansa pojedynku postaci z samą sobą powinna wynosić 50%.
7. Wyniki pojedynków dwóch różnych postaci powinny być wzajemnie uzupełniające się do 100%.

Zastosuj operacje NumPy i unikaj niepotrzebnych pętli.

## PROMPT 7 – Średnie szanse wygranej i eksport CSV

**Opis zmiany:** Dodanie podsumowania pojedynków i zapisywania wyników do pliku.

**Treść promptu:**

Dodaj do programu obliczanie średnich szans wygranej każdej postaci oraz eksport wyników.

Wymagania:
1. Oblicz średnią szansę zwycięstwa każdej postaci przeciwko pozostałym postaciom.
2. Pomijaj pojedynki postaci z samą sobą podczas obliczania średniej.
3. Dodaj średnią szansę wygranej do informacji o postaci.
4. Eksportuj wyniki do pliku `ranking_postaci.csv`.
5. Zapisz ranking, nazwę postaci, wynik siły, przypisaną rolę oraz średnią szansę wygranej.
6. Zastosuj bibliotekę csv.
7. Zadbaj o poprawne kodowanie polskich znaków.
8. Zastosuj czytelne nagłówki kolumn.

Po zakończeniu działania programu plik CSV powinien być automatycznie generowany lub aktualizowany.

## PROMPT 8 – Testy jednostkowe i integracja

**Opis zmiany:** Sprawdzenie poprawności całego programu i przygotowanie końcowej wersji.

**Treść promptu:**

Przeanalizuj cały program RPG Balance Analyzer i przygotuj testy jednostkowe sprawdzające jego działanie.

Wymagania:
1. Wykorzystaj bibliotekę unittest.
2. Przetestuj normalizację statystyk.
3. Przetestuj obsługę stałych kolumn.
4. Przetestuj obliczanie ważonej siły.
5. Przetestuj ranking i remisy.
6. Przetestuj przypisywanie ról.
7. Przetestuj walidację nieprawidłowych danych.
8. Przetestuj macierz pojedynków.
9. Przetestuj średnie szanse wygranej.
10. Przetestuj eksport CSV.
11. Sprawdź przypadki brzegowe.
12. Usuń błędy i zachowaj wszystkie wcześniejsze funkcjonalności.

Przygotuj kompletny kod programu oraz osobny plik `test_main.py`. Podaj instrukcję uruchamiania programu i testów.

---

## 9. Dokumentowanie korekt promptów

Korekty należy wprowadzać po rzeczywistym wykryciu nieprawidłowości lub niepełnego wyniku.

### Korekta 1 – Normalizacja stałych kolumn

**Prompt pierwotny:** PROMPT 2.

**Sytuacja do przetestowania:** Wszystkie postacie posiadają identyczną wartość jednej statystyki.

**Dodatkowe polecenie:**

Sprawdź działanie normalizacji min-max dla kolumny, w której minimum jest równe maksimum. Zabezpiecz obliczenia przed dzieleniem przez zero. Wynik normalizacji takiej kolumny powinien być określony i nie może zawierać NaN ani nieskończoności.

**Rzeczywisty wynik próby:** [UZUPEŁNIJ PO TESTACH]

### Korekta 2 – Walidacja danych

**Prompt pierwotny:** PROMPT 5.

**Sytuacja do przetestowania:** Przekazanie do programu nieprawidłowych danych.

**Dodatkowe polecenie:**

Rozszerz testy walidacji o wartości NaN, nieskończoność, wartości ujemne oraz nieprawidłowe wymiary tablic. Każdy nieprawidłowy przypadek powinien zostać wykryty przed rozpoczęciem obliczeń i zakończyć się czytelnym komunikatem błędu.

**Rzeczywisty wynik próby:** [UZUPEŁNIJ PO TESTACH]

---

## 10. Podsumowanie

Projekt został podzielony na osiem głównych etapów przebudowy.

Każdy prompt wprowadza nowe funkcjonalności i rozwija wcześniejszą wersję programu. Kolejność zmian pozwala stopniowo przejść od podstawowego analizatora postaci do rozbudowanego systemu wykorzystującego NumPy.

Ważnym elementem procesu jest testowanie kolejnych etapów, wykrywanie przypadków brzegowych i poprawianie promptów na podstawie rzeczywistych wyników działania modelu AI.
