from flask import Flask, render_template, request, url_for, session
from flask_migrate import Migrate
from werkzeug.utils import redirect

from dababase import db
from forms import UsuarioForm ,ProductForm
from models import Usuario, Producto

app = Flask(__name__)


#cofiguración de la bd

USER_DB = 'postgres'
PASS_DB = 'mundo2014'
URL_DB = 'localhost'
NAME_DB = 'obio'
FULL_URL_DB= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


#configurar flask
migrate = Migrate()
migrate.init_app(app, db)

#configurar de flask-wtf
app.config['SECRET_KEY']='hackaton'

app.secret_key ='hackatoon'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    return render_template('index.html')

@app.route('/login',methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['email']

        #agregar el usuario a la sesión
        session['email'] = usuario
    return render_template('login.html')

@app.route('/registro',methods=['GET','POST'])
def agregar():
    usuario = Usuario()
    usuarioForm = UsuarioForm(obj=usuario)
    if request.method == 'POST':
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            app.logger.debug(f'Usuario:{usuario}')
            #insertar db
            db.session.add(usuario)
            db.session.commit()


    return render_template('registro.html', forma = usuarioForm)


@app.route('/producto',methods=['GET','POST'])
def regProducto():
    producto = Producto()
    productForm = ProductForm(obj=producto)
    if request.method == 'POST':
        if productForm.validate_on_submit():
            productForm.populate_obj(producto)
            app.logger.debug(f'producto:{producto}')
            #insertar db
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('regProducto'))


    return render_template('producto.html', forma = productForm)