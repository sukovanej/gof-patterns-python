# GOF

# Creational patterns

 - they abstract the instantiation proccess
 - they make the system independent of how its objects are created, composed and represented
 - **object creational patterns** use inheritance , **class creational patterns** delete to other objects
 - example system - a *maze*
    - *maze* is a set or *room*s
    - a *room* knows it neighbors, a neighbor is a *door* to another *room*, a *wall* or a *room*
    - each *room* has four sides

## Abstract factory

 - provides an interface for creating families of related or dependent objects without specifying 
 their concrete classes

 - sometimes called *kit*

 - *abstract factory* declares an interface for operations that create abstract product objects
 - *concrete factory* implements operations to create concrete product objects
 - *abstract product* declares an interface for a type of product object
 - *concrete product* defines a product object to be created by a corresponding concrete factory
 - *clients* uses only interfaces declares by *abstract facotry* and *abstract product* classes


```python
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def make_product_1(self) -> AbstractProduct1:
        ...

    @abstractmethod
    def make_product_2(self) -> AbstractProduct2:
        ...


class AbstractProduct1(ABC):
    ...


class AbstractProduct2(ABC):
    ...


class ConcreteProduct1(AbstractProduct1):
    ...


class ConcreteProduct2(AbstractProduct2):
    ...


class ConcreteFactory(AbstractFactry):
    def make_product_1(self) -> AbstractProduct1:
        return ConcreteProduct1()
        
    def make_product_2(self) -> AbstractProduct2:
        return ConcreteProduct2()


def accepting_factory(factory: AbstractFactory) -> None:
    product_1 = factory.make_product_1()
    product_2 = factory.make_product_2()
    ...
```

## Adapter

## Bridge

## Chain of responsibility

## Command

## Composite

## Decorator

## Facade

## Factory method

## Flyweight

## Interpreter

## Iterator

## Mediator

## Memento

## Observer

## Prototype

## Proxy

## Singleton

## State

## Strategy

## Template method

## Visitor