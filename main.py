from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user, prefix='/user')
@app.get('/')
def read_root():
    return "go to /user"