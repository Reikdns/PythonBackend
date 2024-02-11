from fastapi import APIRouter

from Entity.estudiante import Estudiante
from DAL.estudiantes import Estudiantes

router = APIRouter()

@router.get("/obtener_todos")
def obtener_todos():
    return Estudiantes

@router.get("/obtener_por_nombre")
def obtener_por_nombre(nombre):
    return next(filter(lambda estudiante: estudiante.nombre == nombre, Estudiantes))

@router.post("/guardar_estudiante")
def guardar_estudiante(estudiante: Estudiante):
    Estudiantes.append(estudiante)
    return "¡El estudiante ha sido guardado con éxito!"

@router.get("/filtrar")
def filtrar(calificacion: int):
    return [estudiante.nombre for estudiante in Estudiantes if numpy.mean(estudiante.notas) >= calificacion]