
import unittest
import tempfile
import os
import csv
import numpy as np

from main import (
    waliduj,
    normalizuj,
    oblicz_sile,
    okresl_role,
    macierz_pojedynkow,
    oblicz_srednie_szanse,
    zapisz_csv,
)


class TestAnalizatorRPG(unittest.TestCase):

    def test_normalizacja(self):
        dane = np.array([
            [10, 20, 30, 40],
            [20, 40, 50, 60]
        ], dtype=float)

        wynik = normalizuj(dane)

        np.testing.assert_allclose(
            wynik,
            [[0, 0, 0, 0], [1, 1, 1, 1]]
        )

    def test_stala_kolumna(self):
        dane = np.array([
            [10, 20, 30, 40],
            [10, 30, 30, 60]
        ], dtype=float)

        wynik = normalizuj(dane)

        np.testing.assert_allclose(wynik[:, 0], [0, 0])
        np.testing.assert_allclose(wynik[:, 2], [0, 0])

    def test_walidacja_poprawnych_danych(self):
        waliduj(
            np.array(["A", "B"]),
            np.array([
                [10, 20, 30, 40],
                [20, 30, 40, 50]
            ])
        )

    def test_duplikaty(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A", "A"]),
                np.ones((2, 4))
            )

    def test_ujemne_dane(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A", "B"]),
                np.array([
                    [10, 20, 30, 40],
                    [20, -1, 40, 50]
                ])
            )

    def test_nan(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A", "B"]),
                np.array([
                    [10, 20, 30, 40],
                    [20, 30, np.nan, 50]
                ])
            )

    def test_nieskonczonosc(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A", "B"]),
                np.array([
                    [10, 20, 30, 40],
                    [20, 30, np.inf, 50]
                ])
            )

    def test_zly_wymiar(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A", "B"]),
                np.ones((2, 3))
            )

    def test_jedna_postac(self):
        with self.assertRaises(ValueError):
            waliduj(
                np.array(["A"]),
                np.ones((1, 4))
            )

    def test_role(self):
        dane = np.array([
            [100, 40, 10, 15],
            [130, 20, 20, 8],
            [80, 20, 10, 10]
        ], dtype=float)

        role = okresl_role(dane)

        np.testing.assert_array_equal(
            role,
            ["Szturmowiec", "Obrońca", "Wszechstronny"]
        )

    def test_macierz_pojedynkow(self):
        sila = np.array([0.1, 0.5, 0.9])
        wynik = macierz_pojedynkow(sila)

        self.assertEqual(wynik.shape, (3, 3))
        np.testing.assert_allclose(np.diag(wynik), 0.5)
        np.testing.assert_allclose(wynik + wynik.T, 1.0)

    def test_remis(self):
        wynik = macierz_pojedynkow(np.array([0.5, 0.5]))

        np.testing.assert_allclose(
            wynik,
            [[0.5, 0.5], [0.5, 0.5]]
        )

    def test_srednie_szanse(self):
        pojedynki = np.array([
            [0.5, 0.8, 0.6],
            [0.2, 0.5, 0.7],
            [0.4, 0.3, 0.5]
        ])

        wynik = oblicz_srednie_szanse(pojedynki)

        np.testing.assert_allclose(
            wynik,
            [0.7, 0.45, 0.35]
        )

    def test_ranking(self):
        dane = np.array([
            [10, 10, 10, 10],
            [20, 20, 20, 20],
            [30, 30, 30, 30]
        ], dtype=float)

        sila = oblicz_sile(dane)
        ranking = np.argsort(-sila, kind="stable")

        np.testing.assert_array_equal(ranking, [2, 1, 0])

    def test_csv(self):
        nazwy = np.array(["A", "B"])
        role = np.array(["Obrońca", "Szturmowiec"])
        sila = np.array([0.4, 0.8])
        szanse = np.array([0.3, 0.7])
        ranking = np.array([1, 0])

        with tempfile.TemporaryDirectory() as folder:
            sciezka = os.path.join(folder, "test.csv")

            zapisz_csv(
                sciezka,
                nazwy,
                role,
                sila,
                szanse,
                ranking
            )

            with open(
                sciezka,
                encoding="utf-8-sig",
                newline=""
            ) as plik:
                dane = list(csv.reader(plik, delimiter=";"))

            self.assertEqual(len(dane), 3)
            self.assertEqual(dane[1][1], "B")
            self.assertEqual(dane[2][1], "A")

    def test_stabilny_ranking_przy_remisie(self):
        dane = np.array([
            [10, 20, 30, 40],
            [10, 20, 30, 40],
            [20, 30, 40, 50]
        ], dtype=float)

        sila = oblicz_sile(dane)
        ranking = np.argsort(-sila, kind="stable")

        np.testing.assert_array_equal(ranking, [2, 0, 1])


if __name__ == "__main__":
    unittest.main()
