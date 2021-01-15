## Design Patterns in Python


Code and notes following along the udemy course: 
[Design Patterns in Python](https://www.udemy.com/course/design-patterns-python/). 


###**SOLID** Design Principles:
* Introduced by Robert C. Martin.
* **Single Responsibility Principle**:
    * A class should have a primary responsibility and should not take on other responsibilities. 
    * A class should only have one reason to change. 
    * *Separation of concerns*: different classes handling different, independent tasks or problems. 
* **Open Close Principle**:
    * Classes should be open for extension, but closed for modification. 
    * After you've written and tested a class you should not modify it. Instead you should extend it.
* **Liskov Substitution Principle**:
    * If you have an interface that takes a base class, you should be able to use a derived class 
    in place of the base class.
    * In other words, you should be able to substitute a base type for a subtype.
* **Interface Segregation Principle**:
    * You should not have too many elements or methods in an interface. Instead split it into separate interfaces.
    * Avoid having elements or methods that are not needed. 
* **Dependency Inversion Principle**:
    * High level classes or modules should not depend on lower level classes or modules, instead they 
    should depend on interfaces.
    * Depending on interfaces or abstractions allows you to swap or change them easily. 



### Gamma Categorization
* Creational Patterns
    * Deal with the creation (construction) of objects.
    * Explicit (constructor) vs implicit (DI, reflection, etc).
    * Wholesale (single statement) vs piecewise (step-by-step).
* Structural Patterns
    * Concerned with the structure (e.g., class members).
    * Many patterns are wrappers that mimic the underlying class interface.
    * Stress the importance of good API design.
        * Replicating the interface as much as possible or making as convenient to use as possible.
* Behavioral Patterns
    * They are all different; no central theme.
    * Solve particular problems in unique way.   
    
    
    

### Creational Design Patterns
* Builder
    * When piecewise object construction is complicated, provide an API for doing it succinctly. 
    * Separate component for when object construction gets too complicated.
    * Can create mutually cooperating sub-builders. 
    * Often has a fluent interface. 
* Factory:
    * A component responsible solely for the wholesale (not piecewise) creation of objects.
    * Factory method more expressive than initializer. 
    * Factory can be an outside class or an inner class.
* Prototype:
    * A partially or fully initialized object that you copy (clone) and make use of. 
    * Creation of object from an existing object.
    * Requires explicit deep copy. 
* Singleton:
    * A component which is instantiated only once.
    * When you need to ensure just a single instance exists.
    * Easy to make with a decorator or metaclass.
    * Consider using dependency injection.

### Structural Design Patterns
* Adapter:
    * A construct which adapts an existing interface X to conform to the required interface Y.
    * Converts the interface you get to the interface you need.
* Bridge: 
    * A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
    * Avoids the Cartesian product complexity explosion problem.
* Composite:
    * A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.
* Decorator:
    * Facilitates the addition of behaviors to individual objects without inheriting from them.
    * Python has functional decorators. 
* Facade:
    * Provides a simple and easy to understand user interface over a large and sophisticated body of code.
    * Friendly and easy-to-use, but can provide access to low-level features.
* Flyweight:
    * A space optimization technique that lets us use less memory by storing externally the 
    data associated with similar objects.
* Proxy:
    * A class that functions as an interface to a particular resource. That resource may be remote, expensive
    to construct, or may require logging or some other added functionality.
    * Provide a surrogate object that forwards calls to the real object while performing additional functions.
    * Proxy vs decorator: proxy provides an identical interface; decorator provides an enhanced interface.
    * E.g., access control, communication, logging, etc. 
    
### Behavioral Design Patterns
* Chain of Responsibility:
    * A chain of components who all get a chance to process a command or a query, optionally 
    having default processing implementation and an ability to terminate the processing chain.
    * Allows components to process information / events in a chain.
    * Each element in the chain refers to next element; or make a list and go through it. 
* Command: 
    * An object which represents an instruction to perform a particular action. 
    Contains all the information necessary for the action to be taken.
    * Encapsulate request into a separate object.
    * Good for audit, replay, undo / redo
    * Part of Command Query Separation / Command Query Responsibility Segregation
* Interpreter:
    * A component that processes structured text data. Does so by turning it into separate 
    lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).
    * Transforms textual input into object-oriented structures. 
    * Used by interpreters, compilers, static analysis tools, etc.
    * *Compiler Theory*: separate branch of Computer Science.
* Iterator:
    * An object that facilitates the traversal of a data structure.
    * Provides an interface for accessing elements of an aggregate object.
    * `__iter__` and `__next__` are stateful, but `yield` is much more convenient.
* Mediator:
    * A component that facilitates communication between other components without them necessarily being 
    aware of each other or having direct (reference) across to each other.
    * Provides mediation services between two or more objects. 
    * E.g., message passing, chat room
* Memento:
    * A token/handle representing the system state. Lets us roll back to the state 
    when the token was generated. May or may not directly expose state information.
    * Yields tokens representing system states.
    * Tokens do not allow direct manipulation, but can be used in appropriate APIs.
* Observer:
    * Is an object that wishes to be informed about events happening in the system.
    The entity generating the events is an observable.
    * Allows notifications of changes / happenings in a component.
* State:  
    * A pattern in which the object's behavior is determined by its state. An object transitions from one 
    state to another (something needs to *trigger* a transition). 
    * A formalized construct which manages state and transitions is called a *state machine*.
    * Special frameworks exits to orchestrate state machines. 
* Strategy:
    * Enables the exact behavior of a system to be selected at run-time. 
    * Uses ordinary composition.
* Template Method:
    * Allows us to define the 'skeleton' of the algorithm, with concrete implementations 
    defined in subclasses. 
    * Uses inheritance.
* Visitor:
    * A component (visitor) that knows how to traverse a data structure composed of (possibly related) types.
    * Allows non-intrusive addition of functionality to hierarchies.