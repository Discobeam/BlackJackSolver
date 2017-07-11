# BlackJackSolver
Python script designed to solve a modified blackjack.

# Setup

Place BlackJackSolver into any directory, and run Bot.py with Python 3.x, tested working on Python 3.5 x64 Win7. Other systems should work but are as yet untested.
You may want to tweak the source first.

# Tweaks

Config files are stored in the same directory as the program, and are currently hard-coded into the source (as of initial GitHub version), referenced on lines 12 and 50 of the source. The text file used can be changed at will, but the text file should contain 2 numbers, an initial maximum hand value (the hand value at which the bot will not draw another card), and a difference value, used to determine the next maximum value to use.
If the value used for the difference is 0, the bot will no longer learn, and will simply play games over and over with no changes made.

The formatting for a config file is simply the 2 numbers seperated by a newline character. E.g, for values 12 and 0 (Which appears to be nearly optimal)

```
0
0
```
