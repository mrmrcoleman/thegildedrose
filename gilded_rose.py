#!/usr/bin/python

import item

class gilded_rose:
    items = []

    def main(self):
        print "OMGHAI!"
        self.items.append(item.item("+5 Dexterity Vest", 10, 20))
        self.items.append(item.item("Aged Brie", 2, 0));
        self.items.append(item.item("Elixir of the Mongoose", 5, 7));
        self.items.append(item.item("Sulfuras, Hand of Ragnaros", 0, 80));
        self.items.append(item.item("Backstage passes to a TAFKAL80ETC concert", 15, 20));
        self.items.append(item.item("Conjured Mana Cake", 3, 6));
        self.update_quality()

    def update_quality(self):
        for i in range(0, self.items.size()):
            if ((not("Aged Brie" == self.items.get(i).getName())) and (not("Backstage passes to a TAFKAL80ETC concert" == self.items.get(i).getName()))):
                if (self.items.get(i).getQuality() > 0):
                    if (not("Sulfuras, Hand of Ragnaros" == self.items.get(i).getName())):
                        self.items.get(i).setQuality(self.items.get(i).getQuality() - 1)
            else:
                if (self.items.get(i).get_quality() < 50):
                    self.items.get(i).set_quality(self.items.get(i).get_quality() + 1)
                    if ("Backstage passes to a TAFKAL80ETC concert" == self.items.get(i).getName()):
                        if (self.items.get(i).get_sell_in() < 11):
                            if (self.items.get(i).get_quality() < 50):
                                self.items.get(i).set_quality(self.items.get(i).get_quality() + 1)

                        if (self.items.get(i).get_sell_in() < 6):
                            if (self.items.get(i).get_quality() < 50):
                                self.items.get(i).set_quality(self.items.get(i).get_quality() + 1)

            if (not("Sulfuras, Hand of Ragnaros" == self.items.get(i).get_name())):
                self.items.get(i).set_sell_in(self.items.get(i).get_sell_in() - 1)

            if (self.items.get(i).get_sell_in() < 0):
                if (not("Aged Brie" == self.items.get(i).get_name())):
                    if (not("Backstage passes to a TAFKAL80ETC concert" == self.items.get(i).get_name())):
                        if (self.items.get(i).get_quality() > 0):
                            if (not("Sulfuras, Hand of Ragnaros" == self.items.get(i).getName())):
                                self.items.get(i).set_quality(self.items.get(i).get_quality() - 1)
                    else:
                        self.items.get(i).set_quality(self.items.get(i).get_quality() - self.items.get(i).get_quality())
                else:
                    if (self.items.get(i).get_quality() < 50):
                        self.items.get(i).set_quality(self.items.get(i).get_quality() + 1)

if __name__ == "__main__": gilded_rose().main()
