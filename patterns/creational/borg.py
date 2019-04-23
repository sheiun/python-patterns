#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
博格模式（Borg pattern）（也被稱為 Monostate pattern）是一種實現單例行為的方法，
但是不是只有一個類的實例，而是有多個實例共享相同的狀態。換句話說，
重點是共享狀態而不是共享實例標識。

*這個例子做了什麼？
要理解 Python 中此模式的實現，重要的是要知道，在 Python 中，
實例屬性存儲在名為 __dict__ 的屬性字典中。 通常，每個實例都有自己的字典，
但博格模式會修改它，以便所有實例都具有相同的字典。
在此範例中，__shared_state 屬性將是在所有實例之間共享的字典，
並且通過在初始化新實例時（即在 __init__ 方法中）
將 __shared_state 賦值給 __dict__ 變數來確保這一點。其他屬性通常會添加到實例的屬性字典中，
但是，由於屬性字典本身是共享的（即 __shared_state），因此所有其他屬性也將被共享。
因此，當使用實例 rm2 修改屬性 self.state 時，實例 rm1 中 self.state 的值也會更改。
如果使用 rm3 修改 self.state，則會發生同樣的情況，rm3 是子類別中的實例。
請注意，即使它們共享屬性，實例也不同，如其 ID 所示。

*該模式實際使用在哪裡？
共享狀態在管理資料庫連接等應用程式中很有用：
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

*參考：
https://fkromer.github.io/python-pattern-references/design/#singleton

*TL;DR80
在實例之間提供類似單一行為的行為共享狀態。
"""


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init
