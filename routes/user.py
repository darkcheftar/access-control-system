from fastapi import APIRouter, HTTPException
from models.user import User
from config.db import database
from utils.user import serialize_users,serialize_user
from bson import ObjectId

user = APIRouter()
users_collection = database.access_control.users
# creating user
@user.post('/')
async def create_user(user:User):
    try:
        response = users_collection.insert_one(dict(user))
        return serialize_user(users_collection.find_one({'_id':response.inserted_id}))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# returning all the users present
@user.get('/{id}')
async def get_user(id):
    result = users_collection.find_one({"_id":ObjectId(id)})
    if result:
        return serialize_user(result)
    else:
        raise HTTPException(status_code=404,detail="user not found")

# returning all the users present
@user.get('/')
async def find_all_users(name: str = None, offset: int = 0, limit: int = 2):
    try:
        query = {'name':name} if name else {}
        return {
                'result': serialize_users(users_collection.find(query).skip(offset).limit(limit)),
                'total': users_collection.count_documents(query)
            }
    except Exception as e:
        raise HTTPException(500,str(e))