from cliente import Cliente
from conexion import Conexion

class ClienteDAD:
    SELECIONAR = 'SELECT * FROM cliente'
    SELECIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERTAR ='INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR ='UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def selecionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def selecionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECIONAR_ID, valores)
            registro = cursor.fetchone()
            #Mapeo clase-tabla cliente
            cliente = Cliente(registro[0], registro[1],
                              registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'ha ocurrido un error id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'ha ocurrido un error {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'ha ocurrido un error {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
if __name__ == '__main__':
    # insertar
    #cliente1 = Cliente(nombre='Alejandra', apellido='Lopez', membresia=300)
    #clientes_insertados = ClienteDAD.insertar(cliente1)
    #print(f'Clientes insertados: {clientes_insertados}')

    #Actualizar
   # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    #clientes_actualizar = ClienteDAD.actualizar(cliente_actualizar)
    #print(f'Clientes actualizados: {clientes_actualizar}')

    #Eliminar cliente
    #cliente_eliminar = Cliente(id=3)
    #cliente_eliminado = ClienteDAD.eliminar(cliente_eliminar)
    #print(f'Clientes eliminado: {cliente_eliminado}')

    #selecionar clientes
    clientes = ClienteDAD.selecionar()
    for cliente in clientes:
        print(cliente)