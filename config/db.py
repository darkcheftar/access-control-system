from pymongo import MongoClient


database = MongoClient('mongodb://localhost:27017')
users_collection = database.access_control.users
organisations_collection = database.access_control.organisations
if 'user_name_index' not in users_collection.index_information():
    users_collection.create_index('name',name="user_name_index")
if 'org_name_index' not in organisations_collection.index_information():
    organisations_collection.create_index('name',name='org_name_index',unique=True)