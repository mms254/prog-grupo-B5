class Ambulancia:
    cantidad = 0
    def __init__(self, matricula, zona, modelo, sirena):
        self.matricula = matricula
        self.zona = zona
        self.modelo = modelo
        if sirena not in ['bitonal', 'secuencial']:
            raise ValueError('Ese tono de sirena no existe en esa base de datis, por favor, prueba otra vez con bitonal o secuencial')
        self.sirena = sirena
        self.paramedicos = []
        Ambulancia.cantidad +=1
    @classmethod
    def cantidad_ambulancias(cls):
        return cls.cantidad

    def agregar_paramedico(self, paramedico):
        if paramedico in self.paramedicos:
            print(f'El paramédico {paramedico.nombre} ya está en esta ambulancia.')
            return
        else:
            self.paramedicos.append(paramedico)

    def recoger_paciente(self, paciente):
        self.paciente = paciente
        if self.paciente.estado.lower() == 'urgente':
            return 200
        if self.paciente.estado.lower() == 'grave':
            return 150
        if self.paciente.estado.lower() == 'leve':
            return 90
        else:
            return 0

    def __str__(self):
        return f'Ambulancia {self.matricula} - Zona: {self.zona} - Modelo: {self.modelo} - Sirena: {self.sirena}'