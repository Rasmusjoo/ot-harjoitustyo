import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_otto_toimii(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_ei_muutu_jos_ei_ole_varaa(self):
        maksukortti = Maksukortti(500)
        maksukortti.ota_rahaa(600)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 5.00 euroa")