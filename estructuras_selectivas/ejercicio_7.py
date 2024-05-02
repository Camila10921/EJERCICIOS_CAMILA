#en una llantera se ha establecido una promoción de 
#las llantas marca "todo terreno" 
totalLlantas=int(input("ingrese la cantidad de llantas que va a comprar: ")) #declaro una variable en la cual le pida al usuario ingresar la cantidad de llantas que va a llevar 
if totalLlantas < 5: #colocamos if para el problema si son menos de 5 llantas
    precioPorllanta=300 #colocamos el precio que le queda por llanta si son menos de 5 llantas 
elif totalLlantas >= 5 and totalLlantas <= 10: #colocamos elif y and porque va entre 5 y 10 llantas
    precioPorllanta=250 #colocamos el precio que le queda por llanta si son entre 5 y 10 llantas 
elif totalLlantas > 10: #colocamos elif si son mas de 10 llantas
    precioPorllanta=200 #colocamos el precio que le queda por llanta si son mas de 10 llantas
montoTotal=totalLlantas*precioPorllanta #realizamos la operación necesaria
print("cantidad de llantas compradas", totalLlantas, "en la cual cada llanta le sale por", precioPorllanta, "y debera pagar", montoTotal, "en total") #imprimimos el mensaje que queremos que le salga al usuario

