#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
例子來自 https://en.wikipedia.org/wiki/Facade_pattern#Python


*這種模式是什麼？
Facade 模式是一種為更複雜的系統提供更簡單統一介面的方法。
它通過提供單一入口點提供了一種更簡單的方法來訪問底層系統的功能。
在許多現實生活中都可以看到這種抽象化。
例如，我們可以通過按下按鈕來打開電腦，但實際上在發生這種情況時會執行許多過程和操作
（例如，將程式從硬碟讀取到記憶體）。
在這種情況下，該按鈕用作打開電腦的所有基本程序的統一介面。

*該模式實際使用在哪裡？
當我們使用 isdir 函數時，可以在 Python 標準庫中看到此模式。
儘管用戶僅使用此函數來知道路徑是否指的是一個目錄，但系統進行一些操作並調用其他模組
（例如，os.stat）來給出結果。

*參考：
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade

*TL;DR80
為複雜系統提供更簡單統一的介面。
"""

from __future__ import print_function


# Complex computer parts
class CPU(object):
    """
    簡單的 CPU 表示。
    """
    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory(object):
    """
    簡單的記憶體表示。
    """
    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))


class SolidStateDrive(object):
    """
    簡單的固態硬碟表示。
    """
    def read(self, lba, size):
        return "Some data from sector {0} with size {1}".format(lba, size)


class ComputerFacade(object):
    """
    表示各種電腦部件的外觀。
    """
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
