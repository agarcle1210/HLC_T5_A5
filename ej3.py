class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")

p = persona("Andrés", 18 , "la cabra")
p.presentarse()

class estudiante(persona):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado = grado

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y estoy en el grado de {self.grado}.")

e = estudiante("María", 20, "estudiante", "informática")
e.presentarse()

class trabajador(persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y trabajo en {self.empresa}.")

t = trabajador("Carlos", 30, "ingeniero", "TechCorp")
t.presentarse()