def serialize_organisation(item)->dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
    }
def serialize_organisations(entity) -> list:
    return [serialize_organisation(item) for item in entity]