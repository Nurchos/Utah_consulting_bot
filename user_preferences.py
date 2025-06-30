import json

USER_FILE = "user_data.json"


def add_user(user_id: int):
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if str(user_id) not in data:
        data[str(user_id)] = {"language": "ru"}

    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def set_user_language(user_id: int, language: str):
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if str(user_id) not in data:
        data[str(user_id)] = {}

    data[str(user_id)]["language"] = language

    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def get_user_language(user_id: int) -> str:
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(str(user_id), {}).get("language", "ru")
    except FileNotFoundError:
        return "ru"


def get_all_users() -> list[int]:
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [int(uid) for uid in data.keys()]
    except FileNotFoundError:
        return []
