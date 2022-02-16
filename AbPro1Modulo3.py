"""Grupo de trabajo: Valeria Sanchez, Fernando Quezada, Carlos Galleguillos, Alejandro Lanas"""

Cupcakes=int(input("Ingrese numero de Cupcakes - Precio $1.000 c/u "))
Torta1=int(input("Ingrese numero de Torta Princesa - Precio $10.000 c/u "))
Galleton=int(input("Ingrese numero de Galleton de choc - Precio $500 c/u "))
Torta2=int(input("Ingrese numero de Torta de nuez - Precio $15.000 c/u "))
Alfajor=int(input("Ingrese numero de Alfajor - Precio $1.500 c/u "))
PrecioCup=1000
PrecioT1=10000
PrecioGall=500
PrecioT2=15000
PrecioAlf=1500
Tot=(Cupcakes*PrecioCup+ Torta1*PrecioT1+Galleton*PrecioGall+Torta2*PrecioT2+Alfajor*PrecioAlf)
print("El Valor neto de su pedido es:  $" + (f"{Tot:,}".replace(',','.')))
iva=int(Tot*0.19)
print("El IVA del total de su pedido es:  $" + (f"{iva:,}".replace(',','.')))
print("El Valor total de su compra es:  $" + (f"{(Tot+iva):,}".replace(',','.')))
