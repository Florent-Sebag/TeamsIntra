#!/usr/bin/env python3

import os
import json
from diff_json import findNewModifiedActivites
from intraApi import requestIntraPlanning
from teamsApi import sendActivities

def saveData(data):
    if os.path.exists(".old.json"):
        os.remove(".old.json")

    new_file = open(".old.json", "a")
    json.dump(data, new_file)

def getNewActivities(new_planning) :
    with open('.old.json') as json_file:
        old_planning = json.load(json_file)

    tmp = old_planning
    old_planning = new_planning
    new_planning = tmp
    
    return (findNewModifiedActivites(old_planning, new_planning))
    

# Request from Intra API the actual planning between today and in two weeks
planning = requestIntraPlanning()

# Get old planning & compare to new
# save all differences in new dictionnary
# save date differencies on an other dictionnary
activities = getNewActivities(planning)

# parse the json to get only the required informations
# send msg to teams api
sendActivities(activities[0], activities[1])


#saveData(planning)



