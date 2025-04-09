class Enfermedad:
    def __init__(self, nombre, sintomas, cronica=False):
        if not nombre or not sintomas:
            raise ValueError('Debe proporcionar nombre y síntomas para la enfermedad.')
        self.nombre = nombre
        self.sintomas = sintomas
        self.cronica = cronica
        self.grave = False
        self.pacientes = []
    def marcar_grave(self):
        self.grave = True
        return f'La enfermedad: {self.nombre} ha sido marcada como grave.'
    def obtener_info(self):
        return (f'Enfermedad: {self.nombre}\n'
                f'Síntomas: {self.sintomas}\n'
                f'Crónica: {self.cronica}\n'
                f'Grave: {self.grave}\n')
    def paciente_tiene_enfermedad(self, paciente):
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)
            paciente.asignar_enfermedad(self)
        else:
            print('El paciente ya tiene esa enfermedad asignada')
    def listado_pacientes(self):
        return self.pacientes
