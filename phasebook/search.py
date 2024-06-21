from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    results = []

    if "id" in args:
        user_id = args["id"]
        user = next((user for user in USERS if user["id"] == user_id), None)
        if user:
            results.append(user)

    if "name" in args:
        name_query = args["name"].lower()  # Case insensitive
        filtered_users = [user for user in USERS if name_query in user["name"].lower()]
        results.extend(filtered_users)

    if "age" in args:
        age = int(args["age"])
        filtered_users = [
            user for user in USERS if user["age"] >= age - 1 and user["age"] <= age + 1
        ]
        results.extend(filtered_users)

    if "occupation" in args:
        occupation_query = args["occupation"].lower()  # Case insensitive
        filtered_users = [
            user for user in USERS if occupation_query in user["occupation"].lower()
        ]
        results.extend(filtered_users)

    # Remove duplicates if any
    results = list({user["id"]: user for user in results}.values())

    return results
