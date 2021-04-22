import unittest

from greetersTDD.greeters import Greeters


class GreetersTest(unittest.TestCase):
    # Given a name of the current user welcome them to the system via a message
    def test_pour_utilisateur_inconnu_acueillir_avec_bienvenue(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("", ""), "Bienvenue ")

    def test_pour_utilisateur_connu_acueillir_avec_bienvenue_plus_nom(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("Aziz", ""), "Bienvenue Aziz")

    def test_le_matin_acueillir_avec_bonjour_plus_nom(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("Aziz", "matin"), "Bonjour Aziz")

    def test_l_apres_midi_acueillir_avec_bonne_apres_midi_plus_nom(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("Aziz", "aprem"), "Bonne après midi Aziz")

    def test_le_soir_acueillir_avec_bonne_soiree_plus_nom(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("Aziz", "soir"), "Bonne soirée Aziz")

    def test_la_nuit_acueillir_avec_bonne_nuit_plus_nom(self):
        greeters = Greeters()
        self.assertEqual(greeters.welcome("Aziz", "nuit"), "Bonne nuit Aziz")


if __name__ == '__main__':
    unittest.main()
