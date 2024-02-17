from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from Entity.estudiante import Estudiante, EstudianteResponse
from BLL.connection_manager import ConnectionManager
from Entity.nota import Nota


class EstudianteRepository():
    def __init__(self, connection):
        self.connection = connection

    def obtener_estudiantes(self):
        return self.__Estudiantes

    def obtener_todos(self):
        estudiantes = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT identificacion, nombre, sexo, fecha_ingreso, fecha_nacimiento, AVG(n.nota)"
            "FROM estudiantes e "
            "LEFT JOIN notas n "
            "ON e.id = n.id_estudiante "
            "GROUP BY identificacion"
        )
        result = cursor.fetchall()
        for item in result:
            estudiantes.append(self.mapear_estudiante(item))

        cursor.close()
        return estudiantes

    def guardar_estudiante(self, estudiante: Estudiante):

        id = None
        cursor = self.connection.cursor()

        sql = ("INSERT INTO estudiantes(identificacion, nombre, sexo, fecha_ingreso, fecha_nacimiento) "
               "VALUES(%s, %s, %s, %s, %s)")

        values = (
            estudiante.identificacion,
            estudiante.nombre,
            estudiante.sexo,
            str(estudiante.fechaIngreso),
            str(estudiante.fechaNacimiento))

        cursor.execute(sql, values)
        self.connection.commit()
        id_estudiante = cursor.lastrowid
        cursor.close()

        nota1 = Nota(id_estudiante=id_estudiante, nota=estudiante.notas[0])
        nota2 = Nota(id_estudiante=id_estudiante, nota=estudiante.notas[1])
        nota3 = Nota(id_estudiante=id_estudiante, nota=estudiante.notas[2])
        notas = (nota1, nota2, nota3)
        self.guardar_nota(notas)

    def guardar_nota(self, notas):
        cursor = self.connection.cursor()

        sql = ("INSERT INTO notas(id_estudiante, nota) "
               "VALUES(%s, %s)")

        values = (
            (notas[0].id_estudiante, notas[0].nota),
            (notas[1].id_estudiante, notas[1].nota),
            (notas[2].id_estudiante, notas[2].nota)
        )

        cursor.executemany(sql, values)
        self.connection.commit()
        cursor.close()

    def mapear_estudiante(self, registro):
        return EstudianteResponse(
            identificacion=registro[0],
            nombre=registro[1],
            sexo=registro[2],
            fechaIngreso=registro[3],
            fechaNacimiento=registro[4],
            promedio = registro[5] if registro[5] is not None else 0
        )


