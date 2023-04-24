from pydantic import BaseModel, EmailStr

class Organisation(BaseModel):
    name: str