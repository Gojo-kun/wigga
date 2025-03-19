from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form.get('nome')
        return f"""
        <html>
        <head>
            <style>
                body {{ background-color: black; color: white; text-align: center; font-family: Arial, sans-serif; }}
                form {{ margin-top: 20%; }}
                input, button {{ padding: 10px; margin: 10px; border: none; border-radius: 20px; }}
                input {{ background-color: #333; color: white; width: 200px; text-align: center; }}
                button {{ background-color: white; color: black; cursor: pointer; width: 120px; }}
                .gallery {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; justify-items: center; }}
                .gallery img:nth-child(1) {{ width: 400px; height: auto; }}
                .gallery img:nth-child(2) {{ width: 250px; height: auto; }}
                .gallery img:nth-child(3) {{ width: 500px; height: auto; }}
            </style>
        </head>
        <body>
            <h1>Bem-vindo, {nome}!</h1>
            <div class="gallery">
                <img src="/static/images/img1.jpg" alt="Imagem 1">
                <img src="/static/images/img2.jpg" alt="Imagem 2">
                <img src="/static/images/img3.jpg" alt="Imagem 3">
            </div>
        </body>
        </html>
        """
    return '''
        <html>
        <head>
            <style>
                body { background-color: black; color: white; text-align: center; font-family: Arial, sans-serif; }
                form { margin-top: 20%; }
                input, button { padding: 10px; margin: 10px; border: none; border-radius: 20px; }
                input { background-color: #333; color: white; width: 200px; text-align: center; }
                button { background-color: white; color: black; cursor: pointer; width: 120px; }
            </style>
        </head>
        <body>
            <form method="post">
                <label for="nome">Digite seu nome:</label><br>
                <input type="text" id="nome" name="nome" required><br>
                <button type="submit">Entrar</button>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
