from app import app
# from models.clave_clientes import ClavesClientes
from models import ClavesClientes, Clientes, Grupos, HistorialOp, MensajeClientes, Operaciones

@app.route('/')
@app.route('/index')
def index():
    operaciones = Operaciones.query.all()
    print("c", operaciones)
    # mensaje_clientes = MensajeClientes.query.all()
    # print("c", mensaje_clientes)
    # grupos = Grupos.query.all()
    # print("c", grupos)
    # clientes = Clientes.query.all()
    # print("c", clientes)
    # claves = ClavesClientes.query.all()
    # print("c", claves)
    return "Hello, World!"
