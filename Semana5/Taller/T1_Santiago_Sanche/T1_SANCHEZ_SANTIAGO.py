import numpy as np 
x = 2 + 2 + 3 + 7 
E = 200 * (1000)
l = float(0.2*x)
l1 = float(1.5)
fs_flu = (1.14)
#se determinan los valores admitidos de esfuerzo que pueden soportar los elementos mediante el factor de seguidad 
esf_adm_flu_ten = 250 / fs_flu
esf_adm_flu_cor = 145 / fs_flu
#CABLE BC BD BE Se calcularà con el esfuerzo normal admisible la fuerza máxima que pueden resistir
area_cable = np.pi * ((1/4)/2 * 25.4)**2 
area_perno = np.pi * ((1/2)/2 * 25.4)**2     
fuerza_cable = area_cable * esf_adm_flu_ten      
#PERNOS
# CORTANTE SIMPLE C D E Se calcularà con el esfuerzo cortante admisible la fuerza máxima que pueden resistir
fuerza_perno_simples = area_perno * esf_adm_flu_cor
#CORTANTE DOBLE A B Se analizará el esfuerzo cortante para saber la fuerza máxima que pueden resistir
fuerza_perno_doble = 2 * area_perno * esf_adm_flu_ten 
# Se debe encontrar la menor fuerza que será la que fallará primero y tomaremos esa para hallar el resto de incognitas
fuerza_max = min(fuerza_cable,fuerza_perno_simples,fuerza_perno_doble)


#MEDIANTE LA ESTÁTICA  HALLAREMOS EL VALOR DE WMAX
anguloBC = 40 
anguloBE = 50 

# FUERZAS EN X
#Ax - np.sin(anguloBC)*fuerza_max + np.sin(anguloBE)*fuerza_max = 0
#FUERZAS EN Y
#Ay - WMAX + np.cos(anguloBC)*fuerza_max + np.cos(anguloBE)*fuerza_max + fuerza_max = 0
#SUMATORIA DE MOMENTOS EN A
#l * np.cos(anguloBC)*fuerza_max + l * np.cos(anguloBE)*fuerza_max + l * fuerza_max - l/2 * WMAX = 0 

#AX , AY, WMAX,
matriz = np.array([
    [1, 0, 0], 
    [0, 1, -1],
    [0, 0, - l/2 ]
])
vector = np.array([np.sin(anguloBC)*fuerza_max-np.sin(anguloBE)*fuerza_max, -np.cos(anguloBC)*fuerza_max - np.cos(anguloBE)*fuerza_max - fuerza_max, -l * np.cos(anguloBC)*fuerza_max - l * np.cos(anguloBE)*fuerza_max - l * fuerza_max])
solucion = np.linalg.solve(matriz,vector)
WMAX = solucion[2]

#DEFORMACIONES EN LOS CABLES - COMO LA FUERZA ES LA MISMA EN LOS TRES CABLES LA DEFORMACIÒN SERÀ IGUAL EN LOS TRES CASOS 
#CABLE BC
defor_cable_BC = fuerza_max * l1 / (area_cable * E )
#CABLE BD
defor_cable_BD = fuerza_max * l1 / (area_cable * E )
#CABLE BE
defor_cable_BE = fuerza_max * l1 / (area_cable * E )

#RESULTADOS 
# FUERZAS
AX = solucion[0]
AY = solucion[1]
WMAX = solucion[2]
CABLE_CB = fuerza_max
CABLE_CD = fuerza_max
CABLE_CE = fuerza_max

float(fuerza_max)
float(defor_cable_BC)

lista1 = ["CABLE_CB", "CABLE_CD", "CABLE_CE"]


for e in lista1:
    print("La fuerza a tensión del " + str(i) + " es igual a " + str(fuerza_max) + " Newtons")

for e in lista1:
    print("La deformación del " + str(i) + " es igual a " + str(defor_cable_BC) + " milimetros al cuadrado")

print("La fuerza en la reacción AX es igual a " + str( solucion[0]) + " Newtons")
print("La fuerza en la reacción AY es igual a " + str( solucion[1]) + " Newtons")
print("La fuerza máxima que puede tomar la fuerza W es igual a " + str( solucion[2]) + " Newtons")
  

   