# Bikupan-Solver

Solver for a swedish puzzle called Bikupan which has the form of a beehive. The beehive starts with one word around a number and its your job to fill out the rest of the words, there is only one solution. 

Ignore the HTML, CSS and the app.py code, that is for an upcoming website version of the solver. 

## How it works

By using two objects, hiveClass and hexClass the puzzle is divided into two parts. the individual "hexes" which are the words that surround a number, and the "hive" that contains all the hexes. 

The main function in ´main.py´ starts generating 25 hex objects with their corresponding numbers, that are later inserted into the main hive object. A specified starting word is inserted at a specified location in its correct orientation, it is importaint that the words orientation matches the one in the puzzle. 

The hive is then updated so that all the hexes neighboring the first hex recieve their letters so that they contain the same information, knowing that for example, the top left letter of a neighbour to the right would correspond to the top right letter of the hex. 

A function is used to find all the neighbours of each hex, and a more advanced function updatehexes() under hiveClass is used to give all the hexes their letters.

The ´order()´ function is used to pick out the order of at what hex should recieve the next word. This makes the program way faster than my previous approach of cycling all the hexes from top to bottom and also solves a problem that occurred when hexes in a circle would form a word in the center that doesen't exist.
The ´order()´ function works by getting all the neighbours of the first hex, and then getting the neighbours of those neigbours untill its reached the edges.

Lastly the hive gets filled by, in order, inserting all avalable words at the first location. The words can be clockwise and counter clockwise. If a word is inserted, a copy is made of the hive to allow for more words to be inserted at the same location, untill all possible permutations have been found. 

The program then loops through all hexes according to the order untill all avalable words have been inserted and all hexes have been filled and there is only one hive remainig.

## Example

In the running example the word "GENERA" is placed at location 14. The top letter in the puzzle is "R", followed by "E" on the top right, then "N" bottom right and so on clockwise untill all words have been filled. 

The order function finds that the nearest neighbour algorithm tells the program use the order: 13, 10, 11....

All avalable words are tested in location 13 untill all permuations have been found, which in this case are 8 total permutations or possibilities. 

It then proceeds to insert a word at location 10, and finds that there are 21 total permutations and so on. 

the program continues finding that at one point there are 84 different permutations after inserting words in a certain order. 



## How to run it

The termcolour package is used to make the numbers red in the console, and is optional. 

To run the code with the included example, just run ´main.py´ and it will output one hive per hex inserted. 



## Misc

Fonts Used: 

- Century Gothic Bold for numbers
- Century Gothic for Letters


