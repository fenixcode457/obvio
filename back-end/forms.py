from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    registro =  SubmitField('Registro')


class UbicacionForm(FlaskForm):
    colonia = StringField('Nombre', validators=[DataRequired()])
    calle = StringField('Apellido', validators=[DataRequired()])
    estado = SelectField('Category', choices = [('Clothes', 'Clothes'), ('Watch', 'Watch')])
    codigopostal = StringField('Password', validators=[DataRequired()])
    registro =  SubmitField('Registro')


class ProductForm(FlaskForm):
    nombreProducto = StringField('Nombreproducto', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    registro =  SubmitField('Registro')
