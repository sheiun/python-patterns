#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
此模式旨在最小化程式在運行時所需的物件數。
Flyweight 是由多個上下文共享的物件，與未共享的物件無法區分。

Flyweight 的狀態不應受其上下文的影響，這被稱為其內在狀態。
將物件狀態與物件的上下文分離，允許共享 Flyweight。

*這個例子做了什麼？
下面的範例設置一個存儲初始化的 'Card Pool' 物件。 當創建 'Card' 時，
它首先檢查它是否已經存在而不是創建一個新的 Card。 這旨在減少程式初始化的物件數量。

*參考：
http://codesnipers.com/?q=python-flyweights
https://python-patterns.guide/gang-of-four/flyweight/

*Python 生態系統中的範例:
https://docs.python.org/3/library/sys.html#sys.intern

*TL;DR80
通過與其他類似物件共享資料來最大限度地減少記憶體使用。
"""

import weakref


class Card(object):
    """The Flyweight"""

    # 可能是一個簡單的字典。
    # 使用 WeakValueDictionary 垃圾蒐集可以回收對象
    # 當沒有其他參考時。
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        # 如果物件存在於池中 - 只需返回它
        obj = cls._pool.get(value + suit)
        # 否則 - 創建一個（並將其添加到池中）
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            # 這行是我們通常在 `__init__` 中看到的部分
            obj.value, obj.suit = value, suit
        return obj

    # 如果取消註解 `__init__` 並註解掉 `__new__` -
    #   Card 變得正常 (non-flyweight).
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def main():
    """
    >>> c1 = Card('9', 'h')
    >>> c2 = Card('9', 'h')
    >>> c1, c2
    (<Card: 9h>, <Card: 9h>)
    >>> c1 == c2
    True
    >>> c1 is c2
    True

    >>> c1.new_attr = 'temp'
    >>> c3 = Card('9', 'h')
    >>> hasattr(c3, 'new_attr')
    True

    >>> Card._pool.clear()
    >>> c4 = Card('9', 'h')
    >>> hasattr(c4, 'new_attr')
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
