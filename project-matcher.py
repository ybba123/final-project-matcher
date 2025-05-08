# Authors: Abby Brennan-Jones, Catherine Wang

from z3 import *

s = Solver()

# pseudocode
# all our constraints: topic areas of interest, preferences for being partners with
# certain people, availability, and desired grade range for the final project
# unit propagation and backtracking search
# send to z3: there is a number of groups, each person is a variable and gets assigned a group number
# data structures: 
#   input in python
#   list of dictionaries for each person with their preferences, {int (each person's ID): {"hate": [1, 2, 3];
#   "times": ["Monday morning"]; "topics": ["garbage collection"]}}
# convert each person's preferences into a formula with clauses
#
# z3 is a SAT solver so don't need to implement a whole SAT solver

# don't match together people who hate (A's group number and B's group number must be different) each other
def no_hatred(a, b, c):
    # if person A hates person B, it's mutually exclusive and A ^ B would be false
    # hatred can be one directional
    # s = Solver()
    # x = Bool('hate')

    # a = Int('person a')
    # b = Int('person b')

    # s.add(Not(And(a, b)))

    # result = s.check() # check result

    # if result == sat:
    #     print("sat")
    # else:
    #     print("unsat. person a and person b cannot be paired together")
    #     print(s.model())
    for student in a['hate']:
        if student == 'b' or student == 'c':
            return False
    for student in b['hate']:
        if student == 'a' or student == 'c':
            return False
    for student in c['hate']:
        if student == 'a' or student == 'b':
            return False
    return True

def common_preferences(a_pref, b_pref, c_pref):
    # if person A and person B have no topics in common, then they cannot be paired together
    s = Solver()
    common_pref = False
    # check if A and B have topics in common
    for item in a_pref:
        if item in b_pref and c_pref:
            return True
        
    return False


    #     for topic2 in b_pref:
    #         if topic == topic2:
    #             common_topic = True
    #             break

    # s.add(common_topic)

    # result = s.check() # check result

    # if result == sat:
    #     print("sat")
    # else:
    #     print("unsat. person a and person b cannot be paired together")
    #     print(s.model())

def main():
    # preferences = input("Enter input: ") # TODO: make this prompt more user-friendly
    preferences = [{'name':'a', 'hate':['b','c'], 'topics':['garbage collection', 'assembly/ISA'], 'times':['Monday morning', 'Monday evening']},
                   {'name':'b', 'hate':[], 'topics':['garbage collection'], 'times':['Tuesday evening']},
                   {'name':'c', 'hate':[], 'topics':['networks'], 'times':['Wednesday morning']},
                   {'name':'d', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                   {'name':'e', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                   {'name':'f', 'hate':[], 'topics':['networks'], 'times':['Friday morning']}]
    
    # for student in preferences:
