stock = {"ZAPATILLAS": 20, "POLERAS": 10, "ZAPATOS": 15 , "POLERÓN": 3, "CHAQUETA": 5 , "GUANTES": 4 }      #define diccionario inicial con productos y unidades en stock
clientes = ["anibal", "maria", "francisca", "pedro", "ana"]  #define lista inicial con clientes

######### CONTROL BODEGA   #######

def actualizar_stock():         #ingresa producto nuevo y lo almacena en diccionario stock{}
    producto = input("Ingrese un nuevo producto: ").upper()
    while producto in stock.keys(): #validacion para ingresar un producto que no este en stock{}
        print('\nProducto ingresado ya se encuentra en el listado de producto\n')
        producto = input("Ingrese un nuevo producto: ").upper()     #ingresa producto nuevo
    if producto not in stock.keys():
        valor = int(input("Ingrese la cantidad del nuevo producto: ")) #ingreso del stock de producto nuevo
        stock[producto]=valor   #almcena el producto nuevo y su stock en {stock}
        print('El producto ingresado es: ', producto,' y su stock es ', valor)
        stock[producto]=valor
    #print(stock)
def ingreso():                  #consulta para seguir ingresando productos nuevos
    requ_ingr = True
    while requ_ingr:
        ver_ing = input("¿Quieres ingresar un nuevo producto?: si / no ")
        if ver_ing.upper() == "SI":
            actualizar_stock()
        elif ver_ing.upper() == "NO":
            print(stock)
            requ_ingr = False
        else:
            print("-"*25 + "El valor ingresado no es válido, intente de nuevo" + "-"*25)
def actualizar_valor():         #actualiza cantidad de unidades de productos que estan en inventario sumandole la nueva cantidad
    producto = input("Seleccione el producto que quiere modifica: ").upper()
    if producto in stock.keys():    #verifica que el producto se encuentre en {stock}
        valor = (input("Ingrese la cantidad a actualizar ")) #ingresa las unidades a agregar
        while not (valor).isdigit():    #verifica que valor ingresado sea un numero positivo entero
                valor=input("El valor debe ser un numero entero positivo ")
        else:
            valor=int(valor)        
            for existencia in stock.keys():     #agrega la cantidad ingresada al stock existente
                if existencia == producto:      #verifica que el producto este en {stock}
                    valor2 = int(stock.get(producto))   #extrae el stock inicial del producto en {stock}
                    stock[existencia]=(valor + valor2)  #suma stock inicial y unidades agregadas
                    print(stock)
    else:
        print("El producto no existe")
def stock_disp():               #imprime listado de productos y su stock
    print('\nPRODUCTO\t\tSTOCK\n')
    for prod,val in stock.items():
        print(prod.title(),"\t\t", val)

def stock_prod_disp():
    seguir_consultando=True
    while seguir_consultando:
        producto = input("Seleccione producto para revisar su stock: ").upper()    #validacion de prducto existente
        if producto not in stock.keys():
            print("El producto no existe")
        else:
            print(producto , stock[producto])       #imprime producto seleccionado y su stock
        pregunta_otro_stock=(input('Desea consultar el stock de otro producto si/no: ')).upper()    #consulta para revisar stock de otro prod
        seguir_consultando_error=True
        while seguir_consultando_error:     #valida respuesta de pregunta
            if pregunta_otro_stock=='NO':
                seguir_consultando=False
                seguir_consultando_error=False
            elif pregunta_otro_stock=='SI':
                seguir_consultando=True
                seguir_consultando_error=False
            else:
                seguir_consultando=True
                seguir_consultando_error=True
                print('error - el valor ingresado no se valido')
                pregunta_otro_stock=(input('Desea consultar el stock de otro producto si/no: ')).upper()

def mostr_prod():       #despliega listado de productos y sus stocks
    print("Los productos actualmente en stock son:\n")
    for prod in stock.keys():
        print(prod.title())

def mostr_mas_unid():   #despliega listado de productos con mas de cierta cantidad de unidades
    lista1=[]
    cant = int(input("Ingrese la cantidad que busca: \n"))
    print('\nProductos en stock que tienen mas de ', cant,': \n')   #consulta la cantidad buscada
    print('\nPRODUCTO\t\tSTOCK\n')      #imprime los productos que cumplen con la condicion
    for prod, val in stock.items():
        if val > cant:
            print(prod, '\t\t',val)
            lista1.append([prod,val])   #almacena en una lista los productos que cumplen con la condicion
    #print(lista1)
    if len(lista1)==0:  #revisa que esta lista este vacia; de ser asi, significa que ningun producto cumple con la condicion.
        print('No hay productos con inventario mayor a ',cant)

####### CONTROL DE VENTAS ########

def usuarios_registrados():     #despliega listado de clientes
    print('\nExisten ',len(clientes), 'cliente registrados')
    print('\nLos clientes registrados son: \n')
    for nombre in range (0,len(clientes)):
        print(clientes[nombre].title())

def compra():
    usuarios_registrados()  #despliega lista de clientes 
    compra_lista_almacena=[]    #lista para almacenar la compra (cliente producto y stock)
    compra_cliente=(input('\nIngrese cliente: ')).lower()   #ingreso de cliente que compra
    while compra_cliente not in clientes:   #verifica que cliente este dentro de la lista
        compra_cliente=(input('Debe ingresar un cliente de la lista de clientes. Ingrese nuevamente. ')).lower()
    if compra_cliente in clientes:
            compra_producto=''
            compra_cant='1'
            mostr_prod()    #despliega lista de productos
            compra_producto=(input('\nIngrese producto a comprar: ')).upper()  #ingreso de producto a comprar
            while compra_producto not in stock.keys():  #verifica que producto este dentro de la lista
                compra_producto=(input('Debe ingresar un producto de la lista de productos. Ingrese nuevamente. ')).upper()
            if compra_producto in stock.keys():
                compra_cant=(input('\nIngrese unidades de producto a comprar (ej: 10): '))  #ingreso de unidades a comprar
                if compra_cant=='':     #valor por defecto=1 (en caso de que se ingrese enter, se asume q es 1 unidad de producto)
                    compra_cant=1
                    print('Se ha seleccionado 1 unidad del producto ')
    compra_lista_almacena.append(compra_cliente)    #almacena cliente en lista q almacena la compra
    compra_lista_almacena.append(compra_producto)   #almacena producto en lista q almacena la compra
    compra_lista_almacena.append(int(compra_cant))  #almacena unidades en lista q almacena la compra
    remanente=stock[compra_producto]-int(compra_cant)   #calcula lo que queda en stock para el producto q se esta comprando
    print('\nSu compra es:','\n',compra_cant, ' ',compra_producto,'\n') #imprime resumen de compra
    return remanente            #almacena valor para ser usado en las funciones siguientes

def validacion_compra():        #Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
    validacion=compra()         #validacion = return de compra() = remanente de producto. Esto se usa para verifica que haya producto en stock para satisfacer las unidades que se esta comprando
    validado=validacion>=0       #asigna valor TRUE si remanente es >= 0 (si hay stock suficiente para la compra)
    #print(validado)
    return validado                #almacena validado como resultado de la funcion validacion_compra

def compra_aprobada():  #Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega virtual(aprueba/cancela)
    validado_respuesta=validacion_compra()
    if validado_respuesta==True:    #si este valor es verdadero, hay stock suficiente para la compra
        print('FELICITACIONES!!!. Su compra ha sido aprobada y va en camino\n')
    elif validado_respuesta==False: #si este valor es falso, no hay stock suficiente para la compra
        print('Lo sentimos. No hay stock suficiente por lo que su compra ha sido cancelada\n')


##### MENU PRINCIPAL ####
def ejecutar():
    respuesta_menu=True
    while respuesta_menu:
        print('\n','-'*40, 'MENU PRINCIPAL', '-'*40,'\n')   #despliega menu principal
        opcion_menu_principal=(input('Bienvenido al Menu Principal. Ingrese su opcion.\n\nBodega\nVentas\nSalir\n')).upper()
        if opcion_menu_principal == 'BODEGA': #ingresa a menu de bodega
            solicitud_ingreso = True
            while solicitud_ingreso:
                print('\n','-'*40, 'MENU BODEGA', '-'*40,'\n')      # despliega menu de bodega
                soli = input("1 Ingresar producto nuevo\n2 Actualizar stock de productos\n3 Consultar stock de todos los productos \n4 Consultar stock por producto especifico\n5 Listado de productos\n6 Consultar productos con stock mayor a 'x' unidades\n7 Volver al Menu Principal\n")
                if soli == "1":
                    ingreso()       #ingreso de nuevos productos
                elif soli == "2":
                    actualizar_valor()  #actualizar stock de productos
                elif soli == "3":
                    stock_disp()         #despliega stock de todos los productos       
                elif soli == "4":
                    stock_prod_disp()      #despliega stock disponible para 1 solo producto
                elif soli == "5":
                    mostr_prod()          #despliega listado de productos
                elif soli == "6":
                    mostr_mas_unid()       #despliega productos con unidades mayor que ingresada por consola         
                elif soli == "7":
                    solicitud_ingreso = False #sale del menu
                    respuesta_menu=True
                else:
                    print("Opción no válida")
        elif opcion_menu_principal == 'VENTAS':   #ingresa a menu de ventas
            solicitud_ingreso_venta = True
            while solicitud_ingreso_venta:
                print('-'*40, 'MENU VENTAS', '-'*40,'\n') #despliega menu de venta
                soli = input("1 Mostrar numero de clientes\n2 Comprar\n3 Volver al Menu Principal\n")
                if soli == "1":
                    usuarios_registrados()          #despliega clientes registrado
                elif soli == "2":
                    compra_aprobada()               #menu de compra y aprobacion/cancelacion de esta
                elif soli == "3":
                    solicitud_ingreso_venta = False
                    respuesta_menu=True
                else:
                    print("Opción no válida")        
        elif opcion_menu_principal == 'SALIR':      #sale del menu al menu principal
            print('Ha salido del menu principal')
            respuesta_menu=False
            

ejecutar()                

