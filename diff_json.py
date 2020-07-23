from deepdiff import DeepDiff
from pprint import pprint

def check_diff(diff, length):
    if ("root['end']" in diff["values_changed"] and "root['start']" in diff["values_changed"] and length == 2):
        return (True)
    if ("root['end']" in diff["values_changed"] and length == 1):
        return (True)
    return ("root['start']" in diff["values_changed"] and length == 1)
    

def compare_activity(old, new) :
    diff = DeepDiff(old, new)
    length = len(diff["values_changed"])
    
    if (len(diff) == 1 and "values_changed" in diff and length <= 2):
        return (check_diff(diff, length))
    return (False)
    

def find_modified_activities(old_planning, new_activities) :
    i = 0
    modified_activities = []
    for elem in old_planning :
        while i < len(new_activities):
            if (compare_activity(elem, new_activities[i])):
                modified_activities.append(new_activities[i])
                del new_activities[i]
                break
            i += 1
    return (modified_activities)


def findNewModifiedActivites(old_planning, new_planning):
    new_activites = []
    for new_elem in new_planning :
        i = 0
        isFinded = False

        while i < len(old_planning) :
            if new_elem == old_planning[i] :
                isFinded = True
                del old_planning[i]
                break
            i += 1

        if not isFinded:
            new_activites.append(new_elem)

    modified_activities = find_modified_activities(old_planning, new_activites)
    pprint(modified_activities)
    print("\n\n")
    pprint(new_activites)
    return (modified_activities, new_activites)



        