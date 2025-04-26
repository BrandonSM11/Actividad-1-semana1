Peso = int(input("Ingrese su peso en KG " ))
Altura = float(input("Ingrese su altura en M " ))
IMC = Peso / Altura **2
print ("Su indice de masa corporal es" , IMC)
if IMC < 18.5 :
    print("Bajo peso")
elif IMC > 18.5 and IMC < 24.9 :
    print("Peso normal")
elif IMC >= 25 and IMC <= 29.9 :
    print("Sobrepeso")
elif IMC >=30 :
    print ("Obesidad")





