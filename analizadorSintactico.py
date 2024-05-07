
import analizadorLexico as AL
def eliminar_duplicados(tokens):
    vistos = set()
    resultado = []
    
    for token in tokens:
        if token[2] not in vistos:
            resultado.append(token)  # Añadimos el token a la lista de resultados
            vistos.add(token[2])  # Marcamos el identificador como visto
    
    return resultado


def is_expression(tokens):
    # Aquí podrías implementar una lógica más completa para verificar si los tokens forman una expresión válida
    # Por simplicidad, solo verificamos si el primer token es un identificador, constante, etc.
    return tokens[0][0] in ['IDENTIFIER', 'INTEGER_CONSTANT', 'FLOAT_CONSTANT', 'STRING_CONSTANT', 'CHAR_CONSTANT', 'BOOL_CONST']

def parse_assignment(tokens):
    # Verificamos si hay tokens suficientes para una asignación
    if len(tokens) < 4 or tokens[-1][0] != 'TERMINAL_EXPRESSION':
        return "Error: La asignación es incompleta o falta el ; al final."
    
    # Comprobamos la estructura de la asignación
    if (tokens[0][0] == 'DATA_TYPE' and
        tokens[1][0] == 'IDENTIFIER' and
        tokens[2][0] == 'TERMINAL_EXPRESSION' or
        tokens[3][0] == 'IDENTIFIER' and
        tokens[4][0] == 'OPERATOR_ASSIGN' and
        is_expression(tokens[5:-1])):
        return 'Asignación de variable: {} {} = {}'.format(tokens[0][1], tokens[1][1], tokens[5][1])
    elif (tokens[0][0] == 'IDENTIFIER' and
          tokens[1][0] == 'OPERATOR_ASSIGN' and
          is_expression(tokens[2:-1])):
        return 'Asignación de variable: {} = {}'.format(tokens[0][1], tokens[2][1])
    else:
        return "Error: La estructura de la asignación no es válida."

# Aquí estaría tu código de funciones y gramática, seguido por el código actualizado para el análisis de asignaciones.

# Función principal para análisis sintáctico
def analisis_sintactico(archivoTexto):
    tokens = eliminar_duplicados(AL.analisis_lexico(archivoTexto))
    # Intentamos analizar cada tipo de declaración
    resultados = []
    for token in tokens:
        if token[0] == 'IDENTIFIER':
            # Si el token es un identificador, intentamos parsear una asignación
            resultado = parse_assignment(tokens[tokens.index(token):])
            resultados.append(resultado)
    return resultados

# Llamar a la función e imprimir los resultados.
def realizarAnalisisSintactico(archivoTexto):
    resultados = analisis_sintactico(archivoTexto)
    respuesta = ""
    for resultado in resultados:
        respuesta += resultado + "\n"
    return respuesta

# Aquí definimos un ejemplo de archivo de texto con una asignación que incluye una declaración de tipo de dato.
archivo_ejemplo = """
int x;
x = 5;
float y;
y = 3.14;
String mensaje;
mensaje = "Hola, mundo!";
"""

# Llamamos a la función para realizar el análisis sintáctico y mostramos los resultados.
print(realizarAnalisisSintactico(archivo_ejemplo))
