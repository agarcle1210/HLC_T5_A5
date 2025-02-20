class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

biblioteca = Biblioteca()
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.mostrar_libros()