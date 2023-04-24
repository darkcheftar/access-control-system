from fastapi import FastAPI
from routes.user import user
from routes.organisation import organisation

app = FastAPI()

app.include_router(user, prefix='/user')
app.include_router(organisation, prefix='/organisation')
@app.get('/')
def read_root():
    return "go to /user"