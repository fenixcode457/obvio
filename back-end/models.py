
from app import  db


class TipoUsuario(db.Model):
    __tablename__ = 'tipousuario'
    idTipoUsuario = db.Column(db.Integer, primary_key=True)
    nombreTipo = db.Column(db.String(45))
    descripcion = db.Column(db.String(100))

    def __str__(self):
        return  (

            f'Id:{self.idTipoUsuario},'
            f'NombreTipo:{self.nombreTipo},'
            f'Descripcion:{self.descripcion}'

        )



class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    apellido = db.Column(db.String(45))
    email = db.Column(db.String(55))
    password = db.Column(db.String(8))
    fkTipoUsuario =  db.Column(db.Integer, db.ForeignKey("tipousuario.idTipoUsuario"))


    def __str__(self):
        return  (

            f'IdUsuario:{self.idUsuario},'
            f'nombre:{self.nombre},'
             f'apellido:{self.apellido},'
            f'email:{self.email},'
            f'password:{self.password},'
            f'fkTipoUsuario:{self.fkTipoUsuario} '

        )


class Ubicacion(db.Model):
    idUbicacion = db.Column(db.Integer, primary_key=True)
    colonia = db.Column(db.String(45))
    calle = db.Column(db.String(45))
    estado = db.Column(db.String(55))
    codigopostal = db.Column(db.String(6))
    fkUsuario =  db.Column(db.Integer, db.ForeignKey("usuario.idUsuario"))


    def __str__(self):
        return  (

            f'idUbicacion:{self.idUbicacion},'
            f'colonia:{self.colonia},'
             f'calle:{self.calle},'
            f'estado:{self.estado},'
            f'codigopostal:{self.codigopostal},'
            f'fkUsuario:{self.fkUsuario} '

        )


class Provedor(db.Model):
    __tablename__ = 'provedor'
    idProvedor = db.Column(db.Integer, primary_key=True)
    nombreprovedor = db.Column(db.String(70))
    telefono =db.Column(db.String(15))
    fkUsuario =  db.Column(db.Integer, db.ForeignKey("usuario.idUsuario"))

    def __str__(self):
        return  (

            f'idProvedor:{self.idProvedor},'
            f'nombreprovedor:{self.nombreprovedor},'
            f'telefono:{self.telefono},'
            f'fkUsuario:{self.fkUsuario}'

        )

class Producto(db.Model):
    idProducto = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(57))
    tipo = db.Column(db.String(38))
    precio = db.Column(db.String(3))
    foto = db.Column(db.String(48))
    fkProvedor=  db.Column(db.Integer, db.ForeignKey("provedor.idProvedor"))

    def __str__(self):
        return (

            f'idProducto:{self.idProducto},'
            f'nombreProducto:{self.nombreProducto},'
            f'tipo:{self.tipo},'
            f'precio:{self.precio},'
            f'foto:{self.foto},'
            f'fkProvedor:{self.fkProvedor}'

        )
