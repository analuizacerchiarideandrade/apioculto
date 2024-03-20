import re
from pydantic import validator, BaseModel


class Setores(BaseModel):
    nome: str

