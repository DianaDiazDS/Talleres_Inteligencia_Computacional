import tkinter as tk

from experta import *


class Paciente(Fact):
    pass


class SistemaExpertoIsquemia(KnowledgeEngine):

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_13(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_14(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', IMC='grado1',
                   DR='no', FEE='no', DTM='no',
                   DTA='no', DTT='no'))
    def regla_12(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_1(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_2(self):
        mensaje_resultado.set("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_4(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_5(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='si', CO='bajo', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_6(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='no', CO='bajo', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='si',
                   DTT='no'))
    def regla_7(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='si', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_8(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='no', AF='si', CO='alto', HF='no', HA='no', DR='no',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_16(self):
        mensaje_resultado.set("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_17(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_18(self):
        mensaje_resultado.set("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_9(self):
        mensaje_resultado.set("Tiene un alto riesgo de tener la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_3(self):
        mensaje_resultado.set("Tiene un alto riesgo de sufrir la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_10(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_11(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='si', AF='no', CO='muy alto', HF='no', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_19(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_20(self):
        mensaje_resultado.set("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='no', DTM='si', DTA='no',
                   DTT='no'))
    def regla_15(self):
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

# (Definición de la interfaz gráfica...)

# Entradas para los datos del paciente
label = tk.Label(root, text="sexo:")
label.pack()
entry_sexo = tk.Entry(root)
entry_sexo.pack()
label = tk.Label(root, text="edad")
label.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()
label = tk.Label(root, text="diabetes")
label.pack()
entry_diabetes = tk.Entry(root)
entry_diabetes.pack()
label = tk.Label(root, text="antecedentes")
label.pack()
entry_antecedentes_familiares = tk.Entry(root)
entry_antecedentes_familiares.pack()
label = tk.Label(root, text="colesterol")
label.pack()
entry_colesterol = tk.Entry(root)
entry_colesterol.pack()
label = tk.Label(root, text="fumar")
label.pack()
entry_fumar = tk.Entry(root)
entry_fumar.pack()
label = tk.Label(root, text="hipertension")
label.pack()
entry_hipertension = tk.Entry(root)
entry_hipertension.pack()
label = tk.Label(root, text="dolor")
label.pack()
entry_dolor_toracico = tk.Entry(root)
entry_dolor_toracico.pack()
label = tk.Label(root, text="fatiga")
label.pack()
entry_fatiga = tk.Entry(root)
entry_fatiga.pack()
label = tk.Label(root, text="torax un mes")
label.pack()
entry_dolor_toracico_menos_un_mes = tk.Entry(root)
entry_dolor_toracico_menos_un_mes.pack()
label = tk.Label(root, text="torax un tres")
label.pack()
entry_dolor_toracico_mayor_tres_meses = tk.Entry(root)
entry_dolor_toracico_mayor_tres_meses.pack()
label = tk.Label(root, text="torax intenso")
label.pack()
entry_dolor_toracico_intenso = tk.Entry(root)
entry_dolor_toracico_intenso.pack()

# Botón para obtener el diagnóstico
mensaje_resultado = tk.StringVar()
label_resultado = tk.Label(root, textvariable=mensaje_resultado)
label_resultado.pack()

button = tk.Button(root, text="Obtener Diagnóstico", command=obtener_diagnostico_isquemia)
button.pack()

root.mainloop()
