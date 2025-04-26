Año = int(input("Ingrese un año " ) ) 
if Año %4 !=0 :
    print("No es un año bisiesto")
elif Año %4 ==0 and Año %100 !=0 :
    print ("Es bisiesto")
elif Año %4 ==0 and Año %100 ==0 and Año %400 !=0:
    print ("No es año bisiesto")
elif Año %4 ==0 and Año %100 ==0 and Año %400 ==0:
    print ("Es bisiesto")