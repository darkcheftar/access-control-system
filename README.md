# Access Control System

## Technologies Used

- Python 3 - FastAPI, PyMongo
- Mongodb as Database

## How to Execute

Step 1: Create Virtual Environment

```shell
python -m venv venv
```

Using venv

```shell
venv\Scripts\activate
```

Step 2: Install Dependencies

```shell
pip install -r requirements.txt
```

Step 3: Setup MongoDB

> - Start MongoDb create database with name `access_control`
> - replace <mongodb-connection-string\> with actual connection string in config/db.py

Step 4: Run main.py using uvicorn

```shell
uvicorn main:app --reload
```

Finally App will be live at localhost:8000

## Idea

- users, organisation collections are basic for implemention
- For implementation of permissions there can be multiple ways
  1. Creating another collection which contains the permission information required
  2. Creating a field organisations in user model
  3. Creating a field users in organisation model
  4. Creating both a field organisations in user model and a field users in organisation model

As per the given situation I felt using option 2 is good

- we can add list of users to organsations model if we require information of users related to organisation
- I used bulk updation and of permissions using bulk write

## API Docs

Autogenerated endpoints with swagger ui are present at `/docs`

#### Users API Endpoint

- Create User - `POST /users`
- Find All Users - `GET /users`
- Get A user - `GET /users/{id}`

#### Organisations API Endpoint

- Create Organisation - `POST /organisations`
- Find All Organisation - `GET /organisations`
- ##### Updating Permissions

  - update multiple users permissions for an organisation - `PUT /organisations/{id}/users`
  - delete multiple users permissions for an organisation - `DELETE /organisations/{id}/users`

### File Structure

<pre>
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│
├───config
│       config.json
│       config.json.example
│       db.py
│
├───models
│       organisation.py
│       user.py
│
├───routes
│       organisation.py
│       user.py
│
└───utils
        organisation.py
        user.py
</pre>

- `main.py` is the entry point
- `config` folder contain configurations for Database
- `models` folder contain data models for user and organisation
- `routes` folder is where various `/user` `/organisation` routes were contained
- `utils` folder contain serializers
