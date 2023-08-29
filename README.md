# ohce-tdd
Kata TDD outside in for ohce
## The ohce Algorithm
* Greeter: When you start ohce, depending on the time of day, the application should greet the user differently in Spanish.
* **input**
    String **name**
* **output** (condition(time of day) -> **output)**
    * Between 20 and 6 hour -> "¡Buenas noches **name**!"
    * Between 6 and 12 hours -> "¡Buenas días **name**!"
    * Between 12 and 20 hours -> "¡Buenas tardes **name**!"
* Reversal: The application should reverse and echo any input.
* **input**
    String **reverse**
* **output** (condition -> **output)**
    * -> Reverse_echo(**reverse**)
    * If String **reverse** is a palindrome -> "¡Bonita palabra!"

* Exit:  If the input is "Stop!", the application should say goodbye and terminate.
* **input**
    String **stopword**
* **output** (condition -> **output)**
    * If **stopword** is "Stop!" -> "Adios **name**" and end program    