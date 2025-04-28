# Authors: Abby Brennan-Jones, Catherine Wang

from z3 import *

s = Solver()

# pseudocode
# all our constraints: topic areas of interest, preferences for being partners with
# certain people, availability, and desired grade range for the final project
# unit propagation and backtracking search

# don't match together people who hate each other
def no_hatred(formula):
    # if person A hates person B, it's mutually exclusive and A ^ B would be false