from DAL.estudiantes_repository import EstudianteRepository
from BLL.connection_manager import ConnectionManager

class EstudianteService():

    __connection_manager = ConnectionManager()
    __estudiante_repository = EstudianteRepository(__connection_manager.get_connection())


    def obtener_todos(self):
        self.__connection_manager.open_connection()
        estudiante = self.__estudiante_repository.obtener_todos()
        self.__connection_manager.close_connection()
        return estudiante

    def guardar_estudiante(self, estudiante):
        self.__connection_manager.open_connection()
        self.__estudiante_repository.guardar_estudiante(estudiante)
        self.__connection_manager.close_connection()
        return "El estudiante ha sido registrado con éxito."
