# Ejercicio 1

def mcd(a,b):
    '''
    Función para calcular el MCD entre dos números.
    '''
    counter = 0
    c = a
    d = b
    while d!=0:
        counter = d
        d = c % d
        c = counter
    return c

def print_mcd():
    '''
    Función para comunicar cuál es el resultado.
    '''
    mcd_result = mcd(a, b)
    if mcd_result != 1:
        print(f"El MCD entre {a} y {b} es {mcd_result}.")
    else:
        print(f"{a} y {b} son números coprimos.")

# Prueba 1
a = 180
b = 1032
print_mcd()

# Prueba 2
a = 19
b = 21
print_mcd()

# Ejercicio 2

def mcm(a,b):
    '''
    Función para calcular el MCM entre dos números.
    '''
    resultado = int((a*b)/mcd(a,b))
    return resultado

a = 12
b = 22
mcm_result = mcm(a,b)
print(f"El MCM entre {a} y {b} es {mcm_result}.")

# Ejercicio 3

def dict_freq_words():
    '''
    Función que crea un diccionario con cada palabra en un párrafo y la frecuencia con la que aparecen en el texto.
    '''
    paragraph = input("Coloque un texto a continuación:\n")
    words_list = paragraph.split()
    words_freq = {}

    for w in words_list:
        if w in words_freq:
            words_freq[w] += 1
        else:
            words_freq[w] = 1
    return words_freq

print(f"\nDiccionario de frecuencias:\n{dict_freq_words()}\n")

# Ejercicio 4

def most_freq_word():
    '''
    Función que recibe un párrafo, devuelve un diccionario con cada palabra y su frecuencia, además de la palabra más frecuente y su frecuencia en forma de tupla.
    '''
    most_freq_word = None
    max_freq = 0

    for word, freq in dict_freq_words().items():
        if freq > max_freq:
            most_freq_word = word
            max_freq = freq
    return most_freq_word, max_freq

print(f"\nPalabra más repetida:\n{most_freq_word()}")

# Ejercicio 5
# Opción 1: Usando iteración de bucle While

def get_int():
    while True:
        try:
            num = int(input("Escriba un número entero: \n"))
            return num
        except ValueError as ve:
            print("Caracteres no válidos.")

int_value = get_int()
print("El número entero ingresado es:",int_value)

# Opción 2: Usando una recursión de la función get_int()

def get_int():
    try:
        num = int(input("Escriba un número entero: \n"))
        return num
    except ValueError as ve:
        print("Caracteres no válidos.")
        return get_int()

int_value = get_int()
print("El número entero ingresado es:",int_value)

# Ejercicio 6

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre if None or isinstance(nombre, str) else None
        self.__edad = edad if None or (isinstance(edad, int) and edad >= 0) else None
        self.__dni = dni if isinstance(dni, int) and 8 >= len(str(dni)) >= 7 else None
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre if isinstance(nombre, str) else print("Escriba un nombre válido.")
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Escriba un número entero positivo.")
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        if isinstance(dni, int) and 8 >= len(str(dni)) >= 7:
            self.__dni = dni
        else:
            print("DNI inválido.")
    
    def mostrar(self):
        text = "Nombre: {}\nEdad: {}\nDNI: {}".format(self.nombre, self.edad, self.dni)
        return print(text)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
# Prueba
persona1 = Persona("Franco", 20, 39035441)
persona1.mostrar()

class Cuenta:
    def __init__(self, titular = None, cantidad = 0):
        if isinstance(titular, Persona):
            self._titular = titular
            try:
                self.__cantidad = round(float(cantidad), 2) if cantidad >= 0 and (isinstance(cantidad, float) or isinstance(cantidad, int)) else 0
            except:
                print("Ingrese un número válido.")
        else:
            print("No se creó la cuenta. El titular debe ser una Persona.")
           
    @property
    def titular(self):
        try:
            return self._titular.nombre
        except:
            return "La cuenta es inexistente."

    @titular.setter
    def titular(self, titular):
            print("No es posible modificar los datos del titular.")

    @property
    def cantidad(self):
        try:
            return round(self.__cantidad, 2)
        except:
            return "No hay datos de fondos disponibles."
    
    @cantidad.setter
    def cantidad(self, cantidad):
            print("No es posible modificar los fondos.")

    def mostrar(self):
        text = "Titular: {}\nFondos: {}".format(self.titular, self.cantidad)
        return print(text)
    
    def ingresar(self, cantidad = None):
        try:
            if  cantidad >= 0 and (isinstance(cantidad, float) or isinstance(cantidad, int)):
                self.__cantidad += cantidad
            else:
                pass
        except:
            print("No se ha podido ingresar fondos.")

    def retirar(self, cantidad = None):
        try:
            if  cantidad >= 0 and (isinstance(cantidad, float) or isinstance(cantidad, int)):
                self.__cantidad -= cantidad
            else:
                pass
        except:
            print("No se ha podido retirar fondos.")

# Prueba
cuenta1 = Cuenta(persona1)
cuenta1.ingresar(200.0)
cuenta1.retirar(250.0)
cuenta1.mostrar()

class CuentaJoven(Cuenta):

    def __init__(self, titular=None, cantidad=0, bonificacion=0):
        
        if not 25>titular.edad>=18:
            print("El titular no presenta el rango etario para crear esta cuenta.")
            return
        super().__init__(titular, cantidad)
        try:
            if (isinstance(cantidad, float) or isinstance(cantidad, int)) and 100>= bonificacion >= 0:
                self.__bonificacion = bonificacion 
            else:
                print("El número ingresado es inválido.")
                self.__bonificacion = 0
        except:
            print("ERROR\nIngrese un porcentaje de bonificación numérico.\n")
            self.__bonificacion = 0

    @property
    def bonificacion(self):
        try:
            return self.__bonificacion
        except:
            return "No hay datos de bonificación disponibles."
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def es_titular_valido(self):
        try:
            edad = self._titular.edad
            return 25>= edad >= 18
        except:
            return False

    def mostrar(self):
        try:
            if self.es_titular_valido():
                super().mostrar()
                print(f"Cuenta Joven\nBonificación: {self.__bonificacion}%")
        except:
            pass

# Prueba
cuenta2 = CuentaJoven(persona1, 100, 15)
cuenta2.retirar(50)
cuenta2.mostrar()