from datetime import date
from datetime import timedelta
from ApiRequests import launchGetRequest

INTRA_URL = "https://intra.epitech.eu/"
AUTOLOGIN_ID = "auth-4480553ba869735e3d876d27e411c916a8ca4adf"
PLANNING_URL = "/planning/load"

def formatIntraParams(nb_days) :
    today = date.today()
    end_date = today + timedelta(days=nb_days)

    res = {
        "format" : "json",
        "start" : today.strftime("%Y-%m-%d"),
        "end" : end_date.strftime("%Y-%m-%d")
    }

    return (res)

def requestIntraPlanning():
    url = INTRA_URL + AUTOLOGIN_ID + PLANNING_URL
    params = formatIntraParams(14)

    return launchGetRequest(url, params)