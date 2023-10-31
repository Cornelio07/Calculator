import sqlite3

conn  = sqlite3.connect('Ejemplos')
cursor = conn.cursor()
#Linea para eliminar tablas 
#cursor.execute('''Drop Table mi_tabla''')

"""
Tabla de para dar de alta un paciente con sus datos 

cursor.execute('''CREATE TABLE Pacientes (
                    id INT PRIMARY KEY,
                    nombre VARCHAR(255),
                    edad INT,
                    genero VARCHAR(10),
                    historial_medico TEXT
                )''')

Tabla de Procedimientos Médicos
cursor.execute('''CREATE TABLE ProcedimientosMedicos (
                    id INT PRIMARY KEY,
                    paciente_id INT,
                    fecha DATE,
                    tipo_procedimiento VARCHAR(255),
                    ubicacion_defecto_oseo VARCHAR(255),
                    biomaterial_id INT,
                    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id)
                )''')

Tabla de Biomateriales
cursor.execute('''CREATE TABLE Biomateriales (
                    id INT PRIMARY KEY,
                    composicion TEXT,
                    cantidad_utilizada DECIMAL(10, 2)
                )''')

Tabla de Resultados Clínicos
cursor.execute('''CREATE TABLE ResultadosClinicos (
                    id INT PRIMARY KEY,
                    procedimiento_id INT,
                    fecha_evaluacion DATE,
                    calidad_tejido_oseo DECIMAL(5, 2),
                    cantidad_tejido_oseo DECIMAL(5, 2),
                    FOREIGN KEY (procedimiento_id) REFERENCES ProcedimientosMedicos(id)
                )''')
"""
cursor.execute('''SELECT Pacientes.nombre, ProcedimientosMedicos.fecha, Biomateriales.composicion
                    FROM Pacientes
                    JOIN ProcedimientosMedicos ON Pacientes.id = ProcedimientosMedicos.paciente_id
                    JOIN Biomateriales ON ProcedimientosMedicos.biomaterial_id = Biomateriales.id''')

conn.commit()
conn.close()