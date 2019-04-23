python-patterns-chinese-traditional
===============

Python 中一系列的設計模式和慣用語。

關於此專案
----------------

此專案 Fork 自 [faif/python-patterns](https://github.com/faif/python-patterns) 。  
主要的目的是做*繁體中文*的翻譯，不接受任何程式碼的修改，僅接受英文敘述變更，若有任何關於程式碼的疑問，請移駕至來源專案。  
因貢獻方式不同，此專案的 README 將貢獻以下的欄位全數刪除，

目前模式
----------------

__創建型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [abstract_factory](patterns/creational/abstract_factory.py) | 使用特定工廠的通用函數 |
| [borg](patterns/creational/borg.py) | 實例中具有共享狀態的單例 |
| [builder](patterns/creational/builder.py) | 用建構器物件接收參數並返回建構的物件，代替使用多個建構子 |
| [factory](patterns/creational/factory.py) | 委託專門的函數／方法來創建實例 |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | Python 中延遲評估的屬性模式 |
| [pool](patterns/creational/pool.py) | 預先實例化並維護一組相同類型的實例 |
| [prototype](patterns/creational/prototype.py) | 使用工廠和原型的克隆用於新實例（如果實例化是昂貴的） |

__結構型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.py) | 資料<->商業邏輯<->演示分離（嚴格的關係）|
| [adapter](patterns/structural/adapter.py) | 使用白名單將一個介面調整到另一個介面 |
| [bridge](patterns/structural/bridge.py) | 客戶端提供商中間人，以軟化介面變更 |
| [composite](patterns/structural/composite.py) | 讓客戶均勻對待個別物件和組合 |
| [decorator](patterns/structural/decorator.py) | 使用其它功能包裝功能以影響輸出 |
| [facade](patterns/structural/facade.py) | 使用一個類別作為許多其他類的 API |
| [flyweight](patterns/structural/flyweight__py3.py) | 透明地重用具有相似／相同狀態物件的存在實例 |
| [front_controller](patterns/structural/front_controller.py) | 單一處理程式請求進入應用程式 |
| [mvc](patterns/structural/mvc.py) | 模型<->視圖<->控制器（非嚴格關係） |
| [proxy](patterns/structural/proxy.py) | 一個物件將操作導引到其它東西 |

__行為型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility__py3.py) | 應用一系列連續的處理程序來嘗試和處理數據 |
| [catalog](patterns/behavioral/catalog.py) | 一般方法會根據建構參數調用不同的專用方法 |
| [chaining_method](patterns/behavioral/chaining_method.py) | 繼續回調下一個物件方法 |
| [command](patterns/behavioral/command.py) | 捆綁命令和參數以便稍後調用 |
| [iterator](patterns/behavioral/iterator.py) | 遍歷容器並訪問容器的元素 |
| [mediator](patterns/behavioral/mediator.py) | 一個知道如何連接其他物件並充當代理的物件 |
| [memento](patterns/behavioral/memento.py) | 生成一個可用於返回先前狀態的不透明令牌 |
| [observer](patterns/behavioral/observer.py) | 提供回調給資料的事件／變更通知 |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | 一個來源將事件／資料聯合到註冊的監聽器 |
| [registry](patterns/behavioral/registry__py3.py) | 持續追蹤給定類別的所有子類別 |
| [specification](patterns/behavioral/specification.py) | 可以通過使用布林邏輯將商業規則鏈接在一起來重新組合商業規則 |
| [state](patterns/behavioral/state.py) | 邏輯被組織成離散數量的潛在狀態和可以轉換到的下一個狀態 |
| [strategy](patterns/behavioral/strategy.py) | 對同一資料的可選操作 |
| [template](patterns/behavioral/template.py) | 一個物件強加一個結構，但用可插入的組件 |
| [visitor](patterns/behavioral/visitor.py) | 為集合的所有物品調用回調 |

__可測試性設計模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [dependency_injection](patterns/dependency_injection.py) | 依賴注入的 3 種變體 |

__基本型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [delegation_pattern](patterns/fundamental/delegation_pattern.py) | 物件通過委託給第二個物件（代表）來處理請求 |

__其它__:

|   模式   |     描述    |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard__py3.py) | 建築模型，匯集不同子系統的知識，建構解決方案，AI 方法 - 非四人幫設計模式 |
| [graph_search](patterns/other/graph_search.py) | 圖形演算法 - 非四人幫設計模式 |
| [hsm](patterns/other/hsm/hsm.py) | 分層狀態機 - 非四人幫設計模式 |


影片
------
[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)


貢獻
------------
請參閱來源專案