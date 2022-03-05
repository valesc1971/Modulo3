#solicita ingreso de stock, almacena en variable y muestra en pantalla el stock disponible
stock=int(input("Ingrese stock de cupcakes "))
print(f"el stock actual de cupcakes es " , stock)

#solicita ingreso de la cantidad a comprar, almacena en variable y muestra en pantalla la cantidad elegida
producto_seleccionados=int(input("cuantos productos desea comprar "))
print(f"has elegido " , producto_seleccionados, 'cupcakes')

#iteracion para ingresar cantidad valida (pedido <= 20 unidades). Mientras no se cumple esa condicion, vuelve a preguntar
while producto_seleccionados >20: 
    producto_seleccionados=int(input('su pedido no puede ser mayor que 20 unidades, ingrese la cantidad nuevamente: '))
else:
    if producto_seleccionados>stock:
        print('no hay stock')
#iteracion para ingresar cantidad valida (pedido >= stock disponible). Mientras no se cumple esa condicion, vuelve a preguntar
while producto_seleccionados> stock:
    print(f'su pedido no puede ser mayor que ' ,stock, ' unidades, ingrese la cantidad nuevamente: ')
    producto_seleccionados=int(input('ingrese la cantidad nuevamente: '))

#condicional para compra sin ofertaa (unidades compradas <=12)
if producto_seleccionados<=12:
        stocknuevo=stock-producto_seleccionados
        print(f"has comprado " , producto_seleccionados)
        print(f"el stock actual de cupcakes es " , stocknuevo)
else:
    compraoferta=producto_seleccionados+1 #entra al condicional para compra con oferta (+ 1 cuando la compra es mayor a 12 unidades)
    if compraoferta<=stock: #revisar que la compra sea <= stock disponible
        stocknuevo=stock-compraoferta
        print(f'has comprado mas de 12 cupcakes. Por tu compra, te entregamos 1 de regalo , y te llevas ' ,compraoferta, 'cupcakes')
        print(f"el stock actual de cupcakes es " , stocknuevo)
    else:
        if producto_seleccionados==stock: #si se accede a la oferta pero no hay stock suficiente
            print('has comprado mas de 12 cupccakes, pero lamentamos decirte que no nos queda stock para entregarte 1 de regalo ')
            print(f"has llevado " , producto_seleccionados, "cupcakes y te regalamos un vale para que cobres tu cupcake en tu siguiente visita")
            print ('stock actual es '+str(stock-producto_seleccionados))
        



