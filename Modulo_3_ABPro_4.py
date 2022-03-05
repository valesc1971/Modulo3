import random
import time
print()
print( "*" *42 +"Bienvenido a nuestra pasteleria CAMPCAKE" +"*" *42 )  
print()    

provtot=150
stock={'galletas':120, 'pasteles':150}

compra=0
count=1
while ((compra<=stock["galletas"]) or (compra<=stock['pasteles'])):
    print('Compra # ',count)
    tipo=(random.choice(list(stock))) #selecciona tipo de producto
    compra = (random.randint(1,10))     #genera compra
    print('Compra ' , compra, 'del producto', tipo)
    #print(compra)
    print('stock inicial del producto ' ,tipo, 'es ', stock[tipo] )           
    if compra>stock[tipo]:
        print('no hay stock suficiente')
        print()

        break
    else:

        stock[tipo]=stock[tipo]-compra             #descuenta venta a inventario
        print('stock del producto ', tipo , 'despues de la compra es ' ,stock[tipo])
        
        while provtot>0:            #loop para enviar remesa cuando el stock baja de 100 unidades
            if stock[tipo] <100:
                stock[tipo]=stock[tipo]+50
                print('Llegaron del proveedor 50 productos nuevos de ', tipo)
                provtot=provtot-50
            break
        else:
            print('los proveedores dejaron de enviar producto')
        
        #print(stock)
        time.sleep(0.5)
        if count%10==0:
            #print(stock)
            print(f'quedan',stock["galletas"] , 'de galletas')
            print(f'quedan',stock["pasteles"] , 'de pasteles')
        print('................................')


        count=count+1
print( "*" *42 +"Gracias por comprar en CAMPCAKE" +"*" *42 )




