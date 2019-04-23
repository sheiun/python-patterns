#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
轉接器模式（Adapter Pattern）為類別提供不同的介面。 我們可以將其視為一種電纜轉接器，
允許您在具有不同形狀插座的地方為手機充電。 遵循這個想法，
轉接器模式對於整和由於其不兼容的介面而無法整合的類別非常有用。

*這個例子做了什麼？

該範例具有表示發出不同叫聲的實體 (Dog, Cat, Human, Car) 的類別。
Adapter 類別為產生此類叫聲的原始方法提供了不同的介面。 因此，
原始接口（例如，bark 和 meow）可以使用不同的名稱：make_noise。

*該模式實際使用在哪裡？
Grok 框架使用轉接器使物件與特定 API，而無需修改物件本身：
http://grok.zope.org/doc/current/grok_overview.html#adapters

*參考：
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*TL;DR80
允許將現有類別的介面用作另一個介面。
"""


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    """
    通過替換方法來調整物件。
    用法：
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adapted_methods):
        """我們在物件的字典中設置了轉接方法"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """所有 未 轉接的調用都將傳遞給物件"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """印出原始物件的字典"""
        return self.obj.__dict__


def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}

    >>> objects.append(Adapter(dog, make_noise=dog.bark))

    >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)

    >>> print(objects[0].original_dict())
    {'name': 'Dog'}

    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    >>> for obj in objects:
    ...    print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
