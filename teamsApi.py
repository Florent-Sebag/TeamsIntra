from ApiRequests import launchPostRequest
import datetime
from pprint import pprint

WEBHOOK_URL = "https://outlook.office.com/webhook/de4254ef-bccf-42b7-b0ec-dec271a5c70a@901cb4ca-b862-4029-9306-e5cd0f6d9f86/IncomingWebhook/d840e4a8d10d424bbf36f190622a7e26/60496e1b-99a2-4343-8e32-cc1272f4d058"

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



def createRequest(activity, summary):
    body = formatTeamsRequest(activity, summary)
    launchPostRequest(WEBHOOK_URL, body)

def sendAllActivities(activities, summary):
    for elem in activities :
        createRequest(elem, summary)

def sendActivities(modified_activities, new_activities):
    sendAllActivities(new_activities, setSummary(True))
    sendAllActivities(modified_activities, setSummary(False))

