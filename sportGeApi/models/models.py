from pydantic import BaseModel


class Datas(BaseModel):
    team_name: str
    team_point: int
