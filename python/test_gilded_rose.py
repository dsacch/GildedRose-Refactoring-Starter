# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Aged_Brie(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_Backstage_Passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()

