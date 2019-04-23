#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
在 Java 和其他語言中，抽象工廠模式（Abstract Factory Pattern）
用於提供用於創建相關／從屬物件的介面，而無需指定其實際類別。

我們的想法是根據商業邏輯，平台選擇等抽象物件的創建。

在 Python 中，我們使用的介面只是一個請求即付的，它是 Python 中的 'built in' 介面，
在正常情況下我們可以簡單地將類別本身用作請求即付的，因為類別是 Python 中的第一類別物件。

*這個例子做了什麼？
這個特定的實現抽象了寵物的創建，並取決於我們選擇的工廠（Dog 或 Cat 或 random_animal）
這樣做是有效的，因為 Dog/Cat 和 random_animal 都遵循一個共同的介面（可調用的創建和 .speak()）。
現在我的應用程式可以抽像地創建寵物，並根據我自己的標準稍後決定，狗對貓。

*該模式實際使用在哪裡？

*參考：
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR80
提供一個封裝一組個別工廠的方法。
"""

import random


class PetShop(object):

    """ 一家寵物店 """

    def __init__(self, animal_factory=None):
        """ pet_factory 是我們的抽象工廠。 我們可以隨意設置它。 """

        self.pet_factory = animal_factory

    def show_pet(self):
        """ 使用抽象工廠創建並展示寵物 """

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# 其它工廠：

# 隨機創建一個動物
def random_animal():
    """ 讓我們變成動態的！ """
    return random.choice([Dog, Cat])()


# 與各種工廠展示寵物
if __name__ == "__main__":

    # 一家只賣貓的商店
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # 一家隨機出售動物的商店
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

### OUTPUT ###
# We have a lovely Cat
# It says meow
#
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================
