#programa cuenta con 2 partes:
    #una para ingrso de nuevo clientes/productos
    #otra para ingreso de una compra para un cliente
    #el menu inicial direcciona a una opcion o la otra
    
import random
import time

clientes={
    'cliente1':['carlos','20'],
    'cliente2':['fernando','25'],
    'cliente3':['alejandro','30'],
    'cliente4':['valeria','35'],
    'cliente5':['rodrigo','40'],
    'cliente6':['anibal','45'],
    'cliente7':['javier','50'],
    'cliente8':['olivia','55'],
    'cliente9':['elena','60'],
    'cliente10':['andrea','65']
    }

productos={
    'prod1':['cupcake','150','amarillo'],
    'prod2':['galleta','300','rojo'],
    'prod3':['torta15','525','café'],
    'prod4':['alfajor','230','verde'],
    'prod5':['pastel','450','azul']}

#listas para usar en el llenado de la base clientes-compras
compra_lista_almacena=[]  #lista provisoria para almacenar datos de la compra - para 1 entrada de varias compras, almacena todo junto
compra_lista_almacena_final=[]   #lista provisoria para separar lista compra_lista_almacena en sublistas

print( '\n' + "*" *42 +"Bienvenido a nuestra pasteleria CAMPCAKE" +"*" *42 +'\n' )

print( '\n' + "*" *42 +"MENU" +"*" *42 +'\n' )

menu=input('Ingrese 1 para agregar clientes / Ingrese 2 para ingresar una compra ')

if menu=='1':

    print('Nuestros clientes son: \n')     #imprime diccionario de clientes
    print('USUARIO \t NOMBRE \t EDAD')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
    #print(clientes)


    print('\n Nuestros productos son \n')    #imprime diccionario de productos
    print('ID \t PRODUCTO \t PRECIO \t COLOR')
    for k,v in productos.items():
        print(k,'\t',v[0],'\t', v[1],'\t', v[2])

    #agrega cliente nuevo  a listado de cliente -cliente NO debe estar en la list inicial
    print('..........................................\n')   
    print('agregar cliente a cliente{}\n')
    ID_cliente='cliente1'
    while ID_cliente in clientes.keys():
        ID_cliente=input('Para agregar un nuevo cliente, ingrese su ID (ej: cliente1): ')
        if ID_cliente not in clientes.keys():
            nombre=input('Ingrese nombre cliente: ')
            edad=input('Ingrese edad cliente: ')      
    clientes[ID_cliente]=[nombre,edad]
    print('\nEl cliente agregado es: ', ID_cliente, ' nombre: ' ,nombre, ' edad: ', edad )

    print('USUARIO \t NOMBRE \t EDAD')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
    #agrega producto nuevo  a listado de productos -producto NO debe estar en la list inicial
    print('..........................................\n')   
    print('agregar producto productos{}\n')
    id_P="prod1"
    while id_P in productos.keys():
        id_P=input('Para agregar un nuevo producto, ingrese su ID (ej: prod1): ')
        if id_P not in productos.keys():
            nombreP=input('Ingrese nombre producto: ')
            precioP=input('Ingrese precio producto: ')
            colorP=input('Ingrese color producto: ')
    productos[id_P]=[nombreP,precioP,colorP]
    print('\nEl producto agregado es ', id_P, ' nombre: ' ,nombreP, ' precio: ', precioP, ' color: ', colorP )

    print('ID \t PRODUCTO \t PRECIO \t COLOR')
    for k,v in productos.items():
        print(k,'\t',v[0],'\t', v[1],'\t', v[2])

    #muestra base de datos de clientes
    print('..........................................\n')       
    print('mostrar clientes \n')
    print('USUARIO \t NOMBRE \t EDAD')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
        
    #muestra base de datos de productos
    print('..........................................\n')       
    print('mostrar productos\n')
    print('ID \t PRODUCTO \t PRECIO \t COLOR')
    for k,v in productos.items():
        print(k,'\t',v[0],'\t', v[1],'\t', v[2])

    #elimina un cliente al azar
    print('..........................................\n')
    print('eliminar cliente al azar\n')
    for key3 in random.sample(clientes.keys(), 1):
        cliente_eliminado=list(clientes.pop(key3))     #del clientes[key3]  #del no permite almacenar la variable eliminada - usamos pop para poder mostrar el cliente eliminado
    print('El cliente eliminado es, ', cliente_eliminado[0], '\t',cliente_eliminado[1],'\n')
    #imprime nuevo listado de clientes (sin el cliente eliminado)
    print('USUARIO \t NOMBRE \t EDAD')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
        
    #elimina el ultimo producto del diccionario de productos
    print('..........................................\n')
    print('eliminar ultimo key de productos\n')     
    producto_eliminado=list(productos.popitem())  #usamos popitem para almacenar el producto eliminado en una variable
    print('El producto eliminado es ', producto_eliminado[0], '\t',producto_eliminado[1][0],'\t', producto_eliminado[1][1],'\n')
    #imprime nuevo listado de productos sin el producto eliminado
    print('ID \t PRODUCTO \t PRECIO \t COLOR')
    for k,v in productos.items():
        print(k,'\t',v[0],'\t', v[1],'\t', v[2])

    #imprime claves de clientes con delay de tiempo(0.5 seg par hacerlo mas rapido)
    print('..........................................\n')   
    print('imprime claves con delay de 1 seg \n')
    for key4 in clientes.keys():
        print(key4)
        time.sleep(0.5)

    #imprime valores de clientes con delay de 0.5 seg par hacerlo mas rapido
    print('..........................................\n')       
    print('imprime valores de clientes con delay de 3 segundos\n')    
    for key5 in clientes.values():
        print('nombre: ', key5[0],' \t edad: ', key5[1])
        time.sleep(0.5)

    #imprime id de clientes
    print('..........................................\n')   
    print('imprime id de clientes \n')
    for key6 in clientes.keys():
        print(key6)

    #modifica id de clientes aregandole _piloto al final de cada uno
    print('..........................................\n')   
    print('modifica los IDs\n')
    clientes = {key7+"_piloto" : value7 for key7, value7 in clientes.items()}
    #imprime listado de clientes con el ID modificado
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
    #elimina los ultimos 4 clientes del listado
    print('..........................................\n')   
    print('eliminar los ultimos 4 id clientes en listado\n')
    print('Los clentes eliminados son: \n')
    for i in range (4):
        nuevo_cliente_eliminado=list(clientes.popitem())
        print(nuevo_cliente_eliminado[0], '\t' ,nuevo_cliente_eliminado[1][0],'\t', nuevo_cliente_eliminado[1][1])
    #imprime listado de clientes sin los clientes eliminados
    print('\nLos clientes que quedan en el listado son: \n')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])
        
    print( "*" *42 +"Pasteleria CAMPCAKE" +"*" *42 )  

#----------llenado de lista clientes-compra
if menu=='2':
    print('.'*40+'Bienvenidos a nuestra pasteleria CAMPCAKE'+'.'*40+'\n' )
    print('.'*40+'Este es nuestro sistema de compras'+'.'*40+'\n' )

    #imprime diccionario de clientes
    print('Nuestros clientes son: \n')     
    print('USUARIO \t NOMBRE \t EDAD')
    for k,v in clientes.items():
        print(k,'\t',v[0],'\t', v[1])

    #imprime diccionario de productos
    print('\n')
    print('Nuestros productos son: \n')    
    print('ID \t PRODUCTO \t PRECIO \t COLOR')
    for k,v in productos.items():
        print(k,'\t',v[0],'\t', v[1],'\t', v[2])
    print('..........................................\n')

    #pide input para venta --- cliente, producto a comprar y cantidad
    #permite ingresar otra venta hasta que respuesta==n
    print('\nPara cada venta, debe ingresar el ID del cliente, el ID del producto a comprar y la cantidad de producto a comprar\n')
    cont=1
    respuesta='s'
    while respuesta=='s':
        compra_cliente='cliente1'
        compra_cliente=input('ingrese cliente  ej: cliente1 ')
        while compra_cliente not in clientes.keys():
            compra_cliente=input('Debe ingresar un cliente de la lista de clientes  ej: cliente1 ')
        if compra_cliente in clientes.keys():
            compra_producto='prod1'
            compra_cant='1'
            compra_producto=input('ingrese producto a comprar ej: prod1 ')
            while compra_producto not in productos.keys():
                compra_producto=input('Debe ingresar un producto de la lista de productos ej: prod1 ')
            if compra_producto in productos.keys():
                compra_cant=input('ingrese cantidad de producto a comprar ej: 10 ')
        #a partir del producto ingresado (clave), va al diccionario {productos} y extrae los valores de nombre, precio y color  para esa clave de producto
                nombre_producto=productos[compra_producto][0]
                precio_prod=productos[compra_producto][1]
        compra_prod_color=productos[compra_producto][2]
        compra_lista_almacena.append(compra_cliente)
        compra_lista_almacena.append(compra_producto)
        compra_lista_almacena.append(nombre_producto)
        compra_lista_almacena.append(precio_prod)
        compra_lista_almacena.append(compra_prod_color)
        compra_lista_almacena.append(compra_cant)
        compra_valor=int(precio_prod)*int(compra_cant)
        compra_lista_almacena.append(compra_valor)
        #ingresa a ciclo para hacer otra compra
        respuesta=input('\n otra compra? s/n ')
        if respuesta=='n':
            #separa lista inicial en sublistas para separar las compras de los clientes/productos
            for i in range(0,len(compra_lista_almacena), 7):
                compra_lista_almacena_final.append(compra_lista_almacena[i:i+7])
            print('las compras ingresadas son: \n')
            print('ID CLIENTE\tIDPROD\tPRODUCTO\tPRECIO \tCOLOR\t \tCANTIDAD\tVALOR')
            for h in compra_lista_almacena_final:
                print(h[0],'\t', h[1],'\t', h[2],'\t', h[3],'\t', h[4],'\t', h[5],'\t'*2, h[6], )
                #print(*h, sep='\t')
            print('\n'+'.'*40+'Gracias por comprar en CAMPCAKE'+'.'*40 )
        else:
            cont=cont+1     #aumenta cont en 1 par entrar nuevamente al ciclo while

