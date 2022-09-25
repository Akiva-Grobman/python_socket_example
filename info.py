import pydantic


class Info(pydantic.BaseModel):
    info: str
