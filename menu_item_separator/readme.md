## Menu Item Separator
As the name says, this program gets *names* and *prices* and separates them with *points* as in a menu with the $ sign (mexican peso) and (.00) at the end. At the start you will be asked for the *number of items* in the list (im lazy brah). The *maximum length* per line will be called L.
Example:
```
Cantidad de productos: 3
nombre: Item a
precio: 90
_._._._._._._._._._._._._._._._._._._._._
nombre: ItEm aB
precio: 130
_._._._._._._._._._._._._._._._._._._._._
nombre: Item examPLe3
precio: 34555
_._._._._._._._._._._._._._._._._._._._._
¿Cuánta separación quieres?
```
return for L = 25:
```
|||||||||||||||||||||||||||||||||||||||||
Item a............$90.00
Item ab...........$130.00
Item example3.....$34555.00
|||||||||||||||||||||||||||||||||||||||||
¿Desea cambiar la separación? (Y/N)
```
If you press Y you can change L, in this case to 10:
```
Item a$90.00
Item ab$130.00
Item example3$34555.00
```
And in this case to 35:
```
|||||||||||||||||||||||||||||||||||||||||
Item a......................$90.00
Item ab.....................$130.00
Item example3...............$34555.00
|||||||||||||||||||||||||||||||||||||||||
```
Press anything besides Y to exit.
### Now what?
* Maybe if I want I'll implement some import from a plain text file or excel.
* Maybe I'll write in a .txt file the result.
* Maybe you can import from a plain text file without structure based on *"This is the title so it has no numbers", "Parentheses are used as a description so ill format it too", "Generally numbers in a menu are prices and has the currency close".*
But all this are only ideas, it isn't in my plans to actually implement them to this full-functiona-i.don't.need.more program.
