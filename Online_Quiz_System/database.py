import json


def load_users():
    try:
        with open("users.json", "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else []
    except:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else []
    except:
        return []


def save_leaderboard(data):
    with open("leaderboard.json", "w") as file:
        json.dump(data, file, indent=4)