from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

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


# Rutas
@app.route('/login')
def login():
    # Ejemplo de posts (puedes reemplazar esto con lógica de base de datos)
    return render_template('login.html')

@app.route('/')
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