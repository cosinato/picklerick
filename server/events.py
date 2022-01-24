"""
This is the events module and supports all the ReST actions for the
EVENTS collection
"""

from datetime import datetime
from flask import abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
EVENTS = {
    "0": {"user": "system", "content": "System Startup", "timestamp": get_timestamp()},
}


def get_all():
    """
    This function responds to a request for /events
    with the complete lists of events

    :return:        sorted list of events
    """
    return [EVENTS[key] for key in sorted(EVENTS.keys())]


def get_one(event_id):
    """
    This function responds to a request for /events/{event_id}

    :param name:    id of event to find
    :return:        event matching id
    """
    if event_id in EVENTS:
        event = EVENTS.get(event_id)

    else:
        abort(404, "event with event_id {event_id} not found".format(event_id=event_id))

    return event


def create(event):
    """
    This function creates a new user in the users structure
    based on the passed in user data

    :param user:  user to create in users structure
    :return:        201 on success, 406 on user exists
    """
    event_id = str(len(EVENTS) + 1)
    EVENTS[event_id] = {"content": event, "timestamp": get_timestamp()}
    return EVENTS[event_id], 201
