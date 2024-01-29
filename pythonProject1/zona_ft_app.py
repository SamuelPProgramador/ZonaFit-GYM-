from cliente import Cliente
from cliente_DAD import ClienteDAD

print('*** Clientes de Zona Fit (GYM) ***')
opc = None
while opc !=5:
    print('''Menu
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir ''')
    opc = int(input('Elije  una opcion --> '))
    if opc == 1: #listar clientes
        clientes = ClienteDAD.selecionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
        print('\n')

    elif opc == 2: #agregar cliente
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = int(input('Escribe la membresia: '))
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var,
                          membresia=membresia_var)
        clientes_insertados = ClienteDAD.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}\n')

    elif opc == 3: #modificar
        id_cliente_var = int(input('Escribe le id: '))
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = int(input('Escribe la membresia: '))
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAD.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}\n')

    elif opc == 4:
        id_cliente_var = int(input('Escriba el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAD.eliminar(cliente)
        print(f'Clientes elimnados: {clientes_eliminados}\n')

else:
    print('Saliendo de la aplicacion...')