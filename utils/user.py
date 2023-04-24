def serialize_user(user)->dict:
    return {
        "id": str(user["_id"]),
        "name": str(user["name"]),
        "email": str(user["email"]),
        "organisations": dict(user["organisations"]),
    }
def serialize_users(entity) -> list:
    return [serialize_user(user) for user in entity]