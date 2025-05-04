from flask import Flask, render_template

app = Flask(__name__)

titulo_app = "Zona Fit (GYM)"

@app.route('/')
@app.route('/index.html') # url: http://localhost:5000/index.html
def hola_mundo(): # url: http://localhost:5000/
    app.logger.debug('Entramos al path de inicio /')
    return render_template('index.html', titulo = titulo_app) # Necesario tener el index en la carpeta templates


if __name__ == '__main__':
    app.run(debug=True)
    
