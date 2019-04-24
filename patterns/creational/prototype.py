#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
此模式旨在減少應用程式所需的類別數。 它不是依賴於子類別，
而是通過在運行時複製原型實例來創建物件。

這很有用，因為當類別的實例只有幾個不同的狀態組合，並且實例化很昂貴時，
它可以更容易地產生新類型的物件。

*這個例子做了什麼？
當應用程式中的原型數量可能不同時，保留 Dispatcher（aka，Registry 或 Manager）會很有用。
這允許客戶端在克隆新實例之前向 Dispatcher 查詢原型。

下面提供了一個 Dispatcher 的範例，其中包含三個原型副本：'default'，'objecta' 和 'objectb'。

*TL;DR80
通過克隆原型來創建新的物件實例。
"""


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """ 克隆原型並更新內部屬性字典 """
        # Python 實踐, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """ 獲取所有物件 """
        return self._objects

    def register_object(self, name, obj):
        """ 註冊一個物件 """
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

### OUTPUT ###
# [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
