#!/usr/bin/python

class item:
    name= ""
    sell_in= ""
    quality=""

    def __init__(self, name, sell_in, quality):
        self.set_name(name)
        self.set_sell_in(sell_in)
        self.set_quality(quality)

    # Generated getter and setter code
    def get_name():
        return self.name;

    def set_name(self, name):
        self.name = name

    def get_sell_in():
        return self.sell_in;

    def set_sell_in(self, sell_in):
        self.sell_in = sell_in

    def get_quality():
        return self.quality;

    def set_quality(self, quality):
        self.quality = quality
