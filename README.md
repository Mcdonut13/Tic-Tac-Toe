

#### Intro

A simple tic-tac-toe game made in Python. This is my final project from the Python Essentials course from Cisco Network Academy. 



#### Install and run

If you haven't already, you'll need to have Python installed to run the game locally - https://www.python.org/downloads/


Download this repo to a folder location on your computer.

Right-click on the folder name where the game file is installed and select "Open in Terminal"

\-OR- 

Open a Terminal window and navigate to the directory where the tic-tac-toe.py file lives.

E.g. C:\\Users\\user\\MyProjects\\TTT>

Run the game on Windows by entering 'python tic-tac-toe.py'

\-OR-
On a Mac, Enter 'python3 tic-tac-toe.py'



#### The game

It's simple -- play tic-tac-toe against the computer.
Win, Lose, or Tie, you can play as many times as you want!



#### Instructions for creating the game

These are the instructions provided by Cisco Network Academy for completing this project, for reference.



"The board should be stored as a three-element list, while each element is another three-element list. e.g. board\[row]\[column]
The computer (i.e., your program) should play the game using 'X's;
The user(e.g., you) should play the game using 'O's;
The first move belongs to the computer − it always puts its first 'X' in the middle of the board;
All the squares are numbered row by row starting with 1 (see the example for reference)
Example:
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

The user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10,
and it cannot point to a field which is already occupied;
The program checks if the game is over − there are four possible verdicts: the game should continue , the game ends with a tie, you win, or the computer wins;
The computer responds with its move and the check is repeated;
Don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game."

