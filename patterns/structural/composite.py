#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
組合模式（Composite Pattern）描述了一組物件其處理方式與相同類型物件的單一實例相同。
複合的意圖是將物件 “組合” 成樹狀結構以表示部分整體層次結構。
通過實現組合模式，客戶可以統一處理個別物件和組合。

*這個例子做了什麼？
該範例實現了一個圖形類別，可以是橢圓形或多個圖形的組合。
每個圖形都可以被印出。

*該模式實際使用在哪裡？
在圖形編輯器中，形狀是可以基本的或複雜的。簡單形狀的範例是線，
而複雜形狀是一個由四個線物件組成的矩形。由於形狀具有許多共同的操作，
例如將形狀渲染到螢幕，且由於形狀遵循部分整體層次結構，
因此可以使用組合模式使程式能夠統一處理所有形狀。

*參考：
https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

*TL;DR80
描述一組被視為單一實例的物件。
"""


class Graphic:
    def render(self):
        raise NotImplementedError("You should implement this.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()

### OUTPUT ###
# Ellipse: 1
# Ellipse: 2
# Ellipse: 3
# Ellipse: 4
