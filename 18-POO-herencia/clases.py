# Herencia es la posibilidad de compartir atributos y metodos 
# entre clase. y que diferentes clases hereden de otras

# En este archivo vamos a crear nuestra clase padre
# que sera el molde para crear objetos personas genericas
# personas con las mismas propiedades y metodos

class persona:
    """
    nombre
    apellido
    altura
    edad
    """

# Siempre hay que definir los getter y los setter para un objeto

# Defino metodos que me van a permitir sacar los valores que tienen las diferentes propiesdades cuando yo cree mi objeto
        
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

# Defino metodos que me permitan asignarle un valor a las diferentes propiedades

    def setNombre(self, nombre):
        self.nombre =nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setEdad(self, edad):
        self.edad = edad

    def setAltura(self, altura):
        self.altura = altura

# Definir las funciones, las acciones genericas que una persona puede hacer

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"
    
# Aqui termina la configuracion de la clase padre y comenzamos a definir las cualidades individuales de cada persona
# pero estas personas "Heredaran y tendran cualidades basicas de la clase padre" pero ademas se sumaran los extras

# Creo un Informatico:

class informatico(persona): #en los parentesis escribimos el nombre de la clase que queremos heredar
    """ # propiedades de esta persona
    lenguajes   
    experiencia 
    """

    def __init__(self): # defino un metodo constructor para que cuando cree el objeto le asigne valores a las propiedades
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

# Aqui creo un metodo para el informatico en concreto que me permita sacar todos los lenguajes que tiene
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self,lenguajes):   #Le defino una habilidad, similar a un setter pero con return
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def experiencia(self, experiencia):
        self.experiencia = experiencia
        return self.experiencia
    
    def programar(self):            # Defino acciones
        return "Estoy programando"
    def repararOrdenador(self):
        return "Estoy reparando un ordenador"
    
# Creo un Tecnico de redes:

class tecnicoDeRedes(informatico): # Este heredara ahora de Informatico

    def __init__(self):
        super().__init__()   # con este comando esta clase tambien heredara las propiedades del padre
        self.auditarRedes = "Experto"
        self.experienciaRedes = "15 años"

    def auditoria(self):   #creo un metodo auditoria por es algo que solo puede hacer un tecnico de redes
        return "Estoy auditando una red"