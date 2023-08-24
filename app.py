from flaskr import create_app
from .modelos import db, Cancion
from .modelos import db, Album
from .modelos import db, Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba
with app.app_context():
    c = Cancion(titulo='prueba', minutos=2, segundos=25, interprete='jhon_araujo')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    a = Album(titulo='pepe', año=2021, descripcion='exito crossover', medio='cd')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    u = Usuario(nombre_usuario='juanito', contrasena=2342234)
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())