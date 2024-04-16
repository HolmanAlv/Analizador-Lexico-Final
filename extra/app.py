from flask import Flask, request, render_template_string
import analizador_lexico as AL
app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Cargar Archivo</title>
</head>
<body>
    <h2>Cargar Archivo TXT</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".txt">
        <input type="submit">
    </form>
</body>
</html>
"""

@app.route('/')
def form():
    return HTML_FORM

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No hay archivo cargado', 400
    file = request.files['file']
    if file.filename == '':
        return 'Ningún archivo seleccionado', 400
    if file and file.filename.endswith('.txt'):
        content = file.read().decode('utf-8')
        processed_content = process_content(content)
        return f'Contenido Procesado: <pre>{processed_content}</pre>'
    return 'Tipo de archivo no permitido', 400

def process_content(content):
    tokens = AL.analisis_lexico(content)
    tokens = AL.eliminar_duplicados(tokens)

    respuesta = ""
    for token in tokens:
        respuesta +=" "+ token + "\n"
        print(token) 

    return respuesta # Ejemplo de procesamiento: convertir a mayúsculas

if __name__ == '__main__':
    app.run(debug=True)
