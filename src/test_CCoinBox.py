import unittest
from io import StringIO

from CCoinBox import CCoinBox
from unittest.mock import patch

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def test_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_retourne_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        piece = coinBox.retourne_monnaie()
        self.assertEqual(coinBox.get_vente_permise(), False)
        self.assertEqual(piece, 1)

    def test_permet_une_double_vente(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertEqual(coinBox.get_vente_permise(), True)


    def test_pas_assez_monnaie_courrante_apres_vente(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertLess(coinBox.monnaie_courante, 2)
        self.assertFalse(coinBox.vente_permise)

    def test_vente_non_permise(self):
        coinBox = CCoinBox()
        with patch('sys.stdout', new = StringIO()) as fake_output:
            coinBox.vente()
            self.assertEqual(fake_output.getvalue(), "Pas assez de monnaie\n")

    def test_get_monnaie_totale(self):
        coinBox = CCoinBox()
        self.assertEqual(coinBox.get_monnaie_totale(), 0)

    def test_get_monnaie_courante(self):
        coinBox = CCoinBox()
        self.assertEqual(coinBox.get_monnaie_courante(), 0)