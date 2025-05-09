# final-project-matcher

Manually sorting students into project groups based on their limitations and preferences is very time-consuming and tedious, but what if we had an algorithm that could do so? Final Project Matcher is a tool that automatically matches students together into groups of 3 for a final project.

How to run Final Project Matcher:
- Download the Python script
- Run in terminal

  Note that Final Project Matcher assumes that class size is a multiple of 3 and can only match students who are not incompatible; that is, it doesn't match students who are strongly compatible (e.g., have a preference for each other). A trade-off that we made in this implementation was between adding more features and making the program feasible to implement. For example, we kept the number of possible constraints small so it would be harder for the model to become overconstrained. Some other approaches that we tried that didn’t work include modeling the problem as a graph coloring problem with 3 colors and generating all possible subsets of the set of students of size 3 and using z3 to check if they were compatible.
