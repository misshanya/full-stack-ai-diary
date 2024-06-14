from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str

    first_name: str
    last_name: str
    sch_class: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
