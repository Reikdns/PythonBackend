from pydantic import BaseModel


class Nota(BaseModel):
    id_estudiante: int
    nota: float