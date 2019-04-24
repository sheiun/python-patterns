#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*這種模式是什麼？
Factory 是用於創建其他物件的物件。

*這個例子做了什麼？
該程式顯示了一種用兩種語言本地化單字的方法：英語和希臘語。
"get_localizer" 是根據所選語言建構本地化的工廠函數。
根據本地化的語言，localizer 物件將是來自不同類別的實例。
但是，主程式不必擔心將實例化哪個本地化程式，
因為 "localize" 方法將以獨立於語言的相同方式調用。

*實際上可以在哪裡使用這種模式？
工廠方法可以在流行的 Web 框架 Django 中看到：
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns 
例如，在網頁的聯繫表單中，主題和訊息字段是使用相同的表單工廠（CharField()）創建的，
即使它們根據其用途具有不同的實現。

*參考：
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR80
無需指定確切的類別即可創建物件。
"""

from __future__ import unicode_literals
from __future__ import print_function


class GreekLocalizer(object):
    """ 一個簡單的本地化和一個 gettext"""

    def __init__(self):
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg):
        """ 如果我們沒有翻譯，我們會發揮作用 """
        return self.translations.get(msg, msg)


class EnglishLocalizer(object):
    """ 簡單地回應訊息 """

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    """ 工廠 """
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
