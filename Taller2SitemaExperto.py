import tkinter as tk

from experta import *


class Paciente(Fact):
    pass


class SistemaExpertoIsquemia(KnowledgeEngine):

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_13(self):
        print("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='alto', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_14(self):
        print("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='m', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', IMC='grado1',
                   DR='no', FEE='no', DTM='no',
                   DTA='no', DTT='no'))
    def regla_12(self):
        print("No tiene la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='bajo', HF='no', HA='no', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_1(self):
        print("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='joven', DM='no', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_2(self):
        print("No tiene la enfermedad coronaria (isquemia)")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_4(self):
        print("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_5(self):
        print("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='si', CO='bajo', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_6(self):
        print("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='adulto', DM='no', AF='no', CO='bajo', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='si',
                   DTT='no'))
    def regla_7(self):
        print("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='si', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_8(self):
        print("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='no', AF='si', CO='alto', HF='no', HA='no', DR='no',
                   FEE='si', DTM='si', DTA='no',
                   DTT='no'))
    def regla_16(self):
        print("Tiene Angina pecho inestable")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_17(self):
        print("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='si', DTM='no', DTA='si',
                   DTT='no'))
    def regla_18(self):
        print("Tiene Angina pecho estable")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_9(self):
        print("Tiene un alto riesgo de tener la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='joven', DM='si', AF='no', CO='alto', HF='si', HA='si', DR='no',
                   FEE='no', DTM='no', DTA='no',
                   DTT='no'))
    def regla_3(self):
        print("Tiene un alto riesgo de sufrir la enfermedad coronaria")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='si', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_10(self):
        print("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='h', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_11(self):
        print("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='si', AF='no', CO='muy alto', HF='no', HA='si', DR='si',
                   FEE='no', DTM='si', DTA='no',
                   DTT='si'))
    def regla_19(self):
        print("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='mayor', DM='no', AF='no', CO='muy alto', HF='si', HA='si', DR='si',
                   FEE='si', DTM='no', DTA='no',
                   DTT='si'))
    def regla_20(self):
        print("Tiene Infarto agudo de miocardio")

    @Rule(Paciente(SEXO='m', ED='adulta', DM='si', AF='no', CO='alto', HF='no', HA='si', DR='no',
                   FEE='no', DTM='si', DTA='no',
                   DTT='no'))
    def regla_15(self):
        print("Tiene una probabilidad de tener la enfermedad coronaria en 5 años")


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
    print("Sexo:", sexo)
    print("Edad:", edad)
    print("Diabetes:", diabetes)
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
label = tk.Label(root, text="ediabetes")
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
button_obtener_diagnostico_isquemia = tk.Button(root, text="Obtener Diagnóstico de Isquemia",
                                                command=obtener_diagnostico_isquemia)
button_obtener_diagnostico_isquemia.pack()

root.mainloop()

# def evaluar_isquemia(sexo, edad, diabetes, antecedentes_familiares, colesterol, fumar, hipertension, dolor_toracico, fatiga, edema, dolor_espalda, nauseas_vomitos, sudoracion, dolor_toracico_menos_un_mes, dolor_toracico_mayor_tres_meses, dolor_toracico_intenso):
#     engine = SistemaExpertoIsquemia()
#     engine.reset()
#     engine.declare(Paciente(SEXO=sexo, ED=edad, DM=diabetes, AF=antecedentes_familiares, CO=colesterol, HF=fumar, HA=hipertension, DR=dolor_toracico, FEE=fatiga, MT=edema, EP=dolor_espalda, DEM=dolor_espalda, NV=nauseas_vomitos, SFM=sudoracion, DTM=dolor_toracico_menos_un_mes, DTA=dolor_toracico_mayor_tres_meses, DTT=dolor_toracico_intenso))
#     engine.run()
#
# def obtener_diagnostico_isquemia():
#     sexo = entry_sexo.get()
#     edad = entry_edad.get()
#     diabetes = entry_diabetes.get()
#     antecedentes_familiares = entry_antecedentes_familiares.get()
#     colesterol = entry_colesterol.get()
#     fumar = entry_fumar.get()
#     hipertension = entry_hipertension.get()
#     dolor_toracico = entry_dolor_toracico.get()
#     fatiga = entry_fatiga.get()
#     edema = entry_edema.get()
#     dolor_espalda = entry_dolor_espalda.get()
#     nauseas_vomitos = entry_nauseas_vomitos.get()
#     sudoracion = entry_sudoracion.get()
#     dolor_toracico_menos_un_mes = entry_dolor_toracico_menos_un_mes.get()
#     dolor_toracico_mayor_tres_meses = entry_dolor_toracico_mayor_tres_meses.get()
#     dolor_toracico_intenso = entry_dolor_toracico_intenso.get()
#
#     evaluar_isquemia(sexo, edad, diabetes, antecedentes_familiares, colesterol, fumar, hipertension, dolor_toracico, fatiga, edema, dolor_espalda, nauseas_vomitos, sudoracion, dolor_toracico_menos_un_mes, dolor_toracico_mayor_tres_meses, dolor_toracico_intenso)
#
# # Interfaz gráfica
# root = tk.Tk()
# root.title("Sistema Experto para Isquemia Coronaria")
#
# # (Definición de la interfaz gráfica...)
#
# # Botón para obtener el diagnóstico
# button_obtener_diagnostico_isquemia = tk.Button(root, text="Obtener Diagnóstico de Isquemia", command=obtener_diagnostico_isquemia)
# button_obtener_diagnostico_isquemia.pack()
#
# root.mainloop()
