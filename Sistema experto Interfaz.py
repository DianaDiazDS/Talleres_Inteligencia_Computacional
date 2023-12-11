import tkinter as tk
from tkinter import ttk
from experta import *


class Paciente(Fact):
    pass


class SistemaExpertoIsquemia(KnowledgeEngine):

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_1(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_2(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', IMC='grado1',
                   DR='no', FEE='no', DTM='no',
                   DTA='no', DTT='no'))
    def regla_3(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_4(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_5(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_6(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_7(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='si', CO='bajo', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_8(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='no', CO='bajo', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='si',
                   DTT='no'))
    def regla_9(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='si', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_10(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='no', AF='si', CO='alto', HF='no', HA='no', DR='no',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_11(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_12(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_13(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_14(self):
        mensaje_resultado.set("Tiene un alto riesgo de tener la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_15(self):
        mensaje_resultado.set("Tiene un alto riesgo de sufrir la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_16(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_17(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='si', AF='no', CO='muy alto', HF='no', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_18(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_19(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='no', DTM='si', DTA='no',
                   DTT='no'))
    def regla_20(self):
        mensaje_resultado.set("Tiene una probabilidad de tener la enfermedad coronaria en 5 años")

    @Rule(AS.p << Paciente())
    def regla_default(self, p):
        mensaje_resultado.set("No se puede determinar si posee o no la enfermedad coronaria")


def evaluar_isquemia(sexo, edad, diabetes, antecedentes_familiares, colesterol, fumar, hipertension, dolor_toracico,
                     fatiga, dolor_toracico_menos_un_mes,
                     dolor_toracico_mayor_tres_meses, dolor_toracico_intenso):
    engine = SistemaExpertoIsquemia()
    engine.reset()
    engine.declare(
        Paciente(SEXO=sexo, ED=edad, DM=diabetes, AF=antecedentes_familiares, CO=colesterol, HF=fumar, HA=hipertension,
                 DR=dolor_toracico, FEE=fatiga, DTM=dolor_toracico_menos_un_mes, DTA=dolor_toracico_mayor_tres_meses,
                 DTT=dolor_toracico_intenso))
    engine.run()


def obtener_diagnostico_isquemia():
    sexo = entry_sexo.get()
    edad = entry_edad.get()
    diabetes = entry_diabetes.get()
    antecedentes_familiares = entry_antecedentes_familiares.get()
    colesterol = entry_colesterol.get()
    fumar = entry_fumar.get()
    hipertension = entry_hipertension.get()
    dolor_toracico = entry_dolor_toracico.get()
    fatiga = entry_fatiga.get()
    dolor_toracico_menos_un_mes = entry_dolor_toracico_menos_un_mes.get()
    dolor_toracico_mayor_tres_meses = entry_dolor_toracico_mayor_tres_meses.get()
    dolor_toracico_intenso = entry_dolor_toracico_intenso.get()
    evaluar_isquemia(sexo, edad, diabetes, antecedentes_familiares, colesterol, fumar, hipertension, dolor_toracico,
                     fatiga, dolor_toracico_menos_un_mes,
                     dolor_toracico_mayor_tres_meses, dolor_toracico_intenso)


# Interfaz gráfica

root = tk.Tk()
root.title("Sistema Experto para Isquemia Coronaria")


def obtener_diagnostico_isquemia():
    # Aquí puedes obtener los valores de las entradas según sea necesario
    sexo = entry_sexo.get()
    edad = entry_edad.get()
    diabetes = entry_diabetes.get()
    antecedentes_familiares = entry_antecedentes_familiares.get()
    colesterol = entry_colesterol.get()
    fumar = entry_fumar.get()
    hipertension = entry_hipertension.get()
    dolor_toracico = entry_dolor_toracico.get()
    fatiga = entry_fatiga.get()
    dolor_toracico_menos_un_mes = entry_dolor_toracico_menos_un_mes.get()
    dolor_toracico_mayor_tres_meses = entry_dolor_toracico_mayor_tres_meses.get()
    dolor_toracico_intenso = entry_dolor_toracico_intenso.get()
    # Realiza las operaciones necesarias con los valores obtenidos
    evaluar_isquemia(sexo, edad, diabetes, antecedentes_familiares, colesterol, fumar, hipertension, dolor_toracico,
                     fatiga, dolor_toracico_menos_un_mes,
                     dolor_toracico_mayor_tres_meses, dolor_toracico_intenso)



root.title("Sistema Experto para Isquemia Coronaria")

# Marco para las entradas de información del paciente
frame_paciente = ttk.Frame(root, padding=10)
frame_paciente.pack(padx=20, pady=10, fill="both", expand=True)


# Función para crear etiquetas y entradas de manera más eficiente
def crear_label_y_entry(frame, label_text):
    label = ttk.Label(frame, text=label_text)
    label.grid(row=frame.grid_size()[1], column=0, sticky="w", pady=(5, 0), padx=(0, 10))

    entry = ttk.Entry(frame)
    entry.grid(row=label.grid_info()["row"], column=1, sticky="ew", pady=(5, 0))

    return entry


# Crear etiquetas y entradas
entry_sexo = crear_label_y_entry(frame_paciente, "Sexo:")
entry_edad = crear_label_y_entry(frame_paciente, "Edad:")
entry_diabetes = crear_label_y_entry(frame_paciente, "Diabetes:")
entry_antecedentes_familiares = crear_label_y_entry(frame_paciente, "Antecedentes Familiares:")
entry_colesterol = crear_label_y_entry(frame_paciente, "Colesterol:")
entry_fumar = crear_label_y_entry(frame_paciente, "Fumar:")
entry_hipertension = crear_label_y_entry(frame_paciente, "Hipertensión:")
entry_dolor_toracico = crear_label_y_entry(frame_paciente, "Dolor Torácico:")
entry_fatiga = crear_label_y_entry(frame_paciente, "Fatiga:")
entry_dolor_toracico_menos_un_mes = crear_label_y_entry(frame_paciente, "Dolor Torácico < 1 mes:")
entry_dolor_toracico_mayor_tres_meses = crear_label_y_entry(frame_paciente, "Dolor Torácico > 3 meses:")
entry_dolor_toracico_intenso = crear_label_y_entry(frame_paciente, "Dolor Torácico Intenso:")

# Botón para obtener el diagnóstico
button = ttk.Button(frame_paciente, text="Obtener Diagnóstico", command=obtener_diagnostico_isquemia)
button.grid(row=frame_paciente.grid_size()[1], column=0, columnspan=2, pady=(20, 10))

# Etiqueta para mostrar el resultado
mensaje_resultado = tk.StringVar()
label_resultado = ttk.Label(frame_paciente, textvariable=mensaje_resultado)
label_resultado.grid(row=frame_paciente.grid_size()[1], column=0, columnspan=2, pady=(10, 20))

root.mainloop()