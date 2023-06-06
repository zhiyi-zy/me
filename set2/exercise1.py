"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think the variable some_words defines a list of strings that are indexed from 0 onwards
some_words = ["what", "does", "this", "line", "do", "?"] # it defines the list some_words to ["what", "does", "this", "line", "do", "?"]

# I think this will iterate through all the words in the some_words list and print it
for word in some_words:
    print(word) # it looped through and printed all the words in the some_words list

# I think this will iterate through all the words in the some_words list and print it (same as above)
for x in some_words:
    print(x)    # it looped through and printed all the words in the some_words list

# I think this will print out the list of some_words
print(some_words)   # it printed out the list ["what", "does", "this", "line", "do", "?"]

# I think it will print out the statement "some_words contains more than 3 words" if the length of the list is more than 3
if len(some_words) > 3:
    print("some_words contains more than 3 words")  # it printed out the statement as the length of some_words list is true (6 > 3)

# I think it defines a function called usefulFunction
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think it will print out a fairly portable uname interface and returns a namedtuple() containing six attributes: system, node, release, version, machine, and processor.
    print(platform.uname())

# I think the it will print out the fairly portable uname interface as it is being called 
usefulFunction() # it printed out uname_result(system='Windows', node='DESKTOP-BHBA9M6', release='10', version='10.0.22621', machine='AMD64')
