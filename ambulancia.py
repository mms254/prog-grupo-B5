class Ambulancia:
    cantidad = 0
    def __init__(self, matricula, zona, cantidad_paramedicos, modelo, sirena, paramedicos):
        self.matricula = matricula
        self.zona = zona
        self.modelo = modelo
        self.cantidad_paramedicos = cantidad_paramedicos
        if sirena not in ['bitonal', 'secuencial']:
            raise ValueError('Ese tono de sirena no existe en esa base de datis, por favor, prueba otra vez con bitonal o secuencial')
        self.sirena = sirena
        self.paramedicos = []
        Ambulancia.cantidad +=1

    def agregar_paramedico(self, paramedico):
        if paramedico in self.paramedicos:
            print(f'El paramédico {paramedico.nombre} ya está en esta ambulancia.')
            return
        else:
            self.paramedicos.append(paramedico)

    def recoger_paciente(self, paciente):
        self.paciente = paciente
        if self.paciente.estado.lower() == 'urgente':
            velmax = 200
        if self.paciente.estado.lower() == 'grave':
            velmax = 150
        if self.paciente.estado.lower() == 'leve':
            velmax = 90
        else:
            velmax = 0
        return velmax