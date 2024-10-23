Basic Connect4 program. The GUI is quite simple and rudimentary. The idea for the bot is to use a heuristic function. It first checks wether there is a winning move
in the current depth, so it either blocks or makes it. After that it searches for the best score based on the heuristic function. The score starts from 21 and it goes down
for one color and goes up for the other.
The heuristic function takes 1 solo piece as 0.1, 2 pieces as 0.3 and 3 pieces as 0.9. The algorithm also checks wether the row/column/diagonal is blocked on both sides.
If it's blocked it makes the score 0.1
