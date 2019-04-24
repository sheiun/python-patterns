#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*這種模式是什麼？
在創建物件成本高昂（並且經常創建）時使用此模式，但一次只使用少量物件。
使用 Pool，我們可以通過暫存它們來管理我們現在擁有的那些實例。
現在，如果池中有可用物件，則可以跳過昂貴的物件創建。
池允許 'check out' 非活動物件，然後回傳它。如果沒有可用，
則池創建一個無需等待即可提供。

*這個例子做了什麼？
在此範例中，queue.Queue 用於創建池
（包裝在 with 語句一起使用的自定義 ObjectPool 物件中），並使用字符串填充。
正如我們所看到的，放入 "yam" 的第一個字符串物件由 with 語句使用。
但是因為它之後被釋放回池中，所以通過顯式調用 sample_queue.get() 來重用它。
同樣的事情發生在 "sam" 中，當 ObjectPool 創建時，該函數被刪除（由 GC）並回傳該物件。

*該模式實際使用在哪裡？

*參考：
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

*TL;DR80
存儲一組準備好使用的初始化物件。
"""


class ObjectPool(object):
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x compatibility
        import Queue as queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print('Inside func: {}'.format(pool.item))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam
