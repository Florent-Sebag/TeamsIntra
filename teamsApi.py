from ApiRequests import launchPostRequest
import datetime
import json
from pprint import pprint

WEBHOOK_URL = "https://outlook.office.com/webhook/de4254ef-bccf-42b7-b0ec-dec271a5c70a@901cb4ca-b862-4029-9306-e5cd0f6d9f86/IncomingWebhook/"
WEBHOOK_END_URL = "/60496e1b-99a2-4343-8e32-cc1272f4d058"

def setSummary(isNewActivity):
    if isNewActivity :
        return ("A new activity is now on your intra !")
    return ("An activity has been modified")

def convertDate(toConvert):
    tmp = datetime.datetime.strptime(toConvert, '%Y-%m-%d %H:%M:%S')
    return tmp.strftime("%d/%m/%Y %H:%M")

def formatTeamsRequest(activity, summary):
    request = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": summary,
        "sections": [{
            "activityTitle": summary,
            "facts": [
            {
                "name": "Activity",
                "value": activity["acti_title"]
            },
            {
                "name": "Start date",
                "value": convertDate(activity["start"])
            },
            {
                "name": "End date",
                "value": convertDate(activity["end"])
            },
            {
                "name": "Hint",
                "value": "Dont forget to subscribe ;)"
            }
            ]
        }],
        "potentialAction": [{
            "@context": "http://schema.org",
            "@type": "ViewAction",
            "name": "Go to your intra",
            "target": ["https://intra.epitech.eu/planning/#"]
        }]
    }

    return request

def createRequest(activity, summary, urls):
    body = formatTeamsRequest(activity, summary)

    module_url_id = urls[activity["codemodule"]]
    url = WEBHOOK_URL + module_url_id + WEBHOOK_END_URL
    
    launchPostRequest(url, body)

def sendAllActivities(activities, summary, urls):
    for elem in activities :
        createRequest(elem, summary, urls)

def load_urls() :
    with open('url.json') as json_file:
        return json.load(json_file)

def sendActivities(modified_activities, new_activities):
    urls = load_urls()
    sendAllActivities(new_activities, setSummary(True), urls)
    sendAllActivities(modified_activities, setSummary(False), urls)

