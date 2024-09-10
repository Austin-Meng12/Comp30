# CSE3120 Object Oriented Programming 1

## Definitions

__Object-oriented Analysis (ODA)__ is the process of looking at a problem, system, or task and and idenitifying the objects and interactions between those objects. It answers the question, _what needs to be done_?
    * Often, then process identifies properties and actions for the problem/system/tasks.
    * Example: what makes a chair, a chair?
    * Examples: Does a table fall under your definition of a chair? How would you change your definition of a chair?

__Object-Oriented Design (OOO)__ is the process of converting the identifies objects and iteractions from OOA into object behaviours. It answers the question, _how things interact_?

__Object-oriented Programming (OOP)__ is the process of implementing the outcome of OOD into a function program.
    * OOP is the most common form of programming framework.
    * Structures the program around _how data is managed_ instead of how the program manages data.


A __Class__ is a model of an object. Classes contain __attributes__ and _behaviours_, which are inherited by objects instantiated from the class.
Another definition of a class is a blueprint or a template. 
* An _Attribute_ is a property of characteristic an object possesses. Each object can have different values for the attributes, but all objects instantiated from the class 
    inherits the attributes. Other names for attributes include _memebers_ and _properties_. 
* A _Behaviour_ is an action that can be performed on an object. Behaviours are formally named _Methods_ and are written the same as a function. Therefore, methods can also accept parameters and return values. 
* One major advantage to methods is they automatically have acess to all atrributes within the object. Therefore, object only have to pass arguments for data outside of the object. 
* Methods always have at least one argument, '''self''', which indicates that the function refers to the current object.
  * __Contructors__ are methods that provide the object with the default set of attributes. In python, it is  '''self.\_\_int\_\_()'''. Contructors create the object from the class template with the values within the attributes. Other attributes can be the defaults of the class. 
  * In general, all attributes of the object should be present in the Constructor, even if the default value is None.

```python
class Die:
    
    
        def __init__(self, maxValue):  # constructor
            self.maxVal = maxValue  # argument passed from the constructor
            self.mass = 0.01 # default value



    if __name__ == "__main__":
        Die = Die(6)    # constructs the Die object
```


An __Object__ is a unique set of data and functions instantiated from a class. An object accesses attributes and method using _dot notation_. 
Which identifies the object, then the attribute or value.

```python
<object>.<attriubte> = VALUE
<object>.<method>(PARAMETERS) // date the PARAMETER data into the object 
VARIABLES = <object>.<method>() // object returns the data to the rest of the program.
```

A __God object__ or __system object__ is an object that connects or has many methods that connect to other objects. System objects are indications that the developer is programming procedurally in an object-oriented environment. Thus, the advantages of OOP is lose when there is only one main system object.
    * This problem is often found when learning to program in java.

    

# Unified Modeling Language

A standardized modeling language unifying notational systems and approaches to data management and software design. This language is programming language agnostic and does not require programming background to utilize. It is composed of three main diagram types, structure, behaviour, interactions.

NOTE: While software developers require knowledge of all three diagrams, this unit will only focus on strucuture

A class diagram is a common strucutre diagram. It contains the name of the class, the attributes and methods of the class

|Bank Account | |
| --- | --- | 
| _attribute_| _Data Type_ |
| AccountNo | int | 
| AccountType | obkect |
| Balance | float | 
| ClientID | object | 
| TransactionHistory | object |
| _Methods(parameters)_ | _return_ |
| chargeTransaction(float) | None |
| depositFunds(float) |  None |
| withdrawFunds(float) | float | 










