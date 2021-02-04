def informe(urgencias,turnos):
    print("Atendidos por urgencia: ",urgencias)
    print("Atendidos por turno: ",turnos)

def contador(lista,legajo):
    return lista.count(legajo)

urgencias = []
turnos = []

legajo = int(input("Ingrese numero de legajo: "))
while legajo!=-1:
    if int(input("Urgencia = 0, turno = 1: "))==0:
        urgencias.append(legajo)
    else:
        turnos.append(legajo)
    legajo = int(input("Ingrese numero de legajo: "))

informe(urgencias,turnos)

legajo = int(input("Ingrese numero de legajo: "))
while legajo!=-1:
    print("El paciente",legajo,"se atendio",contador(urgencias,legajo),"veces por urgencia, y",contador(turnos,legajo),"veces por turno")
    legajo = int(input("Ingrese numero de legajo: "))