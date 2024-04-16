import re

# Lectura del archivo
# with open("archivo.txt", "r") as file:
#     archivo = file.read()

# Patrones de expresiones regulares para los diferentes tokens.
patrones = {
    'INTEGER_CONSTANT': r'\b\d+\b',
    'FLOAT_CONSTANT': r'\b\d+\.\d+\b',
    'STRING_CONSTANT': r'"[^"\\]*(\\.[^"\\]*)*"',
    'CHAR_CONSTANT': r"'.'",
    'BOOL_CONST': r'\b(true|false)\b',
    'KEY_WORD': r'\b(if|else|while|do|for|return|switch|case|break|function|import|default|try|catch|package|extends|implements|new|super|this|throw|null)\b',
    'ACCESS_MODIFIER': r'\b(private|protected|public)\b',
    'DATA_TYPE': r'\b(int|byte|float|double|char|String|boolean|void|abstract|class|final|static|interface|long|short|var)\b',
    'OPERATOR': r'(\+\+|--|==|!=|<=|>=|&&|\|\||[+\-*/%<>&|!])',
    'SEPARATOR': r'[;,\[\]{}()]',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
}

# Función para el análisis léxico que devuelve una lista de tokens encontrados en el archivo.
def analisis_lexico(archivo):
    tokens_encontrados = []
    for token_tipo, token_patron in patrones.items():
        for match in re.finditer(token_patron, archivo):
            tokens_encontrados.append((token_tipo, match.group(), match.start()+1))
    return sorted(tokens_encontrados, key=lambda x: x[2])

# Eliminar tokens duplicados
def eliminar_duplicados(tokens):
    vistos = set()
    resultado = []
    
    for token in tokens:
        if token[2] not in vistos:
            resultado.append(token)  # Añadimos el token a la lista de resultados
            vistos.add(token[2])  # Marcamos el identificador como visto
    
    return resultado



def tuplaToString(tupla):
    string = ""
    for element in tupla:
        string += str(element)+ ", "
    return string


# Llamar a la función e imprimir los resultados.

def realizarAnalisis(archivoTexto):
    tokens = eliminar_duplicados(analisis_lexico(archivoTexto))
    respuesta = ""
    for token in tokens:
        respuesta += tuplaToString(token)+"\n"
    return(respuesta)

    
# Prueba por consola
# print(realizarAnalisis(archivo))