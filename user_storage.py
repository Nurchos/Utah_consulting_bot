# user_storage.py
user_ids = set()


def add_user(user_id: int):
    user_ids.add(user_id)


def get_all_users():
    return list(user_ids)
