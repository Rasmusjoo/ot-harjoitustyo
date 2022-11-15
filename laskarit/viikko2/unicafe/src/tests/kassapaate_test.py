import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodun_kassan_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassan_myytyjen_edullisten_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassan_myytyjen_maukkaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_rahamaara_kasvaa_ostettaessa_edullinen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+2*240)

    def test_rahamaara_kasvaa_ostettaessa_maukas_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+2*400)

    def test_rahamaara_ei_kasva_jos_ei_ole_varaa_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahamaara_ei_kasva_jos_ei_ole_varaa_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_kasvaa_ostettaessa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_maukkaat_kasvaa_ostettaessa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_edulliset_ei_kasva_jos_ei_ole_varaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_ei_kasva_jos_ei_ole_varaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_edulliset_kasvaa_ostettaessa_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_kasvaa_ostettaessa_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_lataus_kortille_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataus_kortille_pienentaa_kortin_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 11000)

    def test_negatiivinen_lataus_kortille_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahamaara_ei_muutu_jos_kortilla_ei_ole_varaa_edulliseen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahamaara_ei_muutu_jos_kortilla_ei_ole_varaa_maukkaaseen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)