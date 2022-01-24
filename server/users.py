"""
This is the users module and supports all the ReST actions for the
USERS collection
"""

from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
USERS = {"System": {"name": "System", "timestamp": get_timestamp()}}


# Create a handler for our read (GET) users
def get_all():
    """
    This function responds to a request for /users
    with the complete lists of users

    :return:        sorted list of users
    """
    # Create the list of users from our data
    return [USERS[key] for key in sorted(USERS.keys())]


def get_one(name):
    """
    This function responds to a request for /users/{name}
    with one matching user from users

    :param name:    name of user to find
    :return:        user matching name
    """
    # Does the user exist in users?
    if name in USERS:
        user = USERS.get(name)

    # otherwise, nope, not found
    else:
        abort(404, "User with name {name} not found".format(name=name))

    return user


def create(name):
    """
    This function creates a new user in the users structure
    based on the passed in user data

    :param user:  user to create in users structure
    :return:        201 on success, 406 on user exists
    """
    # Does the user exist already?
    if name not in USERS and name is not None:
        USERS[name] = {
            "name": name,
            "timestamp": get_timestamp(),
        }
        return USERS[name], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "User with name {name} already exists".format(name=name),
        )


def update(name):
    """
    This function updates an existing user in the users structure

    :param name:   name of user to update in the users structure
    :param user:  person to update
    :return:        updated user structure
    """
    # Does the user exist in users?
    if name in USERS and name is not None:
        timestamp = get_timestamp()
        user = USERS[name]
        user["timestamp"] = timestamp

        return user

    # otherwise, nope, that's an error
    else:
        abort(404, "User with name {name} not found".format(name=name))


def delete(name):
    """
    This function deletes a user from the users structure

    :param name:   name of user to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the user to delete exist?
    if name in USERS:
        del USERS[name]
        return make_response("{name} successfully deleted".format(name=name), 200)

    # Otherwise, nope, user to delete not found
    else:
        abort(404, "User with name {name} not found".format(name=name))
