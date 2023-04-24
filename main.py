from fastapi import FastAPI
from routes.user import user
from routes.organisation import organisation

app = FastAPI()

app.include_router(user, prefix='/users')
app.include_router(organisation, prefix='/organisations')
@app.get('/')
def welcome_page():
    return "go to /users or /organisations or /docs"