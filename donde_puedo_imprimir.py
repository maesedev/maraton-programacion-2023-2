def calcular_distancia(a,b):
    return abs(a-b)

def obtener_primer_indice_lugar(list,lugar):
    for i,item in enumerate(list):
        if item == lugar:
            return i
    return -1

# aqui guardamos la salida de cada ejecucion, para mostrarlas al final de seguido 
results = []

while True:
    L = int(input())
    if L == 0:
        break
    string = input()


    primer_papeleria = obtener_primer_indice_lugar(string, "P")
    primer_cafeteria = obtener_primer_indice_lugar(string, "C")
    primer_cafeteria_con_papeleria = obtener_primer_indice_lugar(string, "U")

    #caso 1: Hay una U en la entrada
    #   Significa que hay una papeleria cafeteria, en ese caso la distancia minima d es 0
    if primer_cafeteria_con_papeleria != -1:
        results.append(0)
        continue
    
    #caso 2: No hay una cafeteria C o una papeleria P en la entrada
    #   Significa que no hay una papeleria o una cafeteria, en ese caso la distancia minima d es 0
    #   ya que no hay con quien comparar
    if primer_papeleria == -1 or primer_cafeteria == -1 :
        results.append(0)
        continue
    
    #caso 3: hay una pepeleria y una cafeteria en la entrada
    C_pila = [0]
    P_pila = [0]
    distancias = []

    ultimo_apilado = ""
    for i,letter in enumerate(string):
        if letter == "P":
            P_pila.append(i)
            # Si hay elementos en la pila de Cafeterias
            if C_pila:
                dist = calcular_distancia( P_pila[-1] , C_pila[-1] )
                distancias.append(dist)

        if letter == "C":
            ultimo_apilado="C"
            C_pila.append(i)

            # Si hay elementos en la pila de papelerias
            if P_pila:
                dist = calcular_distancia( P_pila[-1] , C_pila[-1] )
                distancias.append(dist)
    results.append(min(distancias))

for result in results :
    print(result)
    



         
    
