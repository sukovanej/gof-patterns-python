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

 - *abstract factory* declares an interface for operations that create abstract product objects
 - *concrete factory* implements operations to create concrete product objects
 - *abstract product* declares an interface for a type of product object
 - *concrete product* defines a product object to be created by a corresponding concrete factory
 - *clients* uses only interfaces declares by *abstract facotry* and *abstract product* classes

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