from fastapi import APIRouter, HTTPException
from models.organisation import Organisation
from config.db import organisations_collection, users_collection
from utils.organisation import serialize_organisations
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from pymongo import UpdateMany
from typing import Literal,List

access_levels = {'READ','WRITE','ADMIN'}

organisation = APIRouter()

# creating organisation
@organisation.post('/')
async def create_organisation(organisation:Organisation):
    try:
        organisations_collection.insert_one(dict(organisation))
        return serialize_organisations(organisations_collection.find())
    except DuplicateKeyError as e:
        raise HTTPException(status_code=400, detail="organisation already exists")


# returning all the organisations present
@organisation.get('/')
async def get_all_organisations(name: str = None, offset: int = 0, limit: int = 2):
    try:
        query = {'name':name} if name else {}
        return {
                'result': serialize_organisations(organisations_collection.find(query).skip(offset).limit(limit)),
                'total':organisations_collection.count_documents(query)
            }
    except Exception as e:
        raise HTTPException(500,str(e))


# updating users permissions
@organisation.put('/{id}/users')
async def updating_user_permission(id, permission_dict: dict[str,Literal['READ','WRITE','ADMIN']]):
    # get Organisation name
    org = organisations_collection.find_one({'_id':ObjectId(id)})
    permission_to_users = {level:[] for level in access_levels}
    # permission_dict {id:level} -> permission_to_users {level:[user]} 
    for userid, permission in permission_dict.items():
        permission_to_users[permission].append(userid)
    updates = []
    # add updates to list
    for level in access_levels:
        if permission_to_users[level]:
            updates.append(
                UpdateMany({'_id':{'$in':list(map(ObjectId,permission_to_users[level]))}},
                    {'$set':{f'organisations.{org["name"]}': level}}))
    try:
        # bulk write can also be used for single user permission
        result = users_collection.bulk_write(updates)
        return {
            "acknowledged":result.acknowledged,
            "bulk_api_result":result.bulk_api_result
        }
    except Exception as e:
        raise HTTPException(500,str(e))

# updating users permissions
@organisation.delete('/{id}/users')
async def removing_all_permission_of_user_on_organisation(id, users_list: List[str]):
    org = organisations_collection.find_one({'_id':ObjectId(id)})
    if not org:
        raise HTTPException(404,'organisation not found')
    try:
        result = users_collection.update_many({'_id':{'$in':list(map(ObjectId,users_list))}},
        {'$unset':{f'organisations.{org["name"]}': 1}})
        return {
            "acknowledged":result.acknowledged,
            "raw_result":result.raw_result
        }
    except Exception as e:
        raise HTTPException(500,str(e))