#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
Decorator 模式用於動態地向物件添加新功能而不變更其實現。
它與繼承不同，因為新功能僅添加到該特定物件，而不是整個子類別。

*這個例子做了什麼？
此範例展示了通過附加相應的標記（<b> 和 <i>）向文字添加格式選項（粗體和斜體）的方法。
此外，我們可以看到裝飾器可以一個接一個地應用，因為原始文字被傳遞給粗體包裝器，
而粗體包裝器又傳遞給斜體包裝器。

*該模式實際使用在哪裡？
Grok 框架使用裝飾器為方法添加功能，例如權限或訂閱事件：
http://grok.zope.org/doc/current/reference/decorators.html

*參考：
https://sourcemaking.com/design_patterns/decorator

*TL;DR80
向物件添加行為而不影響其類別。
"""

from __future__ import print_function


class TextTag(object):
    """ 表示基本文字標記 """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """ 包裝一個標記在 <b> 內 """

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """ 包中一個標記在 <i> 內 """

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())

### OUTPUT ###
# before: hello, world!
# after: <i><b>hello, world!</b></i>
