# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Aged_Brie(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(2, items[0].quality)
    
    def test_Sulfuras(self):
        items = [Item("Sulfuras", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras", items[0].name)

    def test_Backstage_Passes(self):
        items = [Item("Backstage passes", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
