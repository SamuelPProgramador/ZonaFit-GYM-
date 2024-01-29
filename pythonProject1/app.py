from flask import Flask, render_template, redirect, url_for

import cliente_DAD
from cliente import Cliente
from cliente_DAD import ClienteDAD
from cliente_form import ClienteForm

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #recuper los cliente de la bd
    clientes_db = ClienteDAD.selecionar()

    #Creamos un objeto de cliente vacio
    cliente = Cliente()
    cliente_foma =ClienteForm(obj=cliente)
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db, forma=cliente_foma)

@app.route('/guardar', methods=['POST'])
def guardar():
    #creamos los objetos vacios de cliente
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            # guardamos el nuevo cliente en la db
            ClienteDAD.insertar(cliente)
        else:
            ClienteDAD.actualizar(cliente)
        #redireccionar a la pagina de inicio
        return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAD.selecionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    cliente_db = ClienteDAD.selecionar()
    return render_template('index.html', titulo=titulo_app,
                            cliente=cliente_db,
                            forma=cliente_forma)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAD.eliminar(cliente)
    return redirect(url_for('inicio'))


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

if __name__ =='__main__':
    app.run(debug=True)