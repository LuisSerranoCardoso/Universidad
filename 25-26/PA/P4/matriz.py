import numpy as np

class CMatFloat:

    """Clase que representa una matriz dinámica 1D/2D
    
        Atributos:
            _Matriz  #Almacena la matriz (utilice numpy)
            _m_nFilas #Almacena el número de filas de la matriz
            _m_nColumnas #Almacena el número de columnas de la matriz
    """
    def __init__(self, nFilas=1, nColumnas=1):
        """
        Método para incialozar el atribito matriz con None y los atributos filas y columnas a 0
        """
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz2D(self, nFilas, nColumnas):
        """
        Método para crear una matriz bidimensional de ceros.
        Asigna valores de filas y columnas según parámetros.
        """
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """
        Método para crear una matriz unidimensional de ceros.
        Usa CrearMatriz2D para asignar 1 fila y n columnas.
        """
        self.CrearMatriz2D(1, nElementos)
    def Introducir(self):
        """
        Método para introducir los elementos de la matriz.
        Los elementos de la matriz son de tipo decimal.
        """
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                valor = float(input(f"Introduce el elemento [{i}][{j}]: "))
                self._Matriz[i, j] = valor
        return self._Matriz

    def Mostrar(self):
        """
        Método para mostrar los elementos de la matriz.
        """
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                print(f"Elemento [{i}][{j}]: {self._Matriz[i, j]}")

    def Existe(self):
        """
        Método que verifica si matriz está creada y no está vacía.
        Retorna True si existe, de los contrario retorna False.
        """
        return self._Matriz is not None and self._Matriz.size > 0
    def SumarMatrices(self, otra_matriz):
        """
        Método que suma la matriz actual con otra matriz.
        
        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a sumar.
        
        Retorna:
        numpy.ndarray: La matriz resultante de la suma.
        """
        if (self._m_nFilas != otra_matriz._m_nFilas or
                self._m_nColumnas != otra_matriz._m_nColumnas):
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar.")

        matriz_resultante = CMatFloat(self._m_nFilas, self._m_nColumnas)

        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                matriz_resultante._Matriz[i, j] = (self._Matriz[i, j] + otra_matriz._Matriz[i, j])

        return matriz_resultante

    def RestarMatrices(self, otra_matriz):
        """
        Método que resta la matriz actual con otra matriz.

        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a restar.

        Retorna:
        numpy.ndarray: La matriz resultante de la resta.
        """
        if (self._m_nFilas != otra_matriz._m_nFilas or
                self._m_nColumnas != otra_matriz._m_nColumnas):
            raise ValueError("Las matrices deben tener las mismas dimensiones para restar.")

        matriz_resultante = CMatFloat(self._m_nFilas, self._m_nColumnas)

        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                matriz_resultante._Matriz[i, j] = (self._Matriz[i, j] - otra_matriz._Matriz[i, j])

        return matriz_resultante

    @staticmethod
    def leer_int(mensaje="Introduce un número entero: ") -> int:
        """
        Función auxiliar para leer un número entero del teclado.
        Si se introduce un valor no válido, se solicita de nuevo.

        Parámetros:
        mensaje (str): El mensaje que se muestra al usuario solicitando la entrada.

        Retorna:
        int: El valor entero introducido por el usuario.
        """
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")
            except EOFError:
                print("\nEntrada EOF detectada. Finalizando programa.")
                raise

    @staticmethod
    def leer_float(mensaje="Introduce un número decimal: ") -> float:
        """
        Función auxiliar que solicita al usuario un número decimal.
        Si se introduce un valor no válido, se solicita de nuevo.
        
        Parámetros:
        mensaje (str): El mensaje que se muestra al usuario solictando la entrada.

        Retorna:
        float: El valor decimal introducido por el usuario.
        """
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número decimal.")
            except EOFError:
                print("\nEntrada EOF detectada. Finalizando programa.")
                raise

    @staticmethod
    def crear_menu(opciones_menu):
        """
        El programa incluirá un menú principal con las siguientes opciones: 
            1. Construir matriz 1D: permite crear un vector unidimensional con un número definido de elementos. 
            2. Construir matriz 2D: permite crear una matriz bidimensional definiendo el número de filas y columnas. 
            3. Introducir matriz: permite al usuario ingresar los valores para la matriz creada. 
            4. Mostrar matriz: muestra los valores actuales de la matriz. 
            5. Operaciones con matrices: Lleva al usuario a un submenú donde se pueden realizar operaciones como suma y resta de matrices.
        """
        print("\nMenú Principal:")
        for clave, valor in opciones_menu.items():
            print(f"{clave}. {valor}")
        try:
            eleccion = input("Selecciona una opción: ")
            return eleccion
        except EOFError:
            print("\nEntrada EOF detectada. Finalizando programa.")
            raise

def _main():
    opciones_menu = {
        1: "Construir matriz 1D",
        2: "Construir matriz 2D",
        3: "Introducir matriz",
        4: "Mostrar matriz",
        5: "Operaciones con matrices",
        6: "Finalizar programa"
    }  
    matriz = CMatFloat(1, 1)

    try:
        while True:
            elec = CMatFloat.crear_menu(opciones_menu)
            try:
                opcion = int(elec)
            except ValueError:
                print("Opción no válida. Introduce el número de la opción.")
                continue

            if opcion == 1:
                n = CMatFloat.leer_int("Número de elementos del vector: ")
                matriz.CrearMatriz1D(n)
                print(f"Vector 1D creado con {n} elementos.")
            elif opcion == 2:
                f = CMatFloat.leer_int("Número de filas: ")
                c = CMatFloat.leer_int("Número de columnas: ")
                matriz.CrearMatriz2D(f, c)
                print(f"Matriz 2D creada de {f} filas y {c} columnas.")
            elif opcion == 3:
                if not matriz.Existe():
                    print("No hay ninguna matriz creada. Primero construye una matriz.")
                else:
                    matriz.Introducir()
            elif opcion == 4:
                if not matriz.Existe():
                    print("No hay ninguna matriz creada.")
                else:
                    matriz.Mostrar()
            elif opcion == 5:
                opciones_ops = {1: "Sumar matrices", 2: "Restar matrices", 3: "Volver al menú principal"}
                while True:
                    elec2 = CMatFloat.crear_menu(opciones_ops)
                    try:
                        op2 = int(elec2)
                    except ValueError:
                        print("Opción no válida.")
                        continue

                    if op2 == 1:
                        # Solicitar la segunda matriz
                        print("Construyendo la segunda matriz para la suma:")
                        f2 = CMatFloat.leer_int("Número de filas: ")
                        c2 = CMatFloat.leer_int("Número de columnas: ")
                        # validar dimensiones antes de solicitar elementos
                        if (f2, c2) != (matriz._m_nFilas, matriz._m_nColumnas):
                            print("Error: Las dimensiones de la segunda matriz no coinciden con la matriz actual. Operación cancelada.")
                        else:
                            otra = CMatFloat(f2, c2)
                            otra.Introducir()
                            try:
                                resultado = matriz.SumarMatrices(otra)
                                print("Resultado de la suma:")
                                resultado.Mostrar()
                            except ValueError as e:
                                print(f"Error: {e}")
                    elif op2 == 2:
                        print("Construyendo la segunda matriz para la resta:")
                        f2 = CMatFloat.leer_int("Número de filas: ")
                        c2 = CMatFloat.leer_int("Número de columnas: ")
                        if (f2, c2) != (matriz._m_nFilas, matriz._m_nColumnas):
                            print("Error: Las dimensiones de la segunda matriz no coinciden con la matriz actual. Operación cancelada.")
                        else:
                            otra = CMatFloat(f2, c2)
                            otra.Introducir()
                            try:
                                resultado = matriz.RestarMatrices(otra)
                                print("Resultado de la resta:")
                                resultado.Mostrar()
                            except ValueError as e:
                                print(f"Error: {e}")
                    elif op2 == 3:
                        break
                    else:
                        print("Opción no válida en el submenú.")
            # fin del submenú
            elif opcion == 6:
                print("Finalizando programa.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    except EOFError:
        # Entrada redirigida finalizó; salir limpiamente
        print("Entrada terminada. Saliendo.")


if __name__ == '__main__':
    _main()