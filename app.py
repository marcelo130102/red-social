from flask import Flask, render_template, request, jsonify as JSONResponse, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import base64


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.secret_key = 'super secret key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Necesitamos
# 1. Modelos de datos para Usuario, Post y Comentarios
# 2. Lógica para añadir usuarios a la base de datos y post
# 3. Modificar las rutas para que muestren los datos de la base de datos

with app.app_context():
    db.create_all()



# Crear modelos de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('%s', '%s', '%s', '%s')" % (self.username, self.email, self.name, self.posts)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_img = db.Column(db.String(300), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.content


def check_auth(username, password):
    """Esta función es llamada para verificar si un usuario es válido."""
    user = User.query.filter_by(username=username).first()
    if user:
        return user.password == password
    return False

def requires_auth(view):
    def wrapper_view(*args, **kwargs):
        print(session)
        if 'user' not in session or not check_auth(session.get('user'), session.get('password')):
            if request.endpoint == 'index':
                return redirect(url_for('login'))
        return view(*args, **kwargs)
    wrapper_view.__name__ = view.__name__
    return wrapper_view

# Rutas
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        auth_header = request.headers.get('Authorization')
        # Lógica para verificar usuario
        if auth_header and auth_header.startswith('Basic '):
            #Decodificar el header
            enconded_creds = auth_header[len('Basic '):]
            decoded_creds = base64.b64decode(enconded_creds).decode('utf-8')
            username, password = decoded_creds.split(':')
            # Verificar si el usuario existe
            if check_auth(username, password):
                session['user'] = username
                session['password'] = password
                return redirect(url_for('index'))
            else:
                return JSONResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)          
    if request.method == 'GET':
        return render_template('login.html')

    return JSONResponse({'error': 'Método no permitido'}, status=405)



@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

@app.route('/')
@requires_auth
def index():
    # Ejemplo de posts (puedes reemplazar esto con lógica de base de datos)
    posts = []
    all_users = User.query.all()
    for user in all_users:
        for post in user.posts:
            posts.append({'user': user.username, 'content': post.content, 'img': post.post_img, 'date_posted': post.date_posted})
            
    posts = sorted(posts, key=lambda x: x['date_posted'])

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)