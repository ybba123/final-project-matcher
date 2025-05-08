# Authors: Abby Brennan-Jones, Catherine Wang

from z3 import *
import json

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
def no_hatred(a_pref, b_pref, c_pref):
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
    for student in a_pref['hate']:
        if student == 'b' or student == 'c':
            return False
    for student in b_pref['hate']:
        if student == 'a' or student == 'c':
            return False
    for student in c_pref['hate']:
        if student == 'a' or student == 'b':
            return False
    return True

def common_topic(a_pref, b_pref, c_pref):
    # if person A and person B have no topics in common, then they cannot be paired together
    s = Solver()
    common_pref = False
    # check if A and B have topics in common
    for topic in a_pref['topics']:
        if topic in b_pref['topics'] and c_pref['topics']:
            return True
        
    return False

def common_time(a_pref, b_pref, c_pref):
    # if person A and person B have no topics in common, then they cannot be paired together
    s = Solver()
    common_pref = False
    # check if A and B have topics in common
    for topic in a_pref['times']:
        if topic in b_pref['times'] and c_pref['times']:
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
    a_json = input("Enter preferences json for student a: ") # TODO: make this prompt more user-friendly
    b_json = input("Enter preferences json for student b: ")
    c_json = input("Enter preferences json for student c: ")
    a_dict = json.loads(a_json)
    b_dict = json.loads(b_json)
    c_dict = json.loads(c_json)
    preferences = [a_dict,b_dict,c_dict]
    # preferences = [{"name":"a", "hate":["b,c"], "topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]},
    #                {"name":"b", "hate":[], "topics":["garbage collection"], "times":["Tuesday evening"]},
    #                {"name":"c", "hate":[], "topics":["networks"], "times":["Wednesday morning"]}]
                #     {'name':'d', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                #    {'name':'e', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                #    {'name':'f', 'hate':[], 'topics':['networks'], 'times':['Friday morning']}
                
    # for student in preferences:
    s = Solver()

    s.add(no_hatred(preferences[0],preferences[1],preferences[2]))
    s.add(common_topic(preferences[0],preferences[1],preferences[2]))
    s.add(common_time(preferences[0],preferences[1],preferences[2]))

    result = s.check()

    if result == sat:
        print(f"Group 1: Student {preferences[0]['name']}, Student {preferences[1]['name']}, and Student {preferences[2]['name']}")
    else:
        print("Students are incompatible.")

main()