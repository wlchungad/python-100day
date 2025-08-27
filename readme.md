# Python 100-day challenge
## Aim
In this challenge, I would need to (in most cases) block myself from the usage of vibe coding / coding assistant / Copliot what-so-ever, and try to build something by my own mind. The code may not be perfect, and sometimes I need to refer to some dictionaries or tutorials, yet writing in such old-fashioned way could keep myself from being brainrot.

## Tasks
### Day 1 - 10
| Done | Day | Topic | To-do item |
| :---: | :---: | :---: | :--- |
| :white_check_mark: | 1 | Basic print function | Create a function to write "Hello world" |
| :white_check_mark: | 2 | Variables and data | Print the pricing of some fruit |
| :white_check_mark: | 3 | Basic I/O | Print the result (name) after user input valid name |
| :white_check_mark: | 4 | Arithmetic | Write a CLI calculator (+, –, ×, ÷) <br> *No need to error-handle for now*|
| :white_check_mark: | 5 | Conditionals | Determine which Quadrant a given coordinate is in<br>Quadrant I: `(+,+)`<br>Quadrant II: `(-,+)`<br>Quadrant III: `(-,-)`<br>Quadrant IV: `(+,-)` |
| :white_check_mark: | 6 | Loops | Write a guessing game with some simple display (similar to hangman or wordle) |
| :white_check_mark: | 7 | Functions & backtracking | Write 2 functions:<ul><li>Fibonacci Numbers<li>Factorials</ul>|
| :white_check_mark: | 8 | String & List comprehension | Create an application of Caesar Cipher to encrypt and decrypt |
| :white_check_mark: | 9 | List operations | Write a to-do list with CRUD (Create, Read, Update, and Delete) functions |
| :white_check_mark: | 10 | Dictionary | Write a contact book that contains:<br><ul><li>Name</li><li>Phone Number</li><li>E-mail address</li></ul> |

### Day 11-20
| Done | Day | Topic | To-do item |
| :---: | :---: | :---: | :--- |
| :white_check_mark: | 11 | String Operation | Palindrome test: check if a word, phrase, or sequence could be read the same backwards as forwards |
| :white_check_mark: | 12 | Randomize | Write a CoC-style Dice roller, then simulate a battle.<br>*The configuration could be wrong, please refer to the rule book.* |
| :white_check_mark: | 13 | Error handling | Write a basic calculator (read-and-execute) with zero-division handling <br>Test cases:<ul><li>365 * 1 * 2<li>1 / 0<li>365/365<li>-1+3<li>1+2-3*4/5|
| :white_check_mark: | 14 | File handling | Write a Emotional Journey application with plain-text storage <br>Bonus: try to implement with Emoji for better presentation :star:| 
| :white_check_mark: | 15 | Map, filter, and reduce | Create a JUPAS admission score calculator |
| :white_check_mark: | 16 | Exception chaining and custom exceptions | To conclude a Age-Score relation of an exam without invalid data |
| :white_check_mark: | 17 | OOP (1) - Class attributes and methods | Create a `Car` Class with:<ul><li>attributes: Brand, Model, Age</li><li>Methods: `start()`, `stop()`</li></ul>|
| :white_check_mark: | 18 | OOP (2) - Inheritance and Polymorphism | Create `Animal` Class and child Class `Cat` and `Dog`, each having different implementation of `make_sound()` |
| :white_check_mark: | 19 | OOP (3) - Encapsulation | Create a `BankAccount` class that contains protected and private members (methods & attributes)<br><b><i>Learning Point:</i></b><br><ul><li>protected members are defined with a one-underscore prefix (e.g. `self._age`)</li><li> private members are defined with two-underscore prefix (e.g. `self.__salary`)</li></ul>|
| :white_check_mark: | 20 | OOP (4) - Abstract classes, Method overloading and Method overriding | Build a ABC of shape, then define classes for Rectangle and Circle<br><b><i>Learning Point:</i></b><br><ul><li>Abstract Classes are marked with `ABC` in class and `@abstractmethod` in its methods, child classes must override the methods with `@abstractmethod`</li><li>Method Overloading is Compile time polymorphism<br>It can be set in any functions, i.e., one function accepts `*args` and handles different inputs<br>In fact, default arguments in method is also a kind of Method overloading</li><li>Method overriding is run time polymorphism<br>It works in class, i.e., child class method overwrite the same-name method from parent </li></ul> |

### Day 21-30
| Done | Day | Topic | To-do item |
| :---: | :---: | :---: | :--- |
| :white_check_mark: | 21 | Decorator | Create a logging decorator that prints the function name and arguments (args and kwargs) and a chain of simple decorators <br><b><i>Learning Point:</i></b><br><ul><li>A decorator is a "jacket" for functions to extend functionality (such as logging)</li><li>Decorators can be applied to functions, methods and classes</li><li>Decorators can be chained, and their order could affect the result</li></ul> |
| :white_check_mark: | 22 | Generator | Re-write Fibonacci number function with `yield`<br><b><i>Learning Point:</i></b><br><ul><li>Generators are functions that `yield` instead of `return`</li><li>The product of generators are iterator objects, not values (string, integers, list, etc.)</li></ul> |
| :white_check_mark: | 23 | Multithreading and Multiprocessing | <ol><li>Create a demo file of threadings and ThreadPool</li><li>Try to fetch the water quality data into text file</li></ol> |
| :white_check_mark: | 24 | (Conceptual) Undo & Redo  | Create a class with Undo and Redo functions |
| :white_check_mark: | 25 | Custom iterators | Create a countdown iterator class, and a child class of Exam Counter; present the iterator as a live timer |
| :white_check_mark: | 26 | Built-in function in Python | Create a Zipped list of student-score, then present the zipped result with enumerated IDs |
| :white_check_mark: | 27 | Context managers | Customize a File Management Context Manager<br><b><i>Learning points:</i></b><br>Context Manager automatically set up and clean up resources.<br>Benefits:<ul><li>Automatic cleanup</li><li>Avoid resource leaks</li><li>Exception-safe</li></ul> |
| :white_check_mark: | 28 | Metaclasses | <br><b><i>Learning points:</i></b><ul><li>Metaclasses are classes that define how other classes are created.</li><li>Metaclasses serve as blueprints for creating classes themselves.</li><li>If we are asking whether we need metaclasses in a situation, <u>it is not needed</u>.</li></ul> |
| :new: | 29 | Garbage collection | Create a memory usage monitor <br><b><i>Learning points:</i></b><ul><li>Garbage collection refers to memory allocation and deallocation.</li><li>Python automatically manages memory by default. However, in some cases, manual deallocation is required.</li><li>Manual collection includes:<ul><li>Time-based garbage collection</li><li>Event-based garbage collection</li></ul></li><ul> |
| :new: | 30 | Singleton | <b><i>Learning points:</i></b><br>Singleton means "Only one instance", which could be important when Database and fileaccess is limited.  | 