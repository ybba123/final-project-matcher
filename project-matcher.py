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
    # TODO: make this prompt more user-friendly
    # TODO: make it so the user can input more than 3 student JSONs; make it so input isn't hard-coded

    # a_json = input("Enter preferences json for student a: ")

    # b_json = input("Enter preferences json for student b: ")
    # c_json = input("Enter preferences json for student c: ")
    # a_dict = json.loads(a_json)
    # b_dict = json.loads(b_json)
    # c_dict = json.loads(c_json)
    # preferences = [a_dict,b_dict,c_dict]
    # preferences = [{"name":"a", "hate":["b,c"], "topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]},
    #                {"name":"b", "hate":[], "topics":["garbage collection"], "times":["Tuesday evening"]},
    #                {"name":"c", "hate":[], "topics":["networks"], "times":["Wednesday morning"]},
    #                 {'name':'d', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
    #                {'name':'e', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
    #                {'name':'f', 'hate':[], 'topics':['networks'], 'times':['Friday morning']}]
    
    preferences = [{"name":"a", "hate":[], "topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]},
                   {"name":"b", "hate":[], "topics":["garbage collection"], "times":["Friday morning"]},
                   {"name":"c", "hate":[], "topics":["garbage collection"], "times":["Friday morning"]},
                    {'name':'d', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                   {'name':'e', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
                   {'name':'f', 'hate':[], 'topics':['garbage collection'], 'times':['Friday morning']}]
    
    # preferences = [{"name":"a", "hate":[], "topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]},
    #                {"name":"b", "hate":[], "topics":["garbage collection"], "times":["Monday morning"]},
    #                {"name":"c", "hate":[], "topics":["garbage collection"], "times":["Monday morning"]}]

    s = Solver()
    num_students = len(preferences)
    print("num_students",num_students)
    num_groups = math.floor(num_students/3)
    print("num_groups",num_groups)

    # assign ints to students
    for i in range(len(preferences)):
        group_num = Int(f'group_num_{i}') # program breaks if you change this to 'group_num'; the index is important apparently
        # add constraint for size
        s.add(group_num >= 0)
        s.add(group_num < num_groups)
        preferences[i]["group number"] = group_num
        # print(preferences[i]["group number"])

    for student in preferences:
        for student2 in preferences:
            if student2 == student:
                continue
            for student3 in preferences:
                if student3 == student or student3 == student2:
                    continue
                # check if they have the same group number. If they do, this implies that constraints are true
                s.add(Implies(student["group number"] == student2["group number"],
                            And(common_topic(student,student2,student3),
                                And(no_hatred(student,student2,student3),
                                    common_time(student,student2,student3)))))

    result = s.check()

    if result == sat:
        model = s.model()
        # print(f"Group 1: Student {preferences[0]['name']}, Student {preferences[1]['name']}, and Student {preferences[2]['name']}")
        for i in range(num_groups):
            print(f"\nGroup {i}:")
            for student in preferences:
                # print(student["group number"])
                # print(model.evaluate(student["group number"]))
                if model.evaluate(student["group number"]) == i:
                    print(student["name"])
    else:
        print("Students are incompatible.")

main()

# TODO: add testing
# TODO: clean up file, document