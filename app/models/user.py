from pydantic import BaseModel

class User(BaseModel):
    user_id: int | None = None
    username: str
    password: str
    email: str
    roles: list[str] = []
    disabled: bool | None = None
    
class UpdateUser(BaseModel):
    username: str
    email: str
    

class Password(BaseModel):
    password: str