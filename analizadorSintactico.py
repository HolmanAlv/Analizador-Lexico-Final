import analizadorLexico as AL

def eliminar_duplicados(tokens):
    vistos = set()
    resultado = []
    for token in tokens:
        if token[2] not in vistos:
            resultado.append(token)
            vistos.add(token[2])
    return resultado

def is_expression(tokens):
    return tokens[0][0] in ['IDENTIFIER', 'INTEGER_CONSTANT', 'FLOAT_CONSTANT', 'STRING_CONSTANT', 'CHAR_CONSTANT', 'BOOL_CONST']

def parse_declaration(tokens):
    # Verifica si es una declaración de variable sin asignación
    if len(tokens) == 3 and tokens[1][0] == 'IDENTIFIER' and tokens[2][0] == 'TERMINAL_EXPRESSION':
        return 'Declaración de variable: {} {}'.format(tokens[0][1], tokens[1][1])
    return None

def parse_assignment(tokens):
    if len(tokens) < 3 or tokens[-1][0] != 'TERMINAL_EXPRESSION':
        return "Error: La asignación es incompleta o falta el ; al final."
    
    if (tokens[0][0] == 'DATA_TYPE' and len(tokens) >= 5 and tokens[1][0] == 'IDENTIFIER' and
        tokens[2][0] == 'OPERATOR_ASSIGN' and is_expression(tokens[3:-1])):
        return 'Asignación de variable con declaración: {} {} = {}'.format(tokens[0][1], tokens[1][1], tokens[3][1])
    
    elif (tokens[0][0] == 'IDENTIFIER' and tokens[1][0] == 'OPERATOR_ASSIGN' and
          is_expression(tokens[2:-1])):
        return 'Asignación de variable: {} = {}'.format(tokens[0][1], tokens[2][1])
    return None

def analisis_sintactico(tokens):
    resultados = []
    index = 0
    while index < len(tokens):
        if tokens[index][0] == 'DATA_TYPE' or tokens[index][0] == 'IDENTIFIER':
            # Busca el fin de la sentencia
            end_index = index
            while end_index < len(tokens) and tokens[end_index][0] != 'TERMINAL_EXPRESSION':
                end_index += 1
            # Extrae la sublista de la sentencia actual
            sentence = tokens[index:end_index+1]
            
            # Intenta parsear como declaración o asignación
            result = parse_assignment(sentence) or parse_declaration(sentence)
            if result:
                resultados.append(result)
            index = end_index + 1
        else:
            index += 1
    return resultados

def realizarAnalisisSintactico(archivoTexto):
    tokens = eliminar_duplicados(AL.analisis_lexico(archivoTexto))
    resultados = analisis_sintactico(tokens)
    respuesta = ""
    for resultado in resultados:
        respuesta += resultado + "\n"
    return respuesta

# Código de prueba con ejemplos de asignaciones y declaraciones
archivo_ejemplo = """
int x;
x = 5;
float y;
y = 3.14;
String mensaje;
mensaje = "Hola, mundo!";
"""

print(realizarAnalisisSintactico(archivo_ejemplo))