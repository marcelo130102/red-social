from flask import Flask, render_template

app = Flask(__name__)

# Rutas
@app.route('/login')
def login():
    # Ejemplo de posts (puedes reemplazar esto con lógica de base de datos)
    return render_template('login.html')

@app.route('/')
def index():
    # Ejemplo de posts (puedes reemplazar esto con lógica de base de datos)
    posts = [
        {'user': 'Usuario1', 'content': '¡Hola, mundo!', 'img': 'https://external.faqp4-2.fna.fbcdn.net/emg1/v/t13/13546349427847062928?url=https%3A%2F%2Felcomercio.pe%2Fresizer%2FqpkOmW8Ky06GRF7cAZiXUFZwL58%3D%2F980x528%2Fsmart%2Ffilters%3Aformat%28jpeg%29%3Aquality%2875%29%2Fcloudfront-us-east-1.images.arcpublishing.com%2Felcomercio%2FXSIPNAL7BRF73KSOUAA3ESJDQI.jpg&fb_obo=1&utld=elcomercio.pe&stp=c0.5000x0.5000f_dst-jpg_flffffff_p500x261_q75&_nc_eui2=AeEWrbq3tSsM3AVla19diAMCIt8kIX9gEXgi3yQhf2AReK1Pi-SILm7IiD3996SCKQnhOlkeI3FyCSL3bPBhqBMK&ccb=13-1&oh=06_AbH_wnP4e3Lig7H_dXLbp1H8T7f54Orb8uSUwqc2s9tGuQ&oe=65924F93&_nc_sid=c63717'},
        {'user': 'Usuario2', 'content': 'Bienvenido a mi red social.'},
        {'user': 'Usuario3', 'content': '¡Esto es una prueba!'},
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)