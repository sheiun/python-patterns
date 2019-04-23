python-patterns
===============

Python 中一系列的設計模式和慣用語。

關於此項目
----------------

此項目 Fork 自 [faif/python-patterns](https://github.com/faif/python-patterns) 。  
主要的目的是做*繁體中文*的翻譯，不接受任何程式碼的修改，僅接受英文敘述變更，若有任何關於程式碼的疑問，請移駕至來源專案。  
因貢獻方式不同，此項目的 README 將貢獻以下的欄位全數刪除，

目前模式
----------------

__創建型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [abstract_factory](patterns/creational/abstract_factory.py) | 使用特定工廠的通用函數 |
| [borg](patterns/creational/borg.py) | 實例中具有共享狀態的單例 |
| [builder](patterns/creational/builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory](patterns/creational/factory.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [pool](patterns/creational/pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](patterns/creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__結構型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](patterns/structural/adapter.py) | adapt one interface to another using a white-list |
| [bridge](patterns/structural/bridge.py) | a client-provider middleman to soften interface changes |
| [composite](patterns/structural/composite.py) | lets clients treat individual objects and compositions uniformly |
| [decorator](patterns/structural/decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](patterns/structural/facade.py) | use one class as an API to a number of others |
| [flyweight](patterns/structural/flyweight__py3.py) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](patterns/structural/front_controller.py) | single handler requests coming to the application |
| [mvc](patterns/structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](patterns/structural/proxy.py) | an object funnels operations to something else |

__行為型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility__py3.py) | apply a chain of successive handlers to try and process the data |
| [catalog](patterns/behavioral/catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](patterns/behavioral/chaining_method.py) | continue callback next object method |
| [command](patterns/behavioral/command.py) | bundle a command and arguments to call later |
| [iterator](patterns/behavioral/iterator.py) | traverse a container and access the container's elements |
| [mediator](patterns/behavioral/mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](patterns/behavioral/memento.py) | generate an opaque token that can be used to go back to a previous state |
| [observer](patterns/behavioral/observer.py) | provide a callback for notification of events/changes to data |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](patterns/behavioral/registry__py3.py) | keep track of all subclasses of a given class |
| [specification](patterns/behavioral/specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](patterns/behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](patterns/behavioral/strategy.py) | selectable operations over the same data |
| [template](patterns/behavioral/template.py) | an object imposes a structure but takes pluggable components |
| [visitor](patterns/behavioral/visitor.py) | invoke a callback for all items of a collection |

__可測試性設計模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [dependency_injection](patterns/dependency_injection.py) | 依賴注入的 3 種變體 |

__基本型模式__:

|   模式   |     描述    |
|:-------:| ----------- |
| [delegation_pattern](patterns/fundamental/delegation_pattern.py) | an object handles a request by delegating to a second object (the delegate) |

__其它__:

|   模式   |     描述    |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard__py3.py) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](patterns/other/graph_search.py) | graphing algorithms - non gang of four pattern |
| [hsm](patterns/other/hsm/hsm.py) | hierarchical state machine - non gang of four pattern |


影片
------
[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)


貢獻
------------
請參閱來源項目