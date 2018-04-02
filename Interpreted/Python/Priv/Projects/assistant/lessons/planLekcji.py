#! /usr/local/bin/python3

from __future__ import print_function
import httplib2
import os
import datetime

from apiclient import discovery
from oauth2client.file import Storage


def stuff_for_tommorow():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    timeMax = (datetime.datetime.utcnow() +
               datetime.timedelta(days=1)).isoformat() + 'Z'

    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, singleEvents=True,
        orderBy='startTime', timeMax=timeMax).execute()
    events = eventsResult.get('items', [])

    if not events:
        return('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        try:
            return(start, event['summary'], ' | ', event['description'])
        except KeyError:
            return(start, event['summary'])
