from fastapi import APIRouter
import numpy
from BLL.connection_manager import ConnectionManager
from Entity.estudiante import Estudiante

from BLL.estudiante_service import EstudianteService

router = APIRouter()

estudiante_service = EstudianteService()
connection = ConnectionManager()



@router.post("/guardar_estudiante")
def guardar_estudiante(estudiante: Estudiante):
    return estudiante_service.guardar_estudiante(estudiante)


@router.get("/obtener_todos")
def obtener_todos():
    return estudiante_service.obtener_todos()
