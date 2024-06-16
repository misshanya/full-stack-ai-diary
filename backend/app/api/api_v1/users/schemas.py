from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: bytes

    first_name: str
    last_name: str
    sch_class: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: str | None = None
    password: bytes | None = None

    first_name: str | None = None
    last_name: str | None = None
    sch_class: int | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
