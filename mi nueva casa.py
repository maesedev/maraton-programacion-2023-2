N = int(input())
casas = []
for i in range(0,N):
    [baños, habitaciones, tiempo_llegada_trabajo, parques, valor] = input().split(" ")
    
    baños = int(baños)
    habitaciones = int(habitaciones)
    tiempo_llegada_trabajo = int(tiempo_llegada_trabajo)
    parques = int(parques)
    valor = int(valor)
    
    if baños < 2  or habitaciones < 4 or tiempo_llegada_trabajo >= 35 or parques < 4:
        continue
    casas.append(valor)

if not casas:
    print("NO DISPONIBLE")
else:
    for valor in casas:
        print(valor)


    

    

