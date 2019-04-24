#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
*這種模式是什麼？
它解耦了複雜物件及其表示的創建，因此可以重用相同的進程來建構來自同一系列的物件。
當您必須將物件的規範與其實際表示（通常用於抽象）分開時，這非常有用。

*這個例子做了什麼？
第一個範例通過使用抽象的基本類別來實現此目的，
其中初始化程式（__init__ 方法）指定所需的步驟
具體子類別實現這些步驟。

在其它程式語言中，有時需要更複雜的安排。特別是，你不能在 C++ 的建構子中有多型行為 - 請參閱
https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
 - 這意味著這種 Python 技術不管用。 所需的多型必須由外部的，已經建構的不同類別的實例提供。

一般來說，在 Python 中這不是必需的，但也包括顯示這種安排的第二個例子。

*該模式實際使用在哪裡？

*參考：
https://sourcemaking.com/design_patterns/builder

*TL;DR80
解耦複雜物件的建構及其表示方式。
"""


# 抽象 Building
class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# 實體 Buildings
class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'


# 在一些非常複雜的情況下，可能需要將建構邏輯拉出到另一個函數中（或方法或其他類別），
# 而不是在基本類別 '__init__'。 (這使您處於一個奇怪的情況，即具體類別沒有有用的建構子)


class ComplexBuilding(object):
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big and fancy'


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


# 客戶端
if __name__ == "__main__":
    house = House()
    print(house)
    flat = Flat()
    print(flat)

    # 使用外部建構函數：
    complex_house = construct_building(ComplexHouse)
    print(complex_house)

### OUTPUT ###
# Floor: One | Size: Big
# Floor: More than One | Size: Small
# Floor: One | Size: Big and fancy
