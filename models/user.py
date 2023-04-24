from pydantic import BaseModel, EmailStr
from typing import Dict

class User(BaseModel):
    name: str
    email: EmailStr
    organisations: Dict[str, str] = {}