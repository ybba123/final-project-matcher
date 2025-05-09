# Authors: Abby Brennan-Jones, Catherine Wang

from z3 import *
import json

s = Solver()

def no_hatred(a_pref, b_pref, c_pref):
    # don't match together people who hate each other; 'hatred' may be one-directional
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

def sanity_check(preferences, model):
    # checks if students assigned as group mates are actually compatible
    for student in preferences:
        for student2 in preferences:
            if student2 == student:
                continue
            for student3 in preferences:
                if student3 == student or student3 == student2:
                    continue
                # check if students with the same group number are compatible
                student1_num = model.evaluate(student["group number"])
                student2_num = model.evaluate(student2["group number"])
                student3_num = model.evaluate(student3["group number"])
                if (student1_num == student2_num and student2_num == student3_num 
                    and (not no_hatred(student, student2, student3) 
                    or not common_topic(student, student2, student3)
                    or not common_time(student,student2,student3))):
                    print("error; incompatible students matched together")

def main():
    
    # For testing:
    # preferences = [{"name":"a", "hate":[], "topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]},
    #                {"name":"b", "hate":[], "topics":["garbage collection"], "times":["Friday morning"]},
    #                {"name":"c", "hate":[], "topics":["garbage collection"], "times":["Friday morning"]},
    #                 {'name':'d', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
    #                {'name':'e', 'hate':[], 'topics':['networks','garbage collection'], 'times':['Monday morning']},
    #                {'name':'f', 'hate':[], 'topics':['garbage collection'], 'times':['Friday morning']}]

    preferences = []

    print("Input a JSON representing a student's preferences. Here is an example of the required format:")
    print('{"name":"a", "hate":["name of student b","name of student c"], ' \
    '"topics":["garbage collection", "assembly/ISA"], "times":["Monday morning"]}')
    print('Type "d" when you are done entering all the preference JSONs for all your students.')
    ans = ""
    while ans != "d":
        ans = input("Enter input: ")
        if ans != "d":
            preferences.append(json.loads(ans))

    s = Solver()
    num_students = len(preferences)
    num_groups = math.floor(num_students/3)

    # assign ints to students
    for i in range(len(preferences)):
        group_num = Int(f'group_num_{i}')
        # add constraint for size
        s.add(group_num >= 0)
        s.add(group_num < num_groups)
        preferences[i]["group number"] = group_num

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
        sanity_check(preferences, model)
        for i in range(num_groups):
            print(f"\nGroup {i}:")
            for student in preferences:
                if model.evaluate(student["group number"]) == i:
                    print(student["name"])
    else:
        print("Students are incompatible.")

main()
